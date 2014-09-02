#!/usr/bin/env python3
i = 1
print("MULTIPLICATION TABLE")
print("-" * 50)
while i < 11:
    n = 1
    while n <=10:
        print("%5d" % (n * i), end = " ")
        n += 1
    print()
    i += 1
print("-" * 50)
