sentence = input()
punctuation = ".,!?;:'-\"()[]{}«»"
words = []
words_lower = []

for word in sentence.split():
    clean_word = ""
    for char in word:
        if char not in punctuation:
            clean_word = clean_word + char
    if clean_word != "" and clean_word.lower() not in words_lower:
        words.append(clean_word)
        words_lower.append(clean_word.lower())
print(words)
