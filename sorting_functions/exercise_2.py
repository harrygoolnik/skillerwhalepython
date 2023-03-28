from utils.example_data import words, word_frequencies
from utils.utils import print_rainbow


# pylint: disable=pointless-string-statement
"""
SORTING WITH KEYS
-----------------

Replace the empty lists in the definitions below so that each of the lists is
a sorted version of `words`.
"""

# * `longest_words` should be sorted by length, with the longest word appearing
#     at the start of the list.
longest_words = ...

# * `custom_sorted` should be sorted in reverse alphabetical order, but with
#   the first letter removed. For example, ['azure', 'turquoise', 'blue', 'teal']
#     is sorted in this way (using 'zure', 'urquoise', 'lue', 'eal' as sort keys)
custom_sorted = ...

print("The longest words are:")
print_rainbow(longest_words)

print()
print("The alphabetically last words excluding the first letter are:")
print_rainbow(custom_sorted)

# * Uncomment the assert statements to check your answers.
# # <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>
# assert longest_words[:2] == ['telecommunications', 'responsibilities'], \
#     f"Wrong first two longest_words, {longest_words[:2]}, should be ['telecommunications', 'responsibilities']"
# assert custom_sorted[:3] == ['ozone', 'gzip', 'azerbaijan'], \
#     f"Wrong first three words in custom_sorted, {custom_sorted[:3]}, should be ['ozone', 'gzip', 'azerbaijan']"
