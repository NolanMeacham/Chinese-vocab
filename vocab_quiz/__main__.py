"""
Program:
    Main program to run the Chinese vocab quiz
Author:
    Nolan Meacham
Date:
    25 Jan 2021
    Updated: 12 April 2021

Details:
    Runs a vocab quiz using the file that contains the vocab information.
    The file is determined by the user input for which lesson they want to be quizzed on.
    Uses the vocab_quiz class to administer the quiz.
"""


def main():
    from quiz_class import Vocab_quiz
    from numpy import loadtxt

    # file = input('Enter the filename for the vocab quiz: ')
    lesson = input('Enter the lesson number you want to quiz: >>> ')
    print()

    vocab = loadtxt(f'vocab_quiz/vocab_files/lesson{lesson}_vocab.txt', dtype=str, delimiter=',')
    quiz1 = Vocab_quiz(vocab)

    # can this be done without numpy? 
    # using the with open() method?

    # start the quiz
    quiz1.start_quiz()


if __name__ == "__main__":
    main()