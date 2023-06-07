#!/usr/bin/python3

start = ord('a') - 1
end = ord('z')

for charac in range(end, start, -2):
    var1 = chr(charac) + chr((charac - 32) - 1)
    print(var1, end="")
print("")
