import unittest
from course_scheduling_system import CSS
from unittest.mock import MagicMock

class CSSTest(unittest.TestCase):


    def test_q1_1(self):
        self.setUp()
        self.CSS.check_course_exist = MagicMock(return_value = True)
        self.CSS.add_course(('Algorithms', 'Monday', 3, 4))
        self.assertEqual(self.CSS.get_course_list(), [('Algorithms', 'Monday', 3, 4)])

    def test_q1_2(self):
        self.setUp()
        self.CSS.check_course_exist = MagicMock(return_value = True)
        self.CSS.add_course(('DS', 'Tuesday', 3, 4))
        self.CSS.add_course(('DS', 'Tuesday', 3, 4))
        self.assertEqual(self.CSS.get_course_list(), [('DS', 'Tuesday', 3, 4)])

    def test_q1_3(self):
        self.setUp()
        self.CSS.check_course_exist = MagicMock(return_value = False)
        self.CSS.add_course(('DS', 'Tuesday', 3, 4))
        self.assertEqual(self.CSS.get_course_list(), [])


    def test_q1_4(self):
        self.setUp()
        self.CSS.check_course_exist = MagicMock(return_value = True)
        with self.assertRaises(TypeError):
            self.CSS.add_course(('Computer Network', 'third day', 3, 4))


    def test_q1_5(self):
        self.setUp()
        self.CSS.check_course_exist = MagicMock(return_value = True)
        self.CSS.add_course(('DS', 'Tuesday', 3, 4))
        self.CSS.add_course(('Computer Network', 'Wednesday', 3, 4))
        self.CSS.add_course(('Algorithms', 'Monday', 3, 4))
        self.CSS.remove_course(('Computer Network', 'Wednesday', 3, 4))

        self.assertEqual(self.CSS.get_course_list(), [('DS', 'Tuesday', 3, 4), ('Algorithms', 'Monday', 3, 4)])
        self.assertEqual(self.CSS.check_course_exist.call_count, 4)
        print(str(self.CSS))



    def test_q1_6_1(self):
        self.setUp()
        self.CSS.check_course_exist = MagicMock(return_value = True)
        with self.assertRaises(TypeError):
            self.CSS.add_course(('Computer Network', 'Wednesday')) # 8
        with self.assertRaises(TypeError):
            self.CSS.add_course((3, 'Wednesday', 3, 4)) # 10
        with self.assertRaises(TypeError):
            self.CSS.add_course(('Computer Network', 'Wednesday', "three", "four")) # 17

        self.CSS.remove_course(('DS', 'Tuesday', 3, 4)) #58

        

    def test_q1_6_2(self):
        self.CSS = CSS()
        self.CSS.check_course_exist = MagicMock(return_value = False) #56
        self.CSS.remove_course(('DS', 'Tuesday', 3, 4)) #56
        
        

    def setUp(self):
        self.CSS = CSS()
        self.CSS.check_course_exist = MagicMock(return_value = True)

if __name__ == "__main__":
    unittest.main()
    
