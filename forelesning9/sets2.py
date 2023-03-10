def clean(string):
    result = ""
    for char in string:
        if char.isalnum():
            result = result + char.lower()
    return result

uniquewords = set()

sentence = input("Enter a sentence: ")

theWords = sentence.split()

for word in theWords:
    cleaned = clean(word)
    if cleaned != "":
        uniquewords.add(cleaned)

print("The length of unique words are", len(uniquewords), " words.")
print(uniquewords)