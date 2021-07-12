import numpy as np

###############################################################
# Exercise 1.1: trapezoid_area checker

def ex1_check1(func):
    check = [1, 2, 3]
    base1 = [1, 5, 8]
    base2 = [2, 8, 4]
    height = [3, 9, 6]
    exp = [4.5, 58.5, 36]
    
    for i in range(0, len(check)):
        ans = func(base1[i], base2[i], height[i])
        check_trapezoid_answer(check[i], exp[i], ans, base1[i], base2[i], height[i])
        
def check_trapezoid_answer(check, exp, ans, base1, base2, height):
    if (exp == ans):
        print_pass(check)
    else:
        print_dash()
        print_fail(check)
        print("base1 = {}".format(base1))
        print("base2 = {}".format(base2))
        print("base3 = {}".format(height))
        print("Expected: {}".format(exp))
        print("Received: {}".format(ans))
        print_dash()
        
#################################################################   

###############################################################
# Exercise 1.2 : slope checker

def ex1_check2(func):
    check = [1, 2, 3]
    x1 = [1, 5, 8]
    x2 = [2, 8, 4]
    y1 = [3, 9, 6]
    y2 = [7, 2, 3]
    exp = [4, -7/3, 0.75]
    
    for i in range(0, len(check)):
        ans = func(x1[i], y1[i], x2[i], y2[i])
        check_slope_answer(check[i], exp[i], ans, x1[i], y1[i], x2[i], y2[i])
        
def check_slope_answer(check, exp, ans, x1, y1, x2, y2):
    if (exp == ans):
        print_pass(check)
    else:
        print_dash()
        print_fail(check)
        print("x1 = {}".format(x1))
        print("y1 = {}".format(y1))
        print("x2 = {}".format(x2))
        print("y2 = {}".format(y2))
        print("Expected: {}".format(exp))
        print("Received: {}".format(ans))
        print_dash()
        
#################################################################  

###############################################################
# Exercise 2.1 : mean checker

def ex2_check1(func):
    x = [np.random.randint(1,26,5), np.random.randint(1,15,26), np.random.randint(1,48,63), np.random.randint(1, 100, 74)]
    
    for i in range(0, len(x)):
        ans = func(x[i])
        exp = np.average(x[i])
        check_answer(i + 1, exp, ans, x[i])
        
def check_answer(check, exp, ans, x):
    if (exp == ans):
        print_pass(check)
    else:
        print_dash()
        print_fail(check)
        print("x = {}".format(x))
        print("Expected: {}".format(exp))
        print("Received: {}".format(ans))
        print_dash()
        
#################################################################  

#################################################################  

###############################################################
# Exercise 2.2 : std checker

def ex2_check2(func):
    x = [np.random.randint(1,26,5), np.random.randint(1,15,26), np.random.randint(1,48,63), np.random.randint(1, 100, 74)]
    
    for i in range(0, len(x)):
        ans = func(x[i])
        exp = np.std(x[i], ddof=1)
        check_answer(i + 1, exp, ans, x[i])
        
#################################################################  
        
def print_dash():
    print("------------------------------")
    
def print_pass(check):
    print("Check {} PASSED".format(check))
    
def print_fail(check):
    print("Check {} FAILED".format(check))
    