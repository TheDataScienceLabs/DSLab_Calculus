from autograder import FunctionGrader, FunctionTestCase
import numpy as np

check_trapezoid_area = FunctionGrader(
    FunctionTestCase(
        name="Simple Evaluation", kwargs={"base1": 1, "base2": 2, "height": 3}, retval=4.5
    ),
    FunctionTestCase(
        name="Simple Evaluation", kwargs={"base1": 5, "base2": 8, "height": 9}, retval=58.5
    ),
    FunctionTestCase(
        name="Simple Evaluation", kwargs={"base1": 8, "base2": 4, "height": 6}, retval=36
    ),
)

check_slope = FunctionGrader(
    FunctionTestCase(
        name="Simple Evaluation", kwargs={"x1": 1, "x2": 2, "y1": 3, "y2": 7}, retval=4
    ),
    FunctionTestCase(
        name="Simple Evaluation", kwargs={"x1": 5, "x2": 8, "y1": 9, "y2": 2}, retval=-7/3
    ),
    FunctionTestCase(
        name="Simple Evaluation", kwargs={"x1": 8, "x2": 4, "y1": 6, "y2": 3}, retval=0.75
    ),
)

x1 = np.random.randint(1,26,5) 
x2 = np.random.randint(1,15,26)
x3 = np.random.randint(1,48,63)
x4 = np.random.randint(1, 100, 74)

check_mean = FunctionGrader(
    FunctionTestCase(
        name="Simple Evaluation", args=[x1], retval=np.average(x1)
    ),
    FunctionTestCase(
        name="Simple Evaluation", args=[x2], retval=np.average(x2)
    ),
    FunctionTestCase(
        name="Simple Evaluation", args=[x3], retval=np.average(x3)
    ),
    FunctionTestCase(
        name="Simple Evaluation", args=[x4], retval=np.average(x4)
    ),
)

check_std = FunctionGrader(
    FunctionTestCase(
        name="Simple Evaluation", args=[x1], retval=np.std(x1, ddof=1)
    ),
    FunctionTestCase(
        name="Simple Evaluation", args=[x2], retval=np.std(x2, ddof=1)
    ),
    FunctionTestCase(
        name="Simple Evaluation", args=[x3], retval=np.std(x3, ddof=1)
    ),
    FunctionTestCase(
        name="Simple Evaluation", args=[x4], retval=np.std(x4, ddof=1)
    ),
)
