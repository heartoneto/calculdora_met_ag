import unittest
import random;

from main import Calc


class CalcSumTest(unittest.TestCase):
    def test_add(self):
        """
        Test that it can sum a list of integers
        """
        calc = Calc();
        calc.crear_botones();
        
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        calc.press(a)
        calc.press('+')
        calc.press(b)
        calc.equalpress()

        self.assertEqual(str(a + b), calc.equation.get())

class CalcSubTest(unittest.TestCase):
    def test_sub(self):
        calc = Calc();
        calc.crear_botones();
        
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        calc.press(a)
        calc.press('-')
        calc.press(b)
        calc.equalpress()

        self.assertEqual(str(a - b), calc.equation.get())

class CalcMulTest(unittest.TestCase):
    def test_mul(self):
        calc = Calc();
        calc.crear_botones();
        
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        calc.press(a)
        calc.press('*')
        calc.press(b)
        calc.equalpress()

        self.assertEqual(str(a * b), calc.equation.get())

class CalcDivTest(unittest.TestCase):
    def test_div(self):
        calc = Calc();
        calc.crear_botones();
        
        a = random.randint(0, 9)
        b = random.randint(1, 9)
        calc.press(a)
        calc.press('/')
        calc.press(b)
        calc.equalpress()

        self.assertEqual(str(a / b), calc.equation.get())

if __name__ == '__main__':
    unittest.main()
