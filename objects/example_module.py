"Welcome to the example module! This string doesn't do anything, but it's traditional to start a module with a description of what it is."


print("You have loaded the example module! Here is the value in the variable __name__:")
print(__name__)

import numpy as my_favorite_module
from types import SimpleNamespace

x = my_favorite_module.arange(4)
numbers = SimpleNamespace(best=0, second_best=1, third_best=(x**x).prod())


def share_favorites():
    print(
        "My favorite numbers are {}, {}, and {}.".format(
            numbers.best, numbers.second_best, numbers.third_best
        )
    )


if __name__ == "__main__":
    print(
        "This is being run as its own program, not as a module inside a larger program."
    )
    share_favorites()
