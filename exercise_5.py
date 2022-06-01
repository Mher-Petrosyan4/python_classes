#ex 1
num = int(input('Enter a number: '))
if num % 5 == 0 or num % 11 == 0:
    print(f'The number {num} is divisible by 5 or by 11')
else:
    print(f'The number {num} is not divisible by 5 or by 11')

#ex 2
num = int(input('Enter a number: '))
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0:
    print('Fizz')
else:
    print(num)

#ex 3
sentence = input('Enter some sentence: ')
if 'not' in sentence and 'poor' in sentence and sentence.index('not') < sentence.index('poor'):
    print(sentence.replace(sentence[sentence.index('not'):(sentence.index('poor') + 4)], 'good'))
else:
    print(sentence)

sentence = 'bla bla bla not bla poor bla not bla poor'
not_index = sentence.index('not')
poor_index = sentence.index('poor')

if not_index >= 0 and poor_index > not_index:
    sentence = sentence.replace(sentence[not_index: poor_index + 4], 'good')
print(sentence)
print(not_index)
print(poor_index)


#ex 4
word = input('Enter some word: ')
new_word = word[0] + word[1:].replace(word[0], '$')
print(new_word)





