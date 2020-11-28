import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_func_exists(self) :
        self.assertTrue( "quadratic" in globals(), "No function called quadratic has been defined" )
    
    def test_func_return(self) :
        myarr = quadratic( 1, 1, 1 )
        self.assertTrue( len(myarr)==500, "The quadratic function should return an np.array of length 500" )
        
    def test_func_works(self) :
        for i in range(5) :
           a, b, c = np.random.randint(-10,10), np.random.randint(-10,10), np.random.randint(-10,10)
           quad = quadratic( a, b, c )
           for j in range(len(quad)) : 
               yv = a*xvalues[j]*xvalues[j] + b*xvalues[j] + c
               self.assertTrue( np.abs(yv-quad[j])<1e-7, "The quadratic function does not seem to calculate the quadratic correctly" )
