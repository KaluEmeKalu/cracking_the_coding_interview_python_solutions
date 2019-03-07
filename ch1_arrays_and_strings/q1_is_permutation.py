import unittest


class isPerm():
    def run1(self, word1, word2):
        sorted_word1 = sorted(word1)
        sorted_word2 = sorted(word2)

        if sorted_word1 == sorted_word2:
            return True
        return False

    def run2(self, word1, word2):

        def make_arr(word):
            arr = [0] * 128
            for letter in word:
                num = ord(letter)
                arr[num] += 1
            return arr

        return make_arr(word1) == make_arr(word2)


class testPerm(unittest.TestCase):

    def setUp(self):
        self.isperm = isPerm()

    def test_is_perm1(self):
        self.assertFalse(self.isperm.run1('bog', 'god'))
        self.assertTrue(self.isperm.run1('dog', 'god'))

    def test_is_perm2(self):
        self.assertFalse(self.isperm.run2('bog', 'god'))
        self.assertTrue(self.isperm.run2('dog', 'god'))

if __name__ == "__main__":
    unittest.main()