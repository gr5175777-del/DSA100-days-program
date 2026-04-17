#reversing a queue ( by using stack(list) )
'''
from collections import deque

q = deque([1,2,3,4,5])
stack = []

#step1: push into stack
while q:
    stack.append(q.popleft())

#step2: push back to queue
while stack:
    q.append(stack.pop())

print("reverseed queue:",q)'''

#checking if queue is empty or not
'''
from collections import deque

q =deque([1,2,3,4,5])

if not q:
    print("queue is empty")
else:
    print("queue:",q) '''

#

class queueusingstacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self,x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return"empty"
        return self.s2.pop()
    
q = queueusingstacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())