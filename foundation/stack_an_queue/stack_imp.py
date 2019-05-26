class Stack_Imp():
    def __init__(self):
        self.arr=[]
    def push(self,val):
        print(val, ' is pushed into the stack')
        return self.arr.append(val)
    def isEmpty(self,):
        return self.arr.__len__() == 0
    def pop(self):
        if self.arr.__len__()==0:
            return ("Stack is already empty")
        else:
            return self.arr.pop()
    def printArray(self):
        return self.arr
    def search_val(self, val1):
        if val1 in self.arr:
            print(val1, ' found')
            return self.arr.index(val1)
        else:
            return 'Nothing found'
s=Stack_Imp()
s.push(1)
s.push(3)
s.push(5)
s.search_val(3)
print(s.printArray())
s.pop()
s.search_val(2)
print(s.printArray())
s.pop()
s.pop()
s.pop()