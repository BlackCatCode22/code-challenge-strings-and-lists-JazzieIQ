# Code Challenge - Strings and Lists
# #
# Python file name: anotherListProgram.py
#
# Date: 9/11/23
#
# Programmer's name: Matthew Gutierrez

# Intro

print("\nWelcome to Mac Mac's Other Python Strings and Lists Program.\n\n")

# Part One: Strings

## Beginning srings

str_one = " The quick brown fox jumps over the lazy dog. "

str_two = "The slow black dog bows before the regal fox."

print("String One: " + str_one + "\n" + "String Two: " + str_two)

## to_do

str_one_no_spaces = str_one.replace(" ","")

string_cat = str_one + str_two

str_cat_length = int(len(string_cat))

string_cat_lower = string_cat.lower()

string_cat_upper = string_cat.upper()

##to_do: F-string

adjective = "smart"
verb = "ran"
preposition = "through"
str_formatted = f"The {adjective} brown fox {verb} {preposition} the lazy dog."

##to_do: find

str_dog_index = int(str_two.index("black dog"))

str_dog = str_two[9:18]

##output

print("\nNow some To-Do. \nstr_no_spaces is... " + str_one_no_spaces)
print("\nString One and Two together is: " + string_cat)
print("\nAnd is " + str(str_cat_length) + " characters long.")
print("\nIn Lower case: " + string_cat_lower)
print("\nIn Upper case: " + string_cat_upper)
print('\nI have formatted a string from: "The {adjective} brown fox {verb} {preposition} the lazy dog." to "' + str_formatted + '"')
print('\nIn String Two the index of "black dog" is: ' + str(str_dog_index))
print('\nHere is a subtring: "' + str_dog + '"')

# part Two: Lists

## string
str_for_list = "Natalia, Alice, Bob, Charlie, Sergei, David, Eve, Frank, Grace, Dmitri, Hannah,Isaac, Jack, Ivan, Olga"

##To_do: Functions

list_of_names = str_for_list.replace(",", "").split(" ")

list_of_names.sort()

list_sorted = list_of_names

list_sorted_reversed = str_for_list.replace(",", "").split(" ")

list_sorted_reversed.reverse()

def list_item_new_line(list_sorted_reversed):
    for i in list_sorted_reversed:
        (print("\n"+ i + "\n"))

list_of_first_three = list_sorted[0:3]

##append and insert

new_name_1 = "Svetlana"

new_name_2 = "Boris"

def new_names(list_sorted):
    list_sorted.append("Svetlana")
    list_sorted.insert(5, "Boris")
    print(list_sorted)
    list_sorted.sort()
    print("\nAnd now they are sorted again.\n\n" + str(list_sorted))
    list_sorted.extend(list_of_first_three)
    print("\nNow more names: \n\n" + str(list_sorted))
    list_sorted.sort()
    print("\nNow sorted again: \n\n" + str(list_sorted))
    return list_sorted

def names_adjusted(list_sorted):
    list_sorted.remove("Alice")
    print('\nOops "Alice" left down the rabbit hole.\n')
    print(list_sorted)
    create_set = set(list_sorted)
    print("\nHere is a set of names: \n\n" + str(create_set))
    return list_sorted

def make_list_original(list_sorted):
    my_set = set(list_sorted)
    list_sorted = list(my_set)
    list_sorted.sort()
    print("\nI turned it back into a list:\n\n" + str(list_sorted))


##output

print("\nNext Part\nA string list of names: " + str_for_list)

print("\nThey are sorted as a list now: \n" + str(list_sorted))

print("\nThey are reverse sorted as a list now: \n" + str(list_sorted_reversed))

list_item_new_line(list_sorted_reversed)

print("\nI have split three names: " + str(list_of_first_three) + "\n" + str(type(list_of_first_three)) + " is the type of the sublist.")

print("\nI have added new names to the sorted list:\n")

new_names(list_sorted)

names_adjusted(list_sorted)

make_list_original(list_sorted)

print("\n\nProgram End. K Thanks, bye.")