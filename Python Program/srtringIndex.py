# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step] end exclusive

credit_num = "1234-5678-9012-3456"

# print(credit_num[0])    1
# print(credit_num[: 4])    1234
# print(credit_num[5 : 9])    5678
# print(credit_num[5 :])    5678-9012-3456
# print(credit_num[-1])    6
# print(credit_num[: : 2])    13-6891-46

# last_digit = credit_num[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digit}")

credit_num = credit_num[: : -1] # reverse
print(credit_num)