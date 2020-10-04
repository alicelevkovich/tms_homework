word_one = 'Repaper'
word_two = 'Tenet'
word_three = 'Rotor'


def palindrome(word):
    if not isinstance(word, int):
        if word.lower() == word.lower()[::-1]:
            return True
        else:
            return False


def check_word(word):
    if palindrome(word) is True:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')


check_word(word_one)
check_word(word_two)
check_word(word_three)
