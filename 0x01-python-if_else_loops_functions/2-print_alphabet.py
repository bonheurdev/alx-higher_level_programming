#!/usr/bin/python3
# the ord() function is used to get the ASCII value of a character
start = ord('a')
end = ord('z') + 1
for i in range(start, end):
    char = chr(i)  # convert an ASCII value back to character
    print(char, end="")
