"""
Program:
    Generalized Vocab Quiz
Author:
    Nolan Meacham
Date:
    25 Jan 2021
Details:
    Defines a class that is designed to accept a text file of vocab words with
    definitions and then administers a quiz to the user.

    The text file should have the vocab words in the first column and all the
    definitions in the second column, separated by commas
    Example: vocab word 1, definition 1
             vocab word 2, definition 2

    If the user types the correct answer, 'correct' will be displayed.
    If the user types an incorrect answer, 'incorrect' will display along with
    the actual definition.

    Tracks the score for the quiz
"""


class Vocab_quiz():
    def __init__(self, vocab_file):
        self.vocab_words = vocab_file[:, 0]
        self.vocab_answers = vocab_file[:, 1]
        self.score = 0
        self.total = len(self.vocab_words)

    def prompt_user(self, index, word):
        user_input = input(f'{index+1}. {word}: ')
        return user_input

    def get_result(self, index, user_input):
        if user_input.lower() == self.vocab_answers[index].lower():
            self.display_correct()
            self.score += 1
        else:
            self.display_incorrect(index)

    def display_correct(self):
        print('correct!')
        print()

    def display_incorrect(self, index):
        print(
            f'incorrect. {self.vocab_words[index]} means {self.vocab_answers[index]}')
        print()

    def dislay_score(self):
        print(f'Score: {self.score} out of {self.total}')

    def start_quiz(self):
        """
        This function begins the quiz, calling each necessary function
        to administer the entire quiz.
        """
        print('Welcome to the vocab quiz. Good luck!')
        print('Enter the definition for each of the following words:')
        print()

        # iterate through the list of vocab words
        for index, word in enumerate(self.vocab_words):
            user_input = self.prompt_user(index, word)
            self.get_result(index, user_input)

        self.dislay_score()
