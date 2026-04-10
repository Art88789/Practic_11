HOLED_LETTERS = "abdegopq"

def count_holed_letters(word):
    """Подсчитывает количество букв с отверстиями в слове"""
    count = 0
    for char in word:
        if char in HOLED_LETTERS:
            count += 1
    return count

def count_letters(text):
    """Подсчитывает буквы с отверстиями и без отверстий в тексте"""
    holed = 0
    not_holed = 0
    for char in text:
        if char.isalpha():  
            if char in HOLED_LETTERS:
                holed += 1
            else:
                not_holed += 1
    return holed, not_holed

def words_with_holes(text):
    """Возвращает список слов с двумя и более буквами с отверстиями"""
    result = []
    words = text.split()
    for word in words:
        if count_holed_letters(word) >= 2:
            result.append(word)
    return result
text = input()
holed_count, not_holed_count = count_letters(text)
words_list = words_with_holes(text)
print(holed_count, not_holed_count)
print(words_list)
