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
            for exist_id in self.user_id:
                self.assertFalse(id == exist_id)
            print(f"{id} {name}")
            self.user_id.append( id ) # to link the student to specify id
        

        print("\nFinish set_name test\n\n")


    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print("Start get_name test\n")
        print(f"user_id length = {len(self.user_id)}")
        print(f"user_name length = {len(self.user_name)}\n")

        #Regular case
        for name,id in zip(self.user_name,self.user_id):
            self.assertEqual( self.students.get_name(id) , name  )
            print(f"id {id} : {self.students.get_name(id)}")
        
        #Mex
        mex = 0
        for i in range(len(self.user_id)+1):
            if i not in self.user_id:
                mex = i
                break

        self.assertEqual(self.students.get_name(mex), 'There is no such user')
        print(f"id {mex} : There is no such user")

        print("\nFinish get_name test")

if __name__ == '__main__': # pragma: no cover
    t = Test()
    t.test_0_set_name()
    t.test_1_get_name()
