"""

Details:
   Runs a vocab quiz using the filename that the user enters
"""


def main():
    from quiz_class import Vocab_quiz
    from numpy import loadtxt

    # file = input('Enter the filename for the vocab quiz: ')
    lesson = input('Enter the lesson number you want to quiz: >>> ')
    print()
    # vocab = loadtxt(f'vocab_files/{file}', dtype=str, delimiter=',')
    vocab = loadtxt(f'vocab_files/lesson{lesson}_vocab.txt', dtype=str, delimiter=',')
    quiz1 = Vocab_quiz(vocab)

    # start the quiz
    quiz1.start_quiz()


if __name__ == "__main__":
    main()
