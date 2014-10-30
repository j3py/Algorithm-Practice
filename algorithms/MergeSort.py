#-------------------------------------------------------------------
#MERGE SORT  O(n log n)

# Mergesort consumes an unsorted list and returns a sorted list
def mergesort(l):
    if len(l) < 2:
        return l
    pivot = len(l) / 2
    first_half = mergesort(l[:pivot])  # mergesort will sort these lists
    second_half = mergesort(l[pivot:])
    
    return merge(first_half, second_half)

def merge(one, two):  # Google lambda again
    add_top = lambda one, two: one.pop(0) if one[0] < two[0] else
    add_rest = lambda one, two: one if len(one) else two
    merged = []
    while len(one) and len(two):
        merged.append(add_top(one, two))
    merged += add_rest(one, two)
    return merged
    
evens = range(20)[::2]
odds = range(20)[1::2]

l = [...] # Make your list
print(mergesort(l))