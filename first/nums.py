# Слова в алфавите {a, b}, такие, что на третьем месте от
# начала слова стоит буква а, а на пятом месте с конца – буква b.


import re
pattern = r"[ab]{2}a[ab]*b[ab]{4}"
print("To stop process enter 0!")
while True:
    word = input("Enter the word: ")
    print(re.fullmatch(pattern, word))
    if word == "0":
        break

