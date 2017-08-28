import re


class StringCalculatorInputParser(object):
    def __init__(self):  # pragma: no coverage
        pass

    @staticmethod
    def parse_delimiters(delims):
        """
        Parses delimiters list. Able to parse delimiters list for
        "[ABC][DEF][QPP]" -> ["ABC", "DEF", "QPP"]
        :param delims: string with delimiters
        :return: delimiters array
        """
        d = re.findall("\[(.*?)\]", delims)
        if len(d) == 0:
            return [delims]

        return d

    @staticmethod
    def get_tasks(commands):
        """
        Returns tasks and delimiters from input

        :param commands: string with delimiters and takss
        :return: tupple of delimiters, tasks
        """
        default_delimiters = ["\n", ","]

        index = commands.find("//")
        if index != 0:
            return default_delimiters, commands

        delimiters_query = None
        index = commands.find("\n")
        if index != -1:
            delimiters_query = commands[2:index]
            commands = commands[index + 1:]

        if delimiters_query is not None:
            delimiters_query = StringCalculatorInputParser.parse_delimiters(delimiters_query)

        if delimiters_query is None:
            delimiters_query = default_delimiters

        return delimiters_query, commands

    @staticmethod
    def parse_input(commands):
        """
        Parses input and yields values to process
        :param commands: string with delimiters and tasks
        :return: yields values for processing
        """
        possible_separators, data = StringCalculatorInputParser.get_tasks(commands)
        items = [data]

        for separator in possible_separators:
            iteration_items = []

            for item in items:
                iteration_items.extend([str(x).strip() for x in item.split(separator) if len(str(x)) > 0])

            items = iteration_items

        for item in items:
            yield item


class StringCalculator:
    def __init__(self):  # pragma: no coverage
        pass

    @staticmethod
    def add(commands):
        """
        Calculates sum of tasks with delimiters according to rules
        :param commands: string with delimiters and tasks
        :return: result sum
        """
        res = 0

        wrong_numbers = []

        for v in StringCalculatorInputParser.parse_input(commands):
            v = str(v).strip()
            if not len(v):
                continue

            v = int(v)
            if v < 0:
                wrong_numbers.append(v)
                continue

            if v > 1000:
                continue

            res += int(v)

        if wrong_numbers:
            e = Exception("negatives not allowed")
            e.wrong_data = wrong_numbers
            raise e

        return res
