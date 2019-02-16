import unittest


class AnimalQueue():
    count = 0

    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def dequeue(self):
        dog_num = self.dog_queue.peek().count
        cat_num = self.cat_queue.peek().count

        if dog_num > cat_num:
            return self.cat_queue.dequeue()
        else:
            return self.dog_queue.dequeue()

    def dequeue_cat(self):
        return self.cat_queue.dequeue()

    def dequeue_dog(self):
        return self.dog_queue.dequeue()


    def enqueue_cat(self, name):
        count = AnimalQueue.count
        node = Node(count=count, name=name)
        self.cat_queue.enqueue(node)
        AnimalQueue.count += 1


    def enqueue_dog(self, name):
        count = AnimalQueue.count
        node = Node(count=count, name=name)
        self.dog_queue.enqueue(node)
        AnimalQueue.count += 1


class Queue():
    def __init__(self):
        self._array = [None] * 10
        self.count = 0
        self.front = 0

    def expand_list_if_necessary(self):
        if self.count >= len(self._array):
            for _ in range(10):
                self._array.append(None)

    def enqueue(self, element):
        self.expand_list_if_necessary()

        self._array[self.count] = element
        self.count += 1

    def dequeue(self):

        element = self.peek()
        self._array[self.front] = None
        self.front += 1
        return element

    def peek(self):
        return self._array[self.front]

    def __repr__(self):
        return self._array.__repr__()


class Node():
    _id = 0
    def __init__(self, count, name):
        self.count = count
        self.name = name
        Node._id += 1
        self.id = Node._id

    def __repr__(self):
        return self.name


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.q.enqueue(4)
        self.q.enqueue(9)
        self.q.enqueue(-39)
        self.q.enqueue(-89)


        self.animal_q = AnimalQueue()
        # c = Node("fluffy cat")
        self.animal_q.enqueue_cat('fluffy cat')
        self.animal_q.enqueue_dog('sparky dog')
        self.animal_q.enqueue_cat('paws cat')
        self.animal_q.enqueue_cat('puff cat')
        self.animal_q.enqueue_dog('luger dog')


    def testAnimalDequeue(self):
        first_animal = self.animal_q.dequeue()
        second_animal = self.animal_q.dequeue()
        self.assertEqual(first_animal.name, 'fluffy cat')
        self.assertEqual(second_animal.name, 'sparky dog')

    def testDogDequeue(self):
        first_dog = self.animal_q.dequeue_dog()
        second_dog = self.animal_q.dequeue_dog()
        self.assertEqual(first_dog.name, 'sparky dog')
        self.assertEqual(second_dog.name, 'luger dog')
        self.animal_q.enqueue_cat('yo cat')

    def testPeek(self):
        self.assertEqual(4, self.q.peek())

    def testDequeue(self):
        self.assertEqual(4, self.q.dequeue())
        self.assertEqual(9, self.q.dequeue())
        self.assertEqual(-39, self.q.dequeue())
        self.assertEqual(-89, self.q.dequeue())

        # Assert _array is All none
        for x in self.q._array:
            self.assertEqual(x, None)

    def testExpandList(self):
        q = Queue()
        for num in range(22):
            q.enqueue(num)
        self.assertEqual(q._array[21], 21)
        self.assertEqual(0, q.dequeue())


if __name__ == '__main__':
    unittest.main()
