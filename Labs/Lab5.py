word = input("Please Enter Your Own Word : ")
vowels = 0
consonants = 0
letters = 0

word.lower() # convert the word to lowercase

for i in word:
  if i.isalpha(): # check if the character is a letter
    letters += 1 # increment the letter count
    if i in 'aeiou': # check if the letter is a vowel
      vowels += 1 # increment the vowel count
    else:
      consonants += 1 # increment the consonant count

print("Total Number of Letters in this Word = ", letters)
print("Total Number of Vowels in this Word = ", vowels)
print("Total Number of Consonants in this Word = ", consonants)
