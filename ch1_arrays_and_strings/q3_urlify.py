import unittest

class Urlify():

    def run(self, string):
        string_list = list(string)
        new_list = []

        for letter in string_list:
            if letter == " ":
                new_list.append("%20")
            else:
                new_list.append(letter)
        return "".join(new_list)


class TestUrlify(unittest.TestCase):
    def test_urlify(self):
        word = "Cool kids in class"

        answer = "Cool%20kids%20in%20class"

        answer2 = Urlify().run(word)

        self.assertEqual(answer, answer2)




if __name__ == "__main__":
    unittest.main()