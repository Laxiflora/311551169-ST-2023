all: heap_out_of_bounds.c stack_out_of_bounds.c global_out_of_bounds.c use_after_free.c use_after_return.c stack_jump.c normal.c
	gcc heap_out_of_bounds.c -fsanitize=address -o heap_out_of_bounds
	gcc stack_out_of_bounds.c -o stack_out_of_bounds
	gcc global_out_of_bounds.c -fsanitize=address -o global_out_of_bounds
	gcc use_after_free.c  -o use_after_free
	gcc use_after_return.c -fsanitize=address -o use_after_return
	gcc stack_jump.c -fsanitize=address -o stack_jump
	gcc normal.c -fsanitize=address -o normal