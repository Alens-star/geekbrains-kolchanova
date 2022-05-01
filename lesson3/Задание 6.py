def int_func(word):
    word = list(word)
    alph_l = 'abcdefghijklmnopqrstuvwxyz'
    alph_h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in alph_l:
        if i == word[0]:
            word[0] = alph_h[alph_l.index(i)]
    new_word = ''.join(word)
    return new_word

words_input = 'werttt reee ddd'
words_input = words_input.split(" ")

for num, word in enumerate(words_input):
    words_input[num] = int_func(word)
print(" ".join(words_input))
