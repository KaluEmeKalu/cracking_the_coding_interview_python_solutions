import unittest

class IsPalindronePerm():

    def run(self, word):
        count_dict = self.make_d(word)

        odd_count = self.get_odd_count(count_dict)

        if self.is_even(word):
            return odd_count == 0
        else:
            return odd_count == 1

    def make_d(self, word):
        d = {}
        for letter in word:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        return d

    def is_even(self, word):
        n = len(word)
        return n % 2 == 0

    def get_odd_count(self, word_dict):
        odd_count = 0

        for key, value in word_dict.items():
            if value % 2 != 0:
                odd_count += 1
        return odd_count


class TestIsPalinDromePermutation(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        is_list = ['racecar', 'fhsmhfs', 'ohuhou']
        is_not_list = ['forward', 'problem', 'boot']

        obj = IsPalindronePerm()

        for word in is_list:
            self.assertTrue(obj.run(word))

        for word in is_not_list:
            self.assertFalse(obj.run(word))


if __name__ == "__main__":
    unittest.main()