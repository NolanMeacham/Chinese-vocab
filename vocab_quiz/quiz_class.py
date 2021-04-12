"""
Program:
    Generalized Vocab Quiz Class
Author:
    Nolan Meacham
Date:
    25 Jan 2021
    Updated: 12 April 2021
Details:
    Defines a class that is designed to accept a text file of vocab words with
    definitions and then administers a quiz to the user.

    The text file should have the vocab words in the first column and all the
    definitions in the second column, and the chinese character in the third column,
    separated by commas.
    Example: vocab word 1, definition 1, chinese character 1
             vocab word 2, definition 2, chinese character 2

    If the user types the correct answer, 'correct' will be displayed.
    If the user types an incorrect answer, 'incorrect' will display along with
    the actual definition.

    Tracks the score for the quiz
"""


class Vocab_quiz():
    def __init__(self, vocab_file):
        """
        Class constructor.

        Args:
            self (Vocab_quiz): an instance of Vocab_quiz
            vocab_file: a list that contains the lines of the vocab file.
                        the first index of each line is the word in pinyin 
                        the second index is the definition in English
                        the third index is the Chinese simplified character
        """
        self.vocab_words = vocab_file[:,0]
        self.vocab_answers = vocab_file[:,1]
        self.vocab_char = vocab_file[:,2]
        self.score = 0
        self.total = len(self.vocab_words)

    def prompt_user(self, index, word):
        """
        Prompts the user for their answer.

        Args:
            self (Vocab_quiz): an instance of Vocab_quiz
            index (int): the index number of the word being tested
            word (str): the word being tested
        """
        user_input = input(f'{index+1}. {self.vocab_char[index]}/{word}: ')
        return user_input

    def get_result(self, index, user_input):
        """
        Determines if the user's input is correct and calls the appropriate display method.

        Args:
            self (Vocab_quiz): an instance of Vocab_quiz
            index (int): the index number of the word being tested
            user_input (str): the word entered by the user
        """
        if user_input.lower() == self.vocab_answers[index].lower():
            self.display_correct()
            self.score += 1
        else:
            self.display_incorrect(index)

    def display_correct(self):
        """
        Displays the word 'correct' on the screen to let the user know that their
        input was correct.

        Args:
            self (Vocab_quiz): an instance of Vocab_quiz
        """
        print('correct!')
        print()

    def display_incorrect(self, index):
        """
        Displays 'incorrect' and then the correct definition for the word.

        Args:
            self (Vocab_quiz): an instance of Vocab_quiz
            index (int): the index number of the word being tested
        """
        print(
            f'   incorrect.\n {self.vocab_char[index]} ({self.vocab_words[index]}) means {self.vocab_answers[index]}')
        print()

    def dislay_score(self):
        """
        Displays the user's score out of the total number available.

        Args:
            self (Vocab_quiz): an instance of Vocab_quiz
        """
        print(f'Score: {self.score} out of {self.total}')

    def start_quiz(self):
        """
        This function begins the quiz, calling each necessary function
        to administer the entire quiz.

        Args:
            self (Vocab_quiz): an instance of Vocab_quiz
        """
        print('Welcome to the vocab quiz. Good luck!')
        print('Enter the definition for each of the following words:')
        print()

        # iterate through the list of vocab words
        for index, word in enumerate(self.vocab_words):
            user_input = self.prompt_user(index, word)
            self.get_result(index, user_input)

        self.dislay_score()
