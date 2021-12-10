# Author: JD 12/09/2021

def anagram(word_1, word_2):
    word_1 = list(word_1)
    word_1.sort()
    word_2 = list(word_2)
    word_2.sort()
    
    if word_1 == word_2:
        return "anagrams"
    else:
        return "not anagrams"
    
w1 = input("The first word: ")
w2 = input("The second word: ")

result = anagram(w1, w2)

print(w1, "and", w2, "are", result+".")

#test
print(anagram("fired", "fried") == "anagrams")
print(anagram("gainly", "laying") == "anagrams")
print(anagram("yes", "Yes") == "not anagrams")

