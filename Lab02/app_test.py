import unittest
from app import Application
from unittest.mock import MagicMock

class ApplicationTest(unittest.TestCase):


    def fake_mails(self,name):
        print(f"Congrats, {name}!")
        return "Congrats, "+name+"!"

    def setUp(self):
        # stub
        people = ["William", "Oliver", "Henry","Liam"]
        selected = ["William", "Oliver", "Henry"]

        Application.get_names = MagicMock(return_value = (people,selected))
        self.app = Application()
    
    def test_app(self):
        # mock
        #print("--select next person--")
        self.app.get_random_person = MagicMock(side_effect = ["William", "Oliver", "Henry", "Liam"])
        next_person = self.app.select_next_person()
        self.assertEqual(next_person,"Liam")
        print(f"{next_person} selected")

        # spy
        self.app.mailSystem.write = MagicMock(side_effect = self.fake_mails)
        self.app.mailSystem.send = MagicMock()
        self.app.notify_selected()
        print("\n\n")
        print(self.app.mailSystem.write.call_args_list)
        print(self.app.mailSystem.send.call_args_list)
        self.assertEqual( self.app.mailSystem.write.call_count , self.app.mailSystem.send.call_count)


if __name__ == "__main__":
    unittest.main()
    
