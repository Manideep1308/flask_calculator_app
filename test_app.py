import unittest

class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertEqual(4 + 5,9)
   def test2(self):
      self.assertEqual(5 - 2,3)
   def test3(self):
      self.assertEqual(5 * 2,10)      
   def test4(self):
      self.assertEqual(10 / 5,2)
   def test5(self):
      self.assertNotEqual(4 + 5,10)
   def test6(self):
      self.assertNotEqual(5 - 2,4)
   def test7(self):
      self.assertNotEqual(5 * 2,8)
   def test8(self):
      self.assertNotEqual(10 / 5,3)
   def test9(self):
      self.assertEqual(10 % 5,0)
   def test10(self):
      self.assertNotEqual(10 % 5,1)      
                      