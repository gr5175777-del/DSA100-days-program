#by using class and object

class stack:
    def __init__(self):
        self.stack =[]

        #push
    def push(self,data):
        self.stack.append(data)


        #pop
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()

        #peek
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]

        #isempty
    def is_empty(self):
        return len(self.stack) == 0

        #size
    def size(self):
        return len(self.stack)

s = stack()
s.push(10)
s.push(20)
s.push(30)

print("top:",s.peek())
print("popped:",s.pop())
print("size:",s.size())
print("is empty:",s.is_empty())


#by using list(buit in function)
'''
stack = []
#push
stack.append(10)
stack.append(20)
stack.append(30)
print("satck after push:",stack)

#pop
removed = stack.pop()
print("poped element:",removed)
print("stack after pop:",stack)

#peek
top = stack[-1]
print("top element:",top)

#is_empty
print("is stack empty ",len(stack)== 0)

#size
print("stack size:",len(stack))'''

#by using class and object

'''from collections import deque
stack = deque()

#push
stack.append(10)
stack.append(20)

print(stack)

#pop
stack.pop()
print(stack)

#peek
print(stack[-1])'''

'''def valid(s):
    stack = []
    mapping = {')':'(','}':'{',']':'['}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0
s = input("enter a string of brackets:")

if valid(s):
    print("valid paranthases")
else:
    print("invalid paranthases")'''

     