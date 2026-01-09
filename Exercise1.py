word = input("Enter a word: ")
vowel = 0
letter = ""

for letter in word:
  if letter in "AEIOUaeiou":
    vowel += 1

if vowel == 0:
  print("No vowels")
else: 
  print("Output: " + str(vowel))