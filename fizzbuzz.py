import unittest

def fizzbuzz(number):
    return {
        number % 3 ==0 : 'Fizz', 
        number % 5 == 0: 'Buzz'
    }[True]

## unit test in python
class TestFizzBuzz(unittest.TestCase):
    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        assert result == 'Fizz'

    def test_input_6_should_get_fizz(self):
        result = fizzbuzz(6)
        assert result == 'Fizz'

    def test_input_5_should_get_buzz(self):
        result = fizzbuzz(5)
        assert result == 'Buzz'

if __name__ == '__main__':
    unittest.main()