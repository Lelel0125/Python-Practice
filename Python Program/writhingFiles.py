# Python writing files (.txt, .json, .csv(comma separeate value))

import json
import csv

# txt_data = "I like pizza!"
# employees  = ["Eugene", "Squidward", "Spongebob", "Patrick"]


# json
# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }


# csv
employees = [["Name", "Age", "Job"], 
             ["Spongebob", 30, "Cook"], 
             ["Patrick", 37, "Unemployed"], 
             ["Sandy", 27, "Scientist"]]


# file_path = "stuff/output1.txt"    # relative or absolutely
# file_path = "stuff/output2.json"    # relative or absolutely
file_path = "stuff/output3.csv"    # relative or absolutely

try:
    with open(file= file_path, mode= "w", newline="") as file:    # mode: a = append, w = (over)write, r = read, x = create
        # file.write("\n" + txt_data)
        # for employee in employees:
        #     file.write(employee + " ") 

        # json.dump(employee, file, indent=4)

        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)


        # print(f"txt file '{file_path}' was created")
        # print(f"json file '{file_path}' was created")
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")