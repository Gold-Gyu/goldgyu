def count_vowels(words):
    lst = []
    for word in words:
        if word in 'aeiou':
            lst.append(word)

    return len(lst)

count_vowels('apple')
