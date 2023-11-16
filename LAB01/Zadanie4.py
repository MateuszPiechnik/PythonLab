import re

def swapWordsWithRe(file, words):
    with open(file) as f1:
        text = f1.read()
    for word, changeWord in words.items():
        text = re.sub(word, changeWord, text)

    with open('changeTextRe', 'w') as f2:
        f2.write(text)

def swapWords(file, words):
    with open(file) as f1:
        text = f1.read()
    for word, changeWord in words.items():
        text = text.replace(word, changeWord)

    with open('changeText', 'w') as f2:
        f2.write(text)

change = {
    "Python" : "C++",
    "often" : "sometimes"
}

change2 = {
    "Python" : "Matlab",
    "It" : "This"
}

swapWords('tekst', change)
swapWordsWithRe('tekst', change2)