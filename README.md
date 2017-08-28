# tdd-kata
TDD Kata solution


## General information

This repository contains my solutions for TDD-Katas.

Before you will be able to execute these tests you should install:

1. install python 3.4.x, if not yet installed (https://www.python.org/downloads/);
2. have latest possible pip installed. It's required to manage project external dependencies;
3. have latest possible `virtualenv` installed (`pip install virtualenv`). It's required to create virtual environment;
4. have latest possible `make` installed (http://gnuwin32.sourceforge.net/packages/make.htm). It's required to build the project and run its corresponding commands.

To install virtual environment and all dependancies you just need to execute `make`.

When everything is installed, you need just execute `make tests` to run all available tests.

## Kata-1 (String Calculator)

Original article can be found [here](http://osherove.com/tdd-kata-1/]). Below you can find detailed description.

### Before you start

* Try not to read ahead.
* Do one task at a time. The trick is to learn to work incrementally.
* Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata

### String Calculator

Original article can be found here: http://osherove.com/tdd-kata-1/

1. Create a simple String calculator with a method int Add(string numbers)
	* The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example `""` or ``"1"`` or ``"1,2"``
	* Start with the simplest test case of an empty string and move to 1 and two numbers
	* Remember to solve things as simply as possible so that you force yourself to write 	tests you did not think about
	* Remember to refactor after each passing test
2. Allow the Add method to handle an unknown amount of numbers
3. Allow the Add method to handle new lines between numbers (instead of commas).
	* the following input is ok:  ``"1\n2,3"``  (will equal 6)
	* the following input is NOT ok:  ``"1,\n"`` (not need to prove it - just clarifying)
4. Support different delimiters
	* to change a delimiter, the beginning of the string will contain a separate line that looks like this:   ``"//[delimiter]\n[numbers…]"`` for example ``"//;\n1;2"`` should return three where the default delimiter is ``";"`` .
	* the first line is optional. all existing scenarios should still be supported
5. Calling Add with a negative number will throw an exception "negatives not allowed" - and the negative that was passed.if there are multiple negatives, show all of them in the exception message
	** stop here if you are a beginner. Continue if you can finish the steps so far in less than 30 minutes.**
6. Numbers bigger than 1000 should be ignored, so adding 2 + 1001  = 2
7. Delimiters can be of any length with the following format:  ``"//[delimiter]\n"`` for example: ``"//[***]\n1***2***3"`` should return 6
8. Allow multiple delimiters like this:  ``"//[delim1][delim2]\n"`` for example ``"//[*][%]\n1*2%3"`` should return 6.
9. make sure you can also handle multiple delimiters with length longer than one char

Solution can be found in file ``./work_classes/string_calculator.py``

## Kata-2 Recently Used List

Develop a recently-used-list class to hold strings uniquely in Last-In-First-Out order.

* The most recently added item is first, the least recently added item is last.
* Items can be looked up by index, which counts from zero.
* Items in the list are unique, so duplicate insertions are moved rather than added.
* A recently-used-list is initially empty.

Optional extras:

* Null insertions (empty strings) are not allowed.
* A bounded capacity can be specified, so there is an upper limit to the number of items contained, with the least recently added items dropped on overflow.


More tests:

* While getting items by index, supplied index-value should be within the bounds of List [eg. if maximum item counts of list is 5 then supplied index is less than 4 as index starts from 0 (zero)]
* Negative index value not allowed [>0]
* Size limit is must if not supplied make 5 as default [0-4]
* List can be non-sizable means without upper limit list can be created [Hint-try property or constructor initializers]


## Kata-3 The FizzBuzz Kata

Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


## Kata-4 The OddEven Kata

Write a program that prints numbers within specified range lets say 1 to 100. If number is odd print 'Odd' instead of the number. If number is even print 'Even' instead of number. Else print number [hint - if number is Prime].

## Kata-5 The PrimeComposite Kata

Write a program that prints numbers within specified range lets say 1 to 100. 
If number is ```prime``` print 'prime' instead of the number. 

If number is ```composite``` but not ```even``` print 'composite' instead of number.

Else print number. 

Reference(s):

* [Prime numbers](https://en.wikipedia.org/wiki/Prime_number)
* [Composite numbers](https://en.wikipedia.org/wiki/Composite_number),
* [odd even](https://en.wikipedia.org/wiki/Parity_(mathematics)
