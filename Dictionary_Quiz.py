'''The groups_per_user function receives a dictionary, which contains group names with the list of users.
Users can belong to multiple groups.
Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values'''


def groups_per_user(group_dictionary):
    user_groups = {}
    list_aux = []
    list_groups = []
    group_d = ""
    # Go through group_dictionary
    for group in group_dictionary:
        # Now go through the users in the group
        for user in group_dictionary[group]:
            # Now add the group to the the list of
            user_groups[user] = ""
            list_aux.append(user+"="+group)
# groups for this user, creating the entry
    for user in user_groups:
        for item in list_aux:
            group_d = item.split("=")
            if(group_d[0] == user):
                list_groups.append(group_d[1])
        user_groups[user] = list_groups
        list_groups = []

# in the dictionary if necessary

    return(user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))


'''The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.'''


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for item in basket:
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += basket[item]
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44

'''
Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries,
with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list,
but Rory's list has more current information about the number of guests.
Fill in the blanks to combine both dictionaries into one, with each friend listed only once,
and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries.
Then print the resulting dictionary.
'''


def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    full_dict = {}
    full_dict.update(guests1)
    for person in guests2:
        if(person in full_dict):
            full_dict[person] += guests2[person]
        else:
            full_dict[person] = guests2[person]
    return full_dict


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1,
                "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1,
                  "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))


'''
Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation.
Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.")
should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
'''


def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text.lower():
        # Check if the letter needs to be counted or not
        if(letter.isalpha() is False):
            continue
        # Add or increment the value in the dictionaryelse:
        else:
            result[letter] = text.lower().count(letter)

    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
