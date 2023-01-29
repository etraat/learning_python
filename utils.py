def last_word(text):
    """Returns the last word from a string"""
    another = text.split()
    size = len(another)
    return another[size-1]

name = 'Programing there you go'
w = last_word(name)
print(w)