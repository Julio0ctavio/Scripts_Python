def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    text = input_string.lower().replace(" ", "")
    # Traverse through each letter of the input string
    count = 1
    for letter in text:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        new_string = new_string + letter
        reverse_string = reverse_string + text[-count]
        count += 1
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
