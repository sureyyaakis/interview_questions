"""
Problem: Compare two strings as numbers!
You are given two non-negative integers in strings.

Example: "1221" and "123"

Write a function, larger_than(a, b) which returns True if the first number is larger than the second one.

Solve this problem without converting the strings to numbers!
"""
# Input:
#  a: The first non-negative integer in string. Example: "123"
#  b: The second non-negative integer in string. Example: "3344"
# Returns:
#  True if a is larger than b.
#  False if a is smaller than or equal to b.


def larger_than(a,b):
  if len(a) > len(b):
    return True
  elif len(a) < len(b):
    return False
  
  for i in range(len(a)):
    if a[i] == b[i]:
      continue
    elif a[i] > b[i]:
      return True
    else:
      return False
  return False


print('Is "112" larger than "111"? (Should be True.)')
print(larger_than( "112", "111" ))
