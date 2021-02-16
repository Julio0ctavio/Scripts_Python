import re  # Advanced regular expresions: https://regexcrossword.com/

# sample string:
state = "Aguascalientes"
gametag = "EnablingList48"

# A simple search:
result = re.search("aza", "bazaar")

# Another searchs with regular expresions:
regex_result = re.search(r"list", gametag.lower())
print(regex_result)

regex_result = re.search(r"b.ing", gametag.lower())
print(regex_result)

regex_result = re.search(r"[a-z]gu", state)
print(regex_result)

print("\n")
''' Fill in the code to check if the text passed contains punctuation symbols:
commas, periods, colons, semicolons, question marks, and exclamation points. '''


def check_punctuation(text):
    result = re.search(r"\.|\?|\!|\'|\,", text)
    return result is not None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

print("\n")

''' The repeating_letter_a function checks if the text passed includes the letter "a"
lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True,
 while repeating_letter_a("pineapple") is False. Fill in the code to make this work. '''


def repeating_letter_a(text):
    result = re.search(r"([aA].*){2,}", text.lower())
    return result is not None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True


''' Fill in the code to check if the text passed has at least 2 groups of alphanumeric
characters (including letters, numbers, and underscores) separated by one or more
whitespace characters. '''

print("\n")


def check_character_groups(text):
    result = re.search(r"(\w+)\b(.\w)+", text)
    return result is not None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

''' Fill in the code to check if the text passed looks like a standard sentence,
 meaning that it starts with an uppercase letter, followed by at least some lowercase
 letters or a space, and ends with a period, question mark, or exclamation point. '''

print("\n")


def check_sentence(text):
    result = re.search(r"^[A-Z]+[a-z\s]+[\?|\.!]$", text)
    return result is not None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True


''' The check_web_address function checks if the text passed qualifies as a top-level web address,
meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores),
as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level
domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that,
using escape characters, wildcards, repetition qualifiers,
beginning and end-of-line characters, and character classes. '''

print("\n")


def check_web_address(text):
    pattern = r'^[A-Za-z\w][^/@]*$'
    result = re.search(pattern, text)
    return result is not None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True


''' The check_time function checks for the time format of a 12-hour clock, as follows:
the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes
between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.
Fill in the regular expression to do that. How many of the concepts that you just learned can you use here? '''

print("\n")


def check_time(text):
    pattern = r'[0-1]*[0-9]+:[0-5]+[0-9]+[\s]?[AM|am|PM|pm]+'
    result = re.search(pattern, text)
    return result is not None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False

''' The contains_acronym function checks the text for the presence of 2 or more characters
or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter),
returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM)
is a set of communication technologies used for text-based communication" should return True since (IM)
satisfies the match conditions." Fill in the regular expression in this function: '''

print("\n")


def contains_acronym(text):
    pattern = r'[\()@]'
    result = re.search(pattern, text)
    return result is not None


print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True


'''Fill in the code to check if the text passed includes a possible U.S. zip code,
formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits.
The zip code needs to be preceded by at least one space, and cannot be at the start of the text.'''


print("\n")


def check_zip_code(text):
    result = re.search(r"^[^\d{5}]+.+\d{5}[-\d{4}]?.*$", text)
    return result is not None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

'''The long_words function returns all words that are at least 7 characters.
Fill in the regular expression to complete this function.'''


print("\n")


def long_words(text):
    pattern = r'\b(\w{7,})'
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []


'''Add to the regular expression used in the extract_pid function,
to return the uppercase message in parenthesis, after the process id.'''

print("\n")


def extract_pid(log_line):
    regex = re.compile(r"\[(\d+)\]\: ([A-Z]+)")
    result = regex.search(log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


# 12345 (ERROR)
print(extract_pid(
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
# 67890 (RUNNING)
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))


''' We're working with a CSV file, which contains employee information.
Each record has a name field, followed by a phone number field, and a role field.
The phone number field contains U.S. phone numbers, and needs to be modified
to the international format, with "+1-" in front of the phone number.
Fill in the regular expression, using groups, to use the transform_record function to do that. '''

print("\n")


def transform_record(record):
    new_record = re.sub(r",(\d)", r",+1-\1", record)
    return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer


''' The multi_vowel_words function returns all words with 3 or more consecutive vowels
(a, e, i, o, u). Fill in the regular expression to do that.'''

print("\n")


def multi_vowel_words(text):
    pattern = r"(\w+[a|e|i|o|u]{3,}\w+)"
    result = re.findall(pattern, text)
    return result


print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []


''' Question 5
The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX
(3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits),
and converts it to a more formal format that looks like this: (XXX) XXX-XXXX.
Fill in the regular expression to complete this function.'''

print("\n")


def convert_phone_number(phone):
    result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4}\b)", r"(\1) \2-\3", phone)
    return result


print(convert_phone_number("My number is 212-345-9999."))  # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234"))  # Please call (888) 555-1234
print(convert_phone_number("123-123-12345"))  # 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))
