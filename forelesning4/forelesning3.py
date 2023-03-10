#!usr/bin/env python3

a = 1

if a > 5:
    print("HI")
    a = a + 2
    print("a = ", a)

else:
    print("whatever")

# false statement
s1 = "car"
s2 = "cart"

print(s1 > s2)

# if else

originalPrice = float(input("Please enter the original price: "))
if originalPrice < 128:
    discountRate = 0.92
else:
    discountRate = 0.84

discountedPrice = originalPrice * discountRate

print("Price = %.2f" % discountedPrice)


string = input("Enter a String")

position = len(string) // 2

if len(string) % 2 == 1:
    result = string[position]
else:
    result = string[position-1] + string[position]

print("Middle character(s) in '%s' is '%s'" % (string, result))



