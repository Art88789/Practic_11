def get_cleaned_words(text):
    """
    Принимает строку, удаляет из слов знаки препинания 
    и возвращает список очищенных слов.
    """
    punctuation = ".,!?;:'-\"()[]{}«»"
    words = []

    for word in text.split():
        clean_word = ""
        for char in word:
            if char not in punctuation:
                clean_word += char
        
        if clean_word:
            words.append(clean_word)
            
    return words


sentence = input()
result = get_cleaned_words(sentence)
print(result)
