"""
Program:
    Lesson 2 Vocab Quiz
Author:
    Nolan Meacham
Date:
    25 Jan 2021
Details:
    Loads the lesson 2 vocab text file and uses the vocab quiz class
    to administer the lesson 2 vocab quiz.
"""


def main():
    from vocab_quiz import Vocab_quiz
    from numpy import loadtxt
    vocab = loadtxt('lesson2_vocab.txt', dtype=str, delimiter=',')
    quiz1 = Vocab_quiz(vocab)

    # start the quiz
    quiz1.start_quiz()


if __name__ == "__main__":
    main()
