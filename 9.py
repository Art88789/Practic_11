text = ""
while True:
    line = input()
    if line == "":
        break
    text = text + " " + line
punctuation = ".,!?;:'-\"()[]{}«»"
words = []
for word in text.split():
    clean_word = ""
    for char in word:
        if char not in punctuation:
            clean_word = clean_word + char
    if clean_word != "":
        words.append(clean_word.lower())

word_count = {}
word_order = {}
order = 0

for word in words:
    if word not in word_count:
        word_count[word] = 0
        word_order[word] = order
        order = order + 1
    word_count[word] = word_count[word] + 1

unique_words = list(word_count.keys())
unique_words.sort(key=lambda w: (-word_count[w], word_order[w]))

for word in unique_words:
    print(word)
