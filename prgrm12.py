
list1 = list(map(int, input("Enter the first list of integers: ").split()))
list2 = list(map(int, input("Enter the second list of integers: ").split()))

# 1. Check whether the lists are of the same length
if len(list1) == len(list2):
    print("1. The lists are of the same length.")
else:
    print("1. The lists are not of the same length.")

# 2. Check whether the lists have the same values
if list1 == list2:
    print("2. The lists have the same values.")
else:
    print("2. The lists do not have the same values.")

# 3. Check whether any value occurs in both lists
common_values = set(list1).intersection(set(list2))

if common_values:
    print("3. Common value(s) found:", common_values)
else:
    print("3. No common values found.")

