# Exercise 4: Sentence Analysis

sentence = input("Enter a sentence: ")

vowels = 0
spaces = 0

for letter in sentence:
    if letter.lower() in "aeiou":
        vowels = vowels + 1

    if letter == " ":
        spaces = spaces + 1

print("Characters:", len(sentence))
print("Vowels:", vowels)
print("Spaces:", spaces)