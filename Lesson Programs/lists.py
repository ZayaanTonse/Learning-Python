#Lists in Python

#Creating lists
nums=[10,20,30]
mixed=[10,"Python",3.14]
nested=[[1,2],[3,4]]

print(nums)
print(mixed)
print(nested)

#Indexing & slicing
print(nums[0], nums[-1])
print(nums[1:3],nums[::-1])

#List methods
fruits=["apple","banana"]
fruits.append("mango")
fruits.insert(1,"graps")
fruits.remove("banana")
print(fruits)

#Iterating
for f in fruits:
    print(f)

#Nested lists access
matrix=[[1,2],[3,4]]
print(matrix[1][0])