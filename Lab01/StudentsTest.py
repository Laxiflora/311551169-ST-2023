import unittest
import Students

class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary','Thomas','Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print("Start set_name test\n")
        for name in self.user_name:
            id = self.students.set_name(name)
            for exist_name,exist_id in self.user_id:
                self.assertFalse(id == exist_id)
            print(f"{id} {self.students.name[id]}")
            self.user_id.append( (name,id) ) # to link the student to specify id
        

        print("\nFinish set_name test\n\n")


    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print("Start get_name test\n")
        print(f"user_id length = {len(self.user_id)}")
        print(f"user_name length = {len(self.user_name)}\n")

        for i in range(0,len(self.user_name)+2):
            if i < len(self.user_name):
                self.assertEqual( (self.students.get_name(i),i) , self.user_id[i] )
                print(f"id {self.user_id[i][1]} : {self.students.get_name(i)}")
            else:
                self.assertEqual(self.students.get_name(i), 'There is no such user')
                print(f"id {i} : There is no such user")

        print("\nFinish get_name test")



if __name__ == '__main__': # pragma: no cover
    t = Test()
    t.test_0_set_name()
    t.test_1_get_name()
