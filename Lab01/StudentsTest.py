import unittest
import Students

class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary','Thomas','Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print("Start set_name test\n")
        for index,name in enumerate(self.user_name,0):
            self.students.set_name(name)
            self.user_id.append( (name,index) ) # to link the student to specify id
        
        for index,name in enumerate(self.user_name,0):
            self.assertEqual( self.students.name[index] , self.user_name[index] )
            print(f"{index} {self.students.name[index]}")

        print("\nFinish set_name test\n\n")


    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print("Start get_name test\n")
        print(f"user_id length = {len(self.user_id)}")
        print(f"user_name length = {len(self.user_name)}")

        for i in range(0,5):
            if i < len(self.user_name):
                self.assertEqual( (self.students.get_name(i),i) , self.user_id[i] )
            else:
                self.assertEqual(self.students.get_name(i), 'There is no such user')



if __name__ == '__main__': # pragma: no cover
    t = Test()
    t.test_0_set_name()
    t.test_1_get_name()
