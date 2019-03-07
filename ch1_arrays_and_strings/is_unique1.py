# Implement an algorithm to determine if a String has all
# Unique characters
import unittest



class IsUnique():


    def is_unique1(self, string):
        seen = []
        for letter in string:
            if letter in seen:
                return False
            else:
                seen.append(letter)
        return True

    def is_unique2(self, string):
        arr = [False] * 128

        for letter in string:
            num = ord(letter)
            if arr[num]:
                return False
            else:
                arr[num] = True
        return True


class testIsUnique(unittest.TestCase):

    def setUp(self):
        self.obj = IsUnique()

    def test_is_unique1(self):
        self.assertFalse(self.obj.is_unique1('Bobby'))
        self.assertTrue(self.obj.is_unique1('Sugar'))

    def test_is_unique2(self):
        self.assertFalse(self.obj.is_unique2('Bobby'))
        self.assertTrue(self.obj.is_unique2('Sugar'))




if __name__ == "__main__":
    unittest.main()
