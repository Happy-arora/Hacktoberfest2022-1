# Useful functions for python

def concatenate_string(str_a, str_b):
  return str_a + str_b;

def value_in_string(string, value):
  exists = False;
  if value in string:
    exists = True
  return exists

def generate_pass():
  random_string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
  number_characters = 15
  return("".join(random.sample(random_string,number_characters )))

def palindrome():
  palindrome = False
  palindrome_word=str(input("Enter a word: "))
  reverse_word=palindrome_word[::-1]
  if palindrome_word == reverse_word:
      palindrome = True
  return palindrome

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        return quicksort([x for x in array[1:] if x < array[0]])
        + [array[0]]
        + quicksort([x for x in array[1:] if x >= array[0]])

def normalized_value(value, val_min, val_max)
    return ((value - val_min) / (val_max - val_min))
