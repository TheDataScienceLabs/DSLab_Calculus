"""
Check students' work on lab 6.
"""

from sympy import chebyshevt
from sympy.abc import x


def exercise_3(mod):
    if mod.__name__ == "my_module":
        print("The name of your module is correct.")
    else:
        print(
            f"It looks like you used the name {mod.__name__}, which is not what was requested."
        )

    if (
        mod.__doc__
        == "Create a module object.\n\nThe name must be a string; the optional doc argument can have any type."
    ):
        print("It looks like you didn't give a docstring!")
    else:
        print("Here is the docstring you gave:")
        print(mod.__doc__)

    if "INCH" in dir(mod):
        if mod.INCH == 2.54:
            print("The constant INCH looks good")
        else:
            print(f"Your constant INCH is {mod.INCH}, but we were expecting 2.54")
    else:
        print("It looks like you didn't define the constant INCH.")

    if "chebyshev_five" in dir(mod):
        expected = chebyshevt(5, x)
        got = mod.chebyshev_five(x)
        if expected == got:
            print("Your function chebyshev_five looks good to me")
        else:
            print(
                f"There might be a problem with your function chebyshev_five. I expected to get {expected}, but I got {got}."
            )
    else:
        print("It looks like you didn't define the function chebyshev_five")


def exercise_7(Monomial):
    # need to check the derivative function, and the prints.
    pass
