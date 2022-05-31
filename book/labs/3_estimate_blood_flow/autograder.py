import itertools


class FunctionGrader:
    """
    Students will import premade instances of this class to check their code.
    """

    def __init__(self, *test_cases):
        self.test_cases = list(test_cases)

    def __call__(self, func):
        outcomes = [case(func) for case in self.test_cases]
        success_count = sum(o.success for o in outcomes)
        if success_count == len(outcomes):
            print(f"all {len(outcomes)} tests passed successfully. Good job!")
            return
        print(
            f"passed only {success_count} of {len(outcomes)} tests. Here is a detailed summary:"
        )
        for outcome in outcomes:
            print(outcome.summary())
        print("Please make sure your function passes all tests before you continue.")


class FunctionTestCase:
    """
    This class should be instantiated with a descriptive name,
    so that it can be referred to appropriately.
    """

    def __init__(self, name, args=None, kwargs=None, retval=None):
        self.name = name
        self.args = [] if args is None else args
        self.kwargs = {} if kwargs is None else kwargs
        self.retval = retval

    def __call__(self, func):
        return FunctionTestOutcome(self, func)


class FunctionTestOutcome:
    """
    This is created only by FunctionTestCase instances.
    This runs the test case upon instantiation and provides introspection tools.
    """

    def __init__(self, test_case, function):
        self.test_case = test_case
        self.function = function
        try:
            self.returned = function(*test_case.args, **test_case.kwargs)
            self.error = None
        except Exception as e:
            self.returned = None
            self.error = e
        self.success = (self.error is None) and (self.returned == test_case.retval)

    def test_signature(self):
        """
        What would it look like if you called the function on this test case in the REPL?
        """
        return (
            self.function.__name__
            + "("
            + ", ".join(
                itertools.chain(
                    (repr(arg) for arg in self.test_case.args),
                    (
                        f"{key} = {repr(val)}"
                        for key, val in self.test_case.kwargs.items()
                    ),
                )
            )
            + ")"
        )

    def summary(self):
        funcname = self.function.__name__
        testname = self.test_case.name
        if self.success:
            return f"function {funcname} passed test case {testname}."
        message = f"function {funcname} failed test case {testname}:\n\tCalled as {self.test_signature()}"
        if self.error is not None:
            return message + "\n\tProduced the folowing error:\t" + repr(self.error)
        return (
            message
            + f"\n\tExpected the return value {repr(self.test_case.retval)}, but got {repr(self.returned)}."
        )
