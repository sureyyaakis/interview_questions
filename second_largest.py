# Input:
#  a: The given list/array of integers.  Example: [1, -2, 3, 4]
# Returns:
#  The second largest number in the list or None if
#  the array's length is only 1 or 2.

def second_largest(given_list):
  given_list.sort(reverse=True)
  second_largest = given_list[1]
  return (second_largest)
second_largest(1, -2, 3, 4)
