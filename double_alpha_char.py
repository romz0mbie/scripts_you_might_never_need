#!/usr/bin/python3
#Created by OpenAI

for first_letter in range(ord('a'), ord('z') + 1):
    for second_letter in range(ord('a'), ord('z') + 1):
        combination = chr(first_letter) + chr(second_letter)
        print(combination)
