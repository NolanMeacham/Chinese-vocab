"""
Tests the functionality of vocab quiz using Chinese Characters

"""

def main():
    from numpy import loadtxt
    # vocab = loadtxt(f'python_vocab/vocab_quiz/vocab_files/lesson5_vocab_characters.txt', dtype=str, delimiter=',')
    vocab = loadtxt('/Users/nolan/Documents/BYUI/BYUI/2021-1-Winter/CHINA101-Mandarin/python_vocab/vocab_quiz/vocab_files/lesson5_vocab_characters.txt', dtype=str, delimiter=',')

    # print(vocab)
    chars = vocab[:,0]
    pinyins = vocab[:,1]
    definitions = vocab[:,2]

    # run the quiz
    for index, word in enumerate(chars):
        user_input = input(f'{index+1}. {word}: ')
        if user_input.lower() == pinyins[index].lower():
            print('correct!')
            print()
        else:
            print(f'Incorrect. {word} means {pinyins[index].lower()}')
            print()





if __name__ == "__main__":
    main()