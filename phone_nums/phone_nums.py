# Ryan Smith
# rnsmith2@gmail.com
# A Python script to generate words from phone numbers to ease memorization of numbers.

import itertools

def find_words(numbers, avail_words):
    """Given a set of phone numbers, like a phone number, strip away any non-numeric formatting (i.e. (555) 555-5555 will be stripped to 55555555555), and then using the normal associated letter conventions return a list of words that correspond to those letters.  Because 1 doesn't have any letters associated with it, we will by default map 1's to spaces, breaking up any given word into smaller words."""
    if "1" in numbers:
        numbers = numbers.split("1")
    else:
        numbers = [numbers]

    for num in numbers:
        # strip away non-digit characters
        num = [int(x) for x in num if x.isdigit()]
        print(num)
        combos = {x for x in num_letters[num[0]]}
        for digit in num[1:]:
            combos = {combo + letter for combo in combos for letter in num_letters[digit]}
        print(combos & avail_words)
# set the number-letter mappings
num_letters = {
    2: {"a", "b", "c"},
    3: {"d", "e", "f"},
    4: {"g", "h", "i"},
    5: {"j", "k", "l"},
    6: {"m", "n", "o"},
    7: {"p", "q", "r", "s"},
    8: {"t", "u", "v"},
    9: {"w", "x", "y", "z"}
    }

# read dictionary file into a set
with open("wordlist.txt") as dictionary:
    dictionary = dictionary.read()
    avail_words = {word for word in dictionary.split()}

if __name__ == "__main__":
    find_words("234", avail_words)
