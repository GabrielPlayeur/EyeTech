import unittest
import path
import sys
dire = path.Path(__file__).abspath()
sys.path.append(dire.parent.parent)
from main import calcul
from main import output
import unittest

class TestStringMethods(unittest.TestCase):

    def test_calcul(self):
        self.assertEqual(calcul({"droite":[430,800,500,750],"gauche":[750,600,930,70]},540),[0, 0.81])
    def test_output(self):
        self.assertEqual(output({"droite":[430,800,500,750],"gauche":[750,600,930,70]},540),2)


if __name__ == '__main__':
    unittest.main()