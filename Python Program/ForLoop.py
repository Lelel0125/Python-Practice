# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# reversed(range(1, 11)) -> 10, 9, 8...
# for x in range(1, 11, 3):
#     print(x)

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

for x in range(1, 21):
    if x == 13:
        # continue 10 11 12 14 15...
        break #10 11 12
    else:
        print(x)