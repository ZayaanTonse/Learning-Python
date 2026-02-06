#Python Program :String data type

import sys

#Single-line string declaration
string_text="Hello,python!"
print("Single-line string value:",string_text)

#Multi-line string declaration
Multi_line_string="""This is a 
multi-line string example.
It can span Multiple lines."""
print("\nMulti-line string value:\n",Multi_line_string)

#Input
user_string=input("\nEnter a string: ")
print("You entered string:",user_string)

#Type checking
print("\nType of string text:",type(string_text))
print("Type of Multi_line_string:",type(Multi_line_string))
print("Type of user_string:",type (user_string))

#Type casting
string_from_int=str(123)
string_from_float=(45.67)
print("\nString from int:",string_from_int)
print("\nString from float:",string_from_float)

#Storage(memory size in bytes)
print("\nMemory size of multi_line_string:",sys.getsizeof(Multi_line_string), "bytes")
print("Memory size of multi_line_string:",sys.getsizeof(Multi_line_string), "bytes")