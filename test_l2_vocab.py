"""
Chinese tones quiz for Lesson 2 vocab (1-7)
"""

# Define the vocab words and meanings/answers
vocab1to7 = ['nín', 'guì', 'xìng', 'qǐng wèn', 'de', 'Yīngwén', 'míngzi']
vocab8to13 = ['Zhōngwén', 'jiào', 'shénme', 'tā', 'shéi/shuí', 'tóngxué, tóng']

answer1to7 = ['you (polite)', 'honorable/expensive', 'surname',
              'may i ask', 'possession', 'english', 'name']
answer8to13 = ['chinese', 'called', 'what', 'she/her', 'who', 'classmate/same']

print('What do the following words mean:')
print()

# enumerate through the lists and prompt for each word
# check to see if the input matches the answer key
# display correct or incorrect message

for vocab words 1 through 7
for index, word in enumerate(vocab1to7):
    check = input(f'{index+1}. {word}: ')
    if check.lower() == answer1to7[index]:
        print('correct!')
    else:
        print(f'incorrect. {word} means {answer1to7[index]}')
    print()

# for vocab words 8 through 13
for index, word in enumerate(vocab8to13):
    check = input(f'{index+8}. {word}: ')
    if check.lower() == answer8to13[index]:
        print('correct!')
    else:
        print(f'incorrect. {word} means {answer8to13[index]}')
    print()

# L2 Vocab 1 through 7
# one = input('1. nín: ')
# print('   nín: you')
# print()
#
# two = input('2. guì: ')
# print('   guì: honorable, expensive')
# print()
#
# three = input('3. xìng: ')
# print('   xìng: (N) Surname')
# print('   xìng: (V) to have as a surname')
# print()
#
# four = input('4. qǐng wèn: ')
# print('   qǐng wèn: may I ask')
# print('   qǐng: please')
# print('   wèn: to ask')
# print()
#
# five = input('5. de: ')
# print('   de: used to show possession')
# print()
#
# six = input('6. Yīngwén: ')
# print('   Yīngwén: English')
# print()
#
# seven = input('7. míngzi: ')
# print('   míngzi: name')
# print()
