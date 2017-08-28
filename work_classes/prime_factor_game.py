class PrimeFactorGame(object):
    def __init__(self):  # pragma: no coverage
        pass

    @staticmethod
    def play(number):
        if number <= 0 or number > 100:
            raise Exception("Unsupported number")

        if PrimeFactorGame._is_prime(number):
            return "prime"

        if number % 2 == 1:
            return "composite"

        return str(number)

    @staticmethod
    def _is_prime(number):
        mx = (number // 2)
        for i in range(2, mx + 1):
            if number % i == 0:
                return False

        return True

    @staticmethod
    def game():
        res = []

        for i in range(1, 101):
            res.append(PrimeFactorGame.play(i))

        return res
