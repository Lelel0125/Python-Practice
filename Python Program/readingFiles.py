# Python reading files (.txt, .json, .csv)

import json
import csv

# file_path = "stuff/input1.txt"
# file_path = "stuff/input2.json"
file_path = "stuff/input3.csv"

try:
    with open(file= file_path, mode= "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)

        print(content) # csv print memory location

        for line in content: # for csv
            print(line)
            print(line[0])


except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")