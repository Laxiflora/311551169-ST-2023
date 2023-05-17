import angr
import sys

main_addr = 0x4011a9
find_addr = 0x401369
avoid_addr = 0x401348

def handle_fgets_real_input(raw_input):
    idx = 0
    for c in raw_input:
        if c == ord('\n') or c == ord('\0'):
            break
        idx += 1
    return raw_input[:idx]

class Myscanf(angr.SimProcedure):
    def run(self, fmt, n):
        fd = self.state.posix.get_fd(sys.stdin.fileno())
        data, ret_size = fd.read_data(4)
        #fd.read_data(1)  # to skip '\n' or ' '
        self.state.memory.store(n, data)
        return 4

proj = angr.Project('./src/prog', load_options={'auto_load_libs': False})
proj.hook_symbol('__isoc99_scanf', Myscanf(), replace=True)

state = proj.factory.blank_state(addr=main_addr)

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=find_addr, avoid=avoid_addr)
if simgr.found:
    print(simgr.found[0].posix.dumps(sys.stdin.fileno()))
    
    s = simgr.found[0].posix.dumps(sys.stdin.fileno())
    f = open('solve_input','w+')
    d = []
    for i in range(0, 15):
        input = int.from_bytes(s[i * 4 : i * 4 + 4], byteorder='little')
        f.write('%d\n' % input)
        d.append(input)
    f.close()
    print(d)

else:
    print('Failed')