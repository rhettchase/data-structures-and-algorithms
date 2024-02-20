from data_structures.hashtable import Hashtable
import string


def normalize_word(input_string):
  words = input_string.split()

  # Create a translation table: maps each punctuation mark to None
  translate_table = str.maketrans('', '', string.punctuation)

  # Remove punctuation from each word and normalize to lowercase
  normalized_words = [word.translate(translate_table).lower() for word in words]

  return normalized_words

def first_repeated_word(input_string):
 words = normalize_word(input_string)
 seen_words = Hashtable()
 for word in words:
   if seen_words.has(word):
     return word
   seen_words.set(word, True) # mark word as seen with True
 return None
