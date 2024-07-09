#this program translates from pig latin to english. It works by seperating vowels from their "yay" addition and consonants from their "ay" addition and then reordering the letters to form the original word. The translated sentence is then printed.
import sys

value1 = sys.argv[1]

sentence = ""

for word in value1.split(" "):
    if "yay" in word:
        sentence += word[:-3] + " "
    elif "ay" in word:
        #take away the ay
        word = word[:-2]
        #find index of the dash
        dashIndex = word.index("-")
        #add the letters after the dash to the beginning of the word and take away the dash
        word = word[dashIndex+1:] + word[:dashIndex]
        sentence += word + " "

print(sentence) 