sentence = input()
punctuation = ".,!?;:'-\"()[]{}«»"
words = []
for word in sentence.split():
    clean_word = ""
    for char in word:
        if char not in punctuation:
            clean_word = clean_word + char
    if clean_word != "":
        words.append(clean_word)
print(words)
