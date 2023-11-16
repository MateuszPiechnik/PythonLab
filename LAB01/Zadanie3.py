import re

def removeWordWithRe(file, word):
        with open(file) as f1:
            text = f1.read()
            text = re.sub(word, '', text)

        with open('removeWithRe', 'w') as f2:
                f2.write(text)

def removeWord(file, word):
        with open(file, 'r') as f1:
                text = f1.read()
                text = text.replace(word, '')

        with open('removeText', 'w') as f2:
                f2.write(text)

removeWord('tekst', 'Python')
removeWordWithRe('tekst', 'typed')

