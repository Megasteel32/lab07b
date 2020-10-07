# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Luca Maddaleni
# Section:      273
# Assignment:   Lab 7 Program 1
# Date:         10/06/2020

listylist = [] # Creating an empty master list
data_entry = 1 # Creating a variable to track when data is being entered

while data_entry == 1:
    temp_list = [] # Asking for data entry
    temp_list = list(input("Enter data values! If you're done, enter 'done': ").split())
    if temp_list[0] == "done":
        data_entry = 0 # If the data entered is 'done', exits the program
    else:
        for i in range(len(temp_list)): # Makes sure the strings get converted to integers
            temp_list[i] = int(temp_list[i])
        listylist.append(temp_list) # Adds the temp list to the master list

max_value = sum(listylist[0])
place_in_list = 0

for i in range(len(listylist)): # Loops through all the lists in the master list, and if it finds one that is larger, records its value and place in list
    if sum(listylist[i]) > max_value:
        max_value = sum(listylist[i])
        place_in_list = i
print("The sum of elements which is highest is {}, adding up to {}.".format(listylist[place_in_list],max_value))