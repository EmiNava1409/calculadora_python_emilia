import unittest
import main

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(main.sumar(3, 5), 8)
        self.assertEqual(main.sumar(-1, 1), 0)
        self.assertEqual(main.sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(main.restar(5, 3), 2)
        self.assertEqual(main.restar(-1, 1), -2)
        self.assertEqual(main.restar(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(main.multiplicar(3, 5), 15)
        self.assertEqual(main.multiplicar(-1, 1), -1)
        self.assertEqual(main.multiplicar(0, 0), 0)

    def test_dividir(self):
        self.assertEqual(main.dividir(10, 2), 5)
        self.assertEqual(main.dividir(5, 2), 2.5)
        self.assertEqual(main.dividir(8, 4), 2)
        self.assertEqual(main.dividir(5, 0), "Error: No se puede dividir por cero")

if __name__ == "__main__":
    unittest.main()
