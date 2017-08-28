class FizzBuzzImplementation(object):
    def __init__(self):  # pragma: no coverage
        pass

    @staticmethod
    def play(value):
        if value < 0 or value > 100:
            raise Exception("Unsupported value")

        res = None

        if value % 3 == 0:
            res = "fizz"

        if value % 5 == 0:
            res = res + "buzz" if res is not None else "buzz"

        return str(value) if res is None else res
