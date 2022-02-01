"""
These will help studetns check their work as they go, to make sure that their functions do what they should.
"""

from autograder import FunctionGrader, FunctionTestCase
import math
import itertools
import numpy as np

def allclose(x, y):
    return all(math.isclose(i, j) for i, j in itertools.zip_longest(x, y))


naive_cases  = [
    FunctionTestCase('integer square', kwargs = {'a': 1, 'b':2, 'c':1}, retval = [-1, -1], checker = allclose),
    FunctionTestCase('roots are two three', kwargs = {'a': 1, 'b':-5, 'c':6}, retval = [2, 3], checker = allclose),
    FunctionTestCase('no b', kwargs = {'a':1, 'b':0, 'c':-49}, retval = [-7, 7], checker = allclose),
    FunctionTestCase('golden ratio', kwargs = {'a':1, 'b':-1, 'c':-1}, retval = [(1-math.sqrt(5))/2, (1+math.sqrt(5))/2], checker=allclose),
    FunctionTestCase('negative a', kwargs = {'a':-35, 'b':-2, 'c':1}, retval = [-1/5, 1/7], checker = allclose)
]

check_naive_roots = FunctionGrader(*naive_cases)

check_roots = FunctionGrader(*naive_cases, 
    FunctionTestCase('catestrophic cancellation', kwargs = {'a':1, 'b':-1e6-1e-6, 'c':1}, retval = [1e-6, 1e6], checker = allclose),
    FunctionTestCase('positive b cancellation', kwargs = {'a':-1, 'b':1e6+1e-6, 'c':-1}, retval = [1e-6, 1e6], checker = allclose),
    FunctionTestCase('c is zero', kwargs = {'a':-2, 'b':4, 'c':0}, retval = [0, 2], checker = allclose)
)

def check_finite_difference(approximation, relative_error):
    h = np.geomspace(1e-15, 1, 200)
    d = ((4+h)**2-4**2)/h
    if not np.allclose(approximation, d):
        print('You got a different answer for the approximation. Here is what I expected:')
        print(d)
    else:
        print('I agree with your answer for the approximation.')
    e = (d-8) / 8
    if not np.allclose(relative_error, e):
        print('You got a different answer for the relative error. Here is what I expected:')
        print(e)
    else:
        print('I agree with your answer for the relative error.')
        
check_symmetric_difference = FunctionGrader(
    FunctionTestCase('worked example', kwargs = {'x': np.array([1.0, 2, 5, 7, 8]), 'y':np.array([50.0, 49, 42, 35, 34])}, retval = np.array([-1 ,-4/3,-10/3+3/10,-4/3-1/2, -1]), checker=np.allclose),
    FunctionTestCase('constant function', kwargs = {'x': np.array([1, 6, 10]), 'y':np.array([10, 10, 10])}, retval = np.array([0, 0, 0]), checker=np.allclose),
    FunctionTestCase('linear', kwargs={'x': np.array([0, 1, 4, 9]), 'y':np.array([0, 1, 4, 9])}, retval=np.array([1, 1, 1, 1]), checker=np.allclose),
    FunctionTestCase('up and down', kwargs={'x':np.array([0, 1, 2, 3, 4]), 'y':np.array([0, 1, 0, -1, 0])}, retval=np.array([1, 0, -1, 0, 1]), checker=np.allclose)
)