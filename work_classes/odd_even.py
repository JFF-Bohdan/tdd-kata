class OddEvenGame(object):
    def __init__(self):  # pragma: no coverage
        pass

    @staticmethod
    def play(number):
        if number <= 0 or number > 100:
            raise Exception("Wrong value")

        if number % 2 == 0:
            return "even"

        if number % number == 0:
            return "odd"

        return str(number)

    @staticmethod
    def game():
        res = []
        for i in range(1, 101):
            res.append(OddEvenGame.play(i))

        return res
