#Data Structure in Python

print("\n=====DATA STRUCTURE=====")

#Built-in  Examples
S="Python"        #String
I=[10,20,30]      #List
t=(1,2,3)         #Tuple
st={10,20,20,30}  #Set(duplicates removed)
d={"name":"John","age":23}  #Dictionary

print(S)
print(I)
print(t)
print(st)
print(d)

#User-defined Data Structure:Stack(Using class)
class Stack:
      def __init__(self):
          self.items=[]
      def push(self, val):
          self.items.append(val)
      def pop(self):
          return self.items.pop()

#Using the stack
stk =Stack()
stk.push(100)
stk.push(200)
print("\nStack pop:",stk.pop())  #Last in, first out