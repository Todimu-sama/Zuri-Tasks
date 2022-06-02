# File Reading and Word Counting Task
# Author: Todimu Isewon

# read file content and return string of the file contents

import string


def read_file_content(filename: str) -> str:
    with open(filename, "r") as file:
        fileText = file.read()
    return fileText


# word counter function

def count_words() -> dict:
    text: str = read_file_content("./story.txt")
    wordFrequencies: dict = dict()
    wordsInText = text.split(" ")

    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation))

        # Split the line into words
        words = line.split(" ")

    for word in wordsInText:
        if word in wordFrequencies:
            wordFrequencies[word] += 1
        else:
            wordFrequencies[word] = 1

    return wordFrequencies


# Test
print(count_words())
