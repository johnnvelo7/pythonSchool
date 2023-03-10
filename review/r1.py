letter = input("Enter a letter: ")

if letter.lower() in "aeiou":
    print(f"The letter {letter} is a vowel.")
elif letter == 'y':
    print("Sometimes it is a vowel, sometimes consonant.")
else:
    print(f"The letter {letter} is a consonant.")