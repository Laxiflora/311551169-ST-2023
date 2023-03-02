import unittest
from app import Application
from unittest.mock import MagicMock

class ApplicationTest(unittest.TestCase):


    def setUp(self):
        # stub
        Application.__init__ = MagicMock(return_value=None)
        self.app = Application()
        self.app.people = ["William", "Oliver", "Henry","Liam"]
        self.app.selected = ["William", "Oliver", "Henry"]
    
    def test_app(self):
        # mock
        #print("--select next person--")
        self.app.get_random_person = MagicMock(side_effect = ["William", "Oliver", "Henry", "Liam"])
        next_person = self.app.select_next_person()
        self.assertEqual(next_person,"Liam")
        print(f"{next_person} selected")

        # spy
        self.app.mailSystem.write = MagicMock(side_effect = lambda x:'Congrats, ' + x + '!')
        self.app.mailSystem.send = MagicMock()
        self.app.notify_selected()
        for i in self.app.selected:
            print(f"Congrats, {i}!")
        print("\n\n")
        print(self.app.mailSystem.write.call_args_list)
        print(self.app.mailSystem.send.call_args_list)
        self.assertEqual( self.app.mailSystem.write.call_count , self.app.mailSystem.send.call_count)


if __name__ == "__main__":
    unittest.main()
    
