import math

text = 'Beautiful is better than ugly. \n' \
       'Explicit is better than implicit. \n' \
       'Simple is better than complex. \n' \
       'Complex is better than complicated. \n' \
       'Flat is better than nested. \n' \
       'Sparse is better than dense. \n' \
       'Readability counts.' \
       'Special cases aren\'t special enough to break the rules. \n' \
       'Although practicality beats purity. \n' \
       'Errors should never pass silently. \n' \
       'Unless explicitly silenced. \n' \
       'In the face of ambiguity, refuse the temptation to guess. \n' \
       'There should be one-- and preferably only one --obvious way to do it. \n' \
       'Although that way may not be obvious at first unless you\'re Dutch. \n' \
       'Now is better than never. \n' \
       'Although never is often better than *right* now. \n' \
       'If the implementation is hard to explain, it\'s a bad idea. \n' \
       'If the implementation is easy to explain, it may be a good idea. \n' \
       'Namespaces are one honking great idea -- let\'s do more of those! \n'

e_mail = text + 'alicelevkovichlev@gmail.com'
vowels = 'AaEeIiOoUu'


# Count the quantity of letters in text:
letter_count = 0
for letter in text:
    if letter.isalpha():
        letter_count += 1


# The quantity of vowels in text:
def vowel(text_, vowels_):
    result = [letters for letters in text_ if letters in vowels_]
    return len(result)


print(vowel(text, vowels))


# Print each 18 symbol:
position = 18
symbols_count = math.floor(len(text) / position)
letters_list = []
for i in range(0, symbols_count):
    index = (position * i) + position
    letter = text[index]
    if letter.islower():
        letter = letter.upper()
    elif letter.isupper():
        letter = letter.lower()
    letters_list.append(str(index) + letter)
sep = '\n'
sep = sep.join(letters_list)
print(sep)

