'''
// Introduction to Software Testing
// Authors: Paul Ammann & Jeff Offutt
// Chapter 3, page ??
// See BoundedQueueTest.java for JUnit tests. (Instructor only)
'''

class BoundedQueue:
	'''
	// Overview:  a BoundedQueue is a mutable, bounded FIFO data structure
	// of fixed size , with size being set in the constructor
	// A typical Queue is [], [o1], or [o1, o2], where neither o1 nor o2
	// are ever null.  Older elements are listed before newer ones.
	'''
	def __init__(self, cap):
		if cap < 0:
			raise ValueError('BoundedQueue.constructor')
		self.capacity = cap
		self.elements = [None] * self.capacity
		self.size = 0
		self.front = 0
		self.back  = 0

	def enqueue(self, o):
		if o is None:
			raise TypeError('BoundedQueue.enqueue')
		elif self.size == self.capacity:
			raise RuntimeError('BoundedQueue.enqueue')
		else:
			self.size += 1
			self.elements[self.back] = o
			self.back = (self.back + 1) % self.capacity
	
	def dequeue(self):
		if self.size == 0:
			raise RuntimeError('BoundedQueue.enqueue')
		else:
			self.size -= 1
			o = self.elements[self.front % self.capacity]
			self.elements[self.front] = None
			self.front = (self.front + 1) % self.capacity
			return o
	
	def is_empty(self):
		return self.size == 0

	def is_full(self):
		return self.size == self.capacity
	
	def __str__(self):
		result = '['
		for i in range(self.size):
			result += str(self.elements[(self.front + i) % self.capacity])
			if i < self.size - 1:
				result += ', '
		result += ']'
		return result

if __name__ == '__main__':
	bq = BoundedQueue(10)

	for i in range(1, 11):
		bq.enqueue(i)
	print(bq)

	bq.dequeue()

	print(bq.is_empty())
	print(bq.is_full())
	print(bq)

