'''
A snipet to check if the number 237 is
divisible by 3 or 7.
'''
print("Yes it is divisible by 3 becaus ethe remainder is =",237 % 3,".")
print("Not divisible by 7 because the remainder is =",237 % 7,".")

import unittest

class TestDivisibility(unittest.TestCase):

    def test_divisibility(self):
        number = 237
        remainder_3 = number % 3
        remainder_7 = number % 7

        self.assertEqual(remainder_3, 0, "237 should be divisible by 3")
        self.assertNotEqual(remainder_7, 0, "237 should not be divisible by 7")

if __name__ == '__main__':
    unittest.main()
