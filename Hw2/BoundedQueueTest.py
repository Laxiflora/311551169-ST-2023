import unittest
from BoundedQueue import BoundedQueue
from unittest.mock import MagicMock


class BoundedQueueTest(unittest.TestCase):
    
    def testInit_C1(self):
        with self.assertRaises(ValueError):
            self.obj = BoundedQueue(-1)


    def testInit_C2(self):
        self.obj = BoundedQueue(1)


    # (capacity = 1, o = E, size = 1)
    def testenqueue_C1(self):
        self.obj = BoundedQueue(1)
        self.obj.enqueue(0)
        with self.assertRaises(RuntimeError):
            self.obj.enqueue(1)

    # (capacity = 1, o = None, size = 1)
    def testenqueue_C2(self):
        self.obj = BoundedQueue(1)
        self.obj.enqueue(0) # ensure size = 1
        with self.assertRaises(TypeError):
            self.obj.enqueue(None)


    # (capacity = 1, o = E, size = 0)
    def testenqueue_C3(self):
        self.obj = BoundedQueue(1)
        self.obj.enqueue(1)


    # (size = 0)
    def testdequeue_C1(self):
        self.obj = BoundedQueue(1)
        with self.assertRaises(RuntimeError):
            self.obj.dequeue()


    # (size = 1)
    def testdequeue_C2(self):
        self.obj = BoundedQueue(1)
        self.obj.enqueue(0) # ensure size = 1
        self.obj.dequeue()


    # (size = 0)
    def testis_empty_C1(self):
        self.obj = BoundedQueue(1)
        self.assertTrue(self.obj.is_empty())

    # (size = 1)
    def testis_empty_C2(self):
        self.obj = BoundedQueue(1)
        self.obj.enqueue(0) # ensure size = 1
        self.assertFalse(self.obj.is_empty())


    # (capacity =1, size =1 )
    def testis_full_C1(self):
        self.obj = BoundedQueue(1)
        self.obj.enqueue(0) # ensure size = 1
        self.assertTrue(self.obj.is_full())


    # (capacity =1, size =0 )
    def testis_full_C2(self):
        self.obj = BoundedQueue(1)
        self.assertFalse(self.obj.is_full())



if __name__ == "__main__":
    unittest.main()
    
