#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]  # char from the beginning to position 3 (excluded)
word_last_2 = word[7:]  # character from position 7 (included) to the end
middle_word = word[1:8]  # char from position 1 (included) to 8 (excluded)
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
