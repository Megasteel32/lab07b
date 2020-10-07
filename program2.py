# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Luca Maddaleni
# Section:      273
# Assignment:   Lab 7 Program 2
# Date:         10/06/2020

user_word = input("Enter in a word: ")
while user_word != "stop":
    if user_word[0].lower() in ("a", "e", "i", "o", "u", "y"):
        new_word = user_word + "yay"
        print(new_word)
    else:
        new_word = user_word[1:] + user_word[0].lower() + "ay"
        print(new_word)
    user_word = input("Enter in a word: ")