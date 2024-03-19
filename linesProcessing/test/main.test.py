import unittest
import path
import sys
dire = path.Path(__file__).abspath()
sys.path.append(dire.parent.parent)
from lineProcess import LinesProcess as lines
import unittest
a=lines(400)
class TestStringMethods(unittest.TestCase):

    def test_calcul(self):
        self.assertEqual(a.calcul({"right":[250,20,326,750],"left":[750,500,550,100]}),[0, 0.0])
    def test_linePosition(self):
        self.assertEqual(a.linePosition([0.23,0.52]),1)
        self.assertEqual(a.linePosition([0.0,0.13]),0)
        self.assertEqual(a.linePosition([0.82,0]),-2)
        self.assertEqual(a.linePosition([0.36,0.67]),1)
    def test_output(self):
        self.assertEqual(a.output({"right":[250,20,326,750],"left":[750,600,550,70]}),0)


if __name__ == '__main__':
    unittest.main()