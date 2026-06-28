# format specifiers = {value:flags} format a value based on what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces    (add 0 in front of number Ex. 012)
# :< = left justify    (place in left)
# :> = right justify    (place in right)
# :^ = center align    (place in center)
# :+ = use a plugs sign to indicate positive value    (show positive or negative)
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator    (Ex.1,200)

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:=}")
print(f"Price 2 is ${price2:=}")
print(f"Price 3 is ${price3:=}")