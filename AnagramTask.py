# Complete Anagram function
# Author Todimu Isewon

def find_anagrams(firstWord: str, secondWord: str) -> bool:
    # convert the entries to lowercase just in case
    firstWordLc = firstWord.lower()
    secondWordLc = secondWord.lower()

    # first remove all spaces in the text
    firstWordStripped = firstWordLc.replace(" ", "")
    secondWordStripped = secondWordLc.replace(" ", "")

    # next sort the string characters alphabetically
    firstWordSorted = "".join(sorted(firstWordStripped))
    secondWordSorted = "".join(sorted(secondWordStripped))

    # If they are anagrams, they should be of the same length and have same contents
    if firstWordSorted == secondWordSorted and len(firstWordSorted) == len(secondWordSorted):
        return True
    else:
        return False


# Test code to see if it works
wordOne: str = "tom marvolo riddle"
wordTwo: str = "i am lord voldemort"
print(find_anagrams(wordOne, wordTwo))  # returns true

wordOne: str = "sticky fingers"
wordTwo: str = "za warudo"
print(find_anagrams(wordOne, wordTwo))  # returns false

wordOne: str = "a gentleman"
wordTwo: str = "elegant man"
print(find_anagrams(wordOne, wordTwo))  # returns true

wordOne: str = "mother in law"
wordTwo: str = "hitler woman"
print(find_anagrams(wordOne, wordTwo))  # returns true
