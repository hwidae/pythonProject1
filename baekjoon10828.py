import sys
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        else :
            return self.stack.pop()

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else :
            return 0

    def top(self):
        if len(self.stack) == 0:
            return -1
        else :
            return self.stack[len(self.stack)-1]

newstack = Stack()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    a = sys.stdin.readline().rstrip()
    if a[0:4] == 'push':
        b,c = a.split()
        newstack.push(c)
    elif a == 'top':
        print(newstack.top())
    elif a == 'size':
        print(newstack.size())
    elif a == 'empty':
        print(newstack.empty())
    elif a == 'pop':
        print(newstack.pop())