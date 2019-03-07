import unittest

class OneAway():

    def run(self, tup):
        word1, word2 = tup

        n1, n2 = len(word1), len(word2)
        l1 = list(word1)
        l2 = list(word2)

        if n1 == n2:
            for i in range(n1):
                if l1[i] != l2[i]:
                    break
            l1[i] = l2[i]
            return l1 == l2

        elif abs(n1 - n2) == 1:
            big = max(l1, l2)
            small = min(l1, l2)

            for i in range(len(small)):
                if big[i] != small[i]:
                    big.pop(i)
                    break
            if len(small) != len(big):
                    big.pop()
            return big == small


        else:
            return False



class TestOneAway(unittest.TestCase):

    def test_one_away(self):
        obj = OneAway()

        ex1 = ("pale", "bale")  # change a letter
        ex2 = ("pale", "pal")  # remove a letter
        ex3 = ("bear", "beer")  # Change a letter
        ex4 = ("pale", "bake")  # False
        ex4 = ("ple", "pale")  # add a letter

        self.assertTrue(obj.run(ex1))
        self.assertTrue(obj.run(ex2))
        self.assertTrue(obj.run(ex3))
        self.assertFalse(obj.run(ex4))



if __name__ == "__main__":
    unittest.main()