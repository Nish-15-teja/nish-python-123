a="this is nishvika"
print(a[9])
print(a[0:9])
print(len(a))
print(len("this is nishvika"))
print(a[0:9:2])
print(a[0:])# print the entire string until the end means length
print(a[:9])#consider from 0 index and till the index before 9
print(a[:])#cosider total
print(a[::])# consider this as 1 skip (basically same string )
print(a[::5])
#negative indices
print(a[::-1])# reverse the string
print(a[16:0:-1])
print(a[-9:-1])
print(a.isalpha())
print(a.isalnum())
print(a.endswith("a"))
print(a.startswith("i"))
print(a.find("is"))# starting index of the character means from where it start
print(a.capitalize())
print(a.count("i"))# how many times it is present in the string
print(a.upper())
print(a.lower())
print(a.replace("is","are"))

