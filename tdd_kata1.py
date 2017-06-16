import re
import unittest


class StringCalculator:
    def __init__(self):
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
            delimiters_query = StringCalculator.parse_delimiters(delimiters_query)

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
        possible_separators, data = StringCalculator.get_tasks(commands)
        items = [data]

        for separator in possible_separators:
            iteration_items = []

            for item in items:
                iteration_items.extend([str(x).strip() for x in item.split(separator) if len(str(x)) > 0])

            items = iteration_items

        for item in items:
            yield item

    @staticmethod
    def Add(commands):
        """
        Calculates sum of tasks with delimiters according to rules
        :param commands: string with delimiters and tasks
        :return: result sum
        """
        res = 0

        wrong_numbers = []

        for v in StringCalculator.parse_input(commands):
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


class TestStringCalculator(unittest.TestCase):
    def test_simple_tests(self):
        v = StringCalculator.Add("")
        self.assertEqual(v, 0)

        v = StringCalculator.Add("1")
        self.assertEqual(v, 1)

        v = StringCalculator.Add("1,2")
        self.assertEqual(v, 3)

    def test_unknown_amount_of_numbers(self):
        v = StringCalculator.Add("1,2, 3, 4   ")
        self.assertEqual(v, 10)

    def test_crlf_separator_support(self):
        v = StringCalculator.Add("1\n2, 3")
        self.assertEqual(v, 6)

    def test_support_different_delimiters(self):
        v = StringCalculator.Add("//;\n1;2")
        self.assertEqual(v, 3)

    def test_exceptions_for_negative_number(self):
        self.assertRaises(Exception, StringCalculator.Add, "//;\n1;2;-3")

        with self.assertRaises(Exception) as context:
            StringCalculator.Add("//;\n1;2;-3")

        msg = str(context.exception)
        wrong_values = context.exception.wrong_data

        self.assertTrue("negatives not allowed" in msg)
        self.assertTrue(-3 in wrong_values)

    def test_exception_for_negative_numbers_list(self):
        wrong_command = "//;\n1;2;-3;-4;-5"

        with self.assertRaises(Exception) as context:
            StringCalculator.Add(wrong_command)

        msg = str(context.exception)
        wrong_values = context.exception.wrong_data

        self.assertTrue("negatives not allowed" in msg)
        wrong_numbers = [-3, -4, -5]
        for value in wrong_numbers:
            self.assertTrue(value in wrong_values)

    def test_big_numbers_ignore(self):
        v = StringCalculator.Add("1,2, 3, 4, 1500, 2000, 1001   ")
        self.assertEqual(v, 10)

    def test_custom_delimiters(self):
        v = StringCalculator.Add("//[***]\n1***2***3")
        self.assertEqual(v, 6)

    def test_multiple_delimiters(self):
        v = StringCalculator.Add("//[*][%]\n1*2%3")
        self.assertEqual(v, 6)

    def test_multiple_long_delimiters(self):
        v = StringCalculator.Add("//[&&*][%%@]\n1&&*2%%@3")
        self.assertEqual(v, 6)


if __name__ == "__main__":
    unittest.main()
