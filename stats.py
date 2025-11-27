def get_num_words(text):
    count = len(text.split())
    return count


def get_num_letters(text):
    letters = {}

    for text_letter in text:
        if text_letter != ' ':
            letter = text_letter.lower()
            letters[letter] = letters.get(letter, 0) + 1
    
    return letters


def sorting_fn(items):
    return items['num']

def get_sorted_elements(dict):
    unsorted = [{ 'char': key, 'num': value } for key, value in dict.items()]
    print(f"Unsorted {unsorted=}")
    unsorted.sort(reverse=True, key=sorting_fn)


    return unsorted
