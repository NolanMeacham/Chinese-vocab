"""

Details:
   Runs a vocab quiz using the filename that the user enters
"""


def main():
    from quiz_class import Vocab_quiz
    from numpy import loadtxt

    file = input('Enter the filename for the vocab quiz: ')
    print()
    vocab = loadtxt(file, dtype=str, delimiter=',')
    quiz1 = Vocab_quiz(vocab)

    # start the quiz
    quiz1.start_quiz()


if __name__ == "__main__":
    main()
