import this

text = "".join([this.d.get(c, c) for c in this.s])


# Count the quantity of letters in text:
def is_letter(letter):
    return letter.isalpha()


number_of_letters = len(list(filter(is_letter, text)))
print(number_of_letters)

# The quantity of vowels in text:
vowels = 'AaEeIiOoUu'


def vowel(element):
    return element in vowels


vowels_result = filter(vowel, text)
print(len(list(vowels_result)))

# Print each 18 symbol:
position_index = 18
symbol_count = text[::18]
enumerate_symbol = enumerate(symbol_count)
letters_list = []
for i, letter in enumerate_symbol:
    letter = letter.swapcase()
    index = (i+1)*position_index
    letters_list.append(str(index) + letter)
sep = '\n'.join(letters_list)
print(sep)
