#Bitwise Operators in Python

print("\n=====BITWISE OPERATORS IN PYTHON=====")

#Examples value
a, b=5, 3 #5=0101, 3=0011
print("using a =", a, "and b =", b)
print("Binary of a:", format(a, '04b'))
print("Binary of b:", format(b, '04b'))

#Basic bitwise operations
print("a&b ->", a&b, "Binary:", format(a&b,'04b')) #AND
print("a | b ->", "Binary:", format (a|b ,'04b'))   #OR
print("a ^ b ->", "Binary:", format(a^b,'04b'))     #XOR
print("~a    ->", "Binary:", format(~a&0XFF,'08b')) #NOT

#Shifts
print("a << 1 ->", a << 1, "Binary:", format (a << 1,'04b'))
print("a >> 1 ->", a >> 1, "Binary:", format(a >> 1,'04b'))

#User input example
x = int(input("\nEnter first integer: "))
y = int(input("Enter second integer:"))

print ("\nBitwise results:")
print(x, "&" ,y, "=",x & y)
print(x, "|", y, "=", x | y)
print(x, "^", y, "=", x ^ y)
print("~",x , "=", ~x)
print(x, "<<1 =", x << 1)
print(x, ">>1 =", x >> 1)

print("\nBitwise operators : &, |, ^, ~, <<, >>,")