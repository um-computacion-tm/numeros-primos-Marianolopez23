import unittest

from numeros_primos import is_prime

class TestIsPrime (unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertEqual(result,True)
 
    def test_with_2(self):
        result = is_prime(2)
        self.assertEqual(result,True)      
        
    def test_with_3(self):
        result = is_prime(3)
        self.assertEqual(result,True)     
        
    def test_with_4(self):
        result = is_prime(4)
        self.assertEqual(result,False)  

    def test_with_5(self):
        result = is_prime(5)
        self.assertEqual(result,True) 

    def test_with_6(self):
        result = is_prime(6)
        self.assertEqual(result,False) 
    
    def test_with_111(self):
        result = is_prime(111)
        self.assertEqual(result,False)
        
    def test_with_11(self):
        result = is_prime(11)
        self.assertEqual(result,True)
        
    def test_with_1212(self):
        result = is_prime(1212)
        self.assertEqual(result,False)

    def test_with_121(self):
        result = is_prime(121)
        self.assertEqual(result,False)
        
    def test_with_121121(self):
        result = is_prime(121121)
        self.assertEqual(result,False)
if __name__ == '__main__':
    unittest.main()