languages = ["python", "perl", "java", "go", "C"]
lenght = [language for language in languages]
print(lenght)
lenght_values = [len(language) for language in languages]
print(lenght_values)
numbers_13 = [i for i in range(1, 100) if i % 13 == 0]
print(numbers_13)


'''Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. }
Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.
'''

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = []
for item in filenames:
    file_data = item.split(".")
    if(file_data[1] == "hpp"):
        file_data[1] = "h"
        selected_item = ".".join(file_data)
        newfilenames.append(selected_item)
    else:
        newfilenames.append(item)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


'''Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving
the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
'''


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    new_list = []
    for word in words:
        # Create the pig latin word and add it to the list
        n = len(word)
        new_list.append(word.replace(word, (word[1:n] + word[0] + "ay")))

    # Turn the list back into a phrase
    say = " ".join(new_list)
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))


'''
Question 3
The permissions of a file in a Linux system are split into three sets of three permissions:
read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission,
with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or -
 when the permission is not granted. For example: 640 is read/write for the owner, read for the group, and no permissions for the others;
  converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others;
  converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal format into a string format.'''


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for octal_digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if octal_digit >= value:
                result += letter
                octal_digit -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


'''
The group_list function accepts a group name and a list of members, and returns a string with the format:
group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".
Fill in the gaps in this function to do that.'''


def group_list(group, users):
    formatting_group = ""
    if(users != []):
        members = [member for member in users]
        members = ", ".join(members)
        formatting_group = "{}: {}".format(group, members)
    return formatting_group


# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"
