# Says is the written word a palindrome or not
def palindrome():
    word1 = list(input('Enter the word: '))
    word2 = reversed(word1)

    word1 = ''.join(word1)
    word2 = ''.join(word2)
    if word1 == word2:
        print(f'{word2} is a palindrome')
    else:
        print(f'{word2} is not a palindrome')

# Counts symbol amount in sentences and words
def counting():
    sentence = list(input('Enter the sentence: '))
    length = len(sentence)
    print(f'This sentence has {length} symbols')

palindrome()
counting()

