# Input:
#  a: The first non-negative integer in string. Example: "123"
#  b: The second non-negative integer in string. Example: "3344"
# Returns:
#  True if a is larger than b.
#  False if a is smaller than or equal to b.


def larger_than(a, b):
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif  a[i] > b[i]:
            return True
        else:
            return False
    return False
