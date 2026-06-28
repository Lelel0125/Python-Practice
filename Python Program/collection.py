# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set  = {} unordered and immutable(unchanged), but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")

## General
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)    True or False

## List
# fruits[0] = "pineapple"    replace
# fruits.append("pineapple")    add in last
# fruits.remove("apple")
# fruits.insert(0, "pineapple")    insert in specific place
# fruits.sort()    alpha quence
# fruits.reverse()    reverse quence(1 3 2 4 -> 4 2 3 1)
# fruits.clear()    remove all values
# print(fruits.index("pineapple"))    where it is (If doesn't exist, error)
# print(fruits.count("banana"))     If it exist (0 or 1)

## Set
# print(fruits)    Random quence
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()    remove random one
# fruits.clear()

## Tuple
# print(fruits.index("apple"))    found in specific places
# print(fruits.count("coconut"))    how many specific value in Tuple

print(fruits)
# for fruit in fruits:
#     print(fruit)