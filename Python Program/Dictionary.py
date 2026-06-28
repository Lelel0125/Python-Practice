# dictionary = a collection of {key:value} pairs
#              ordered and changeab;e. No duplicates

capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi", 
            "China": "Beijing", 
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))    #Washington D.C.
# print(capitals.get("Japan"))    #None

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})    #add to last
# capitals.update({"USA": "Detroit"})    #update info

# capitals.pop("China")    #remove selected key and value
# capitals.popitem()    #remove last key and value
# capitals.clear()    #remove all key and value

# keys = capitals.keys()    #get all key in dic
# for key in keys:
#     print(key)

# values = capitals.values()    #get all value in dic
# for value in values:
#     print(value)

items = capitals.items()    #show key and value in 2D list
for key, value in items:
    print(f"{key}: {value}")