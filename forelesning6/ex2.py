word = "Hello, World"

# TASK1
print()

for char in word:
    if char.isupper():
        print(char)

# TASK2
print()

for letter in word.split():
    print(word[1])

#  TASK3
print()

vowels = ['a', 'e', 'i', 'o', 'u']
new_word = '_'
for letter in word:
    if letter in vowels:
        new_word += '_'
    else:
        new_word += letter
print(new_word)

# TASK4
print()

word1 = "Hell0, W0rld1"
digit = 0
letters = 0

for letter in word1:
    if letter.isdigit():
        digit = digit + 1
    elif letter.isalpha():
        letters = letters + 1
    else:
        pass

print(f"Letters are: {letters}")
print(f"Digits are: {digit}")

#  TASK 5
print()

word2 = "hellows"
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0
letters = 0

for letter in word2:
    if letter in vowels:
        vowelCount = vowelCount + 1
    elif letter.isalpha():
        letters = letters + 1
    else:
        pass

print(f"Letters are: {letters}")
print(f"Vowels are: {vowelCount}")