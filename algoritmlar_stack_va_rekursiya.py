""" 09/10/2025 """

# class Stack:
#     def __init__(self):
#         self.stack = []


#     def isEmpty(self): # bosh ekkanligin tekshirish
#         return len(self.stack) == 0
    
#     def push(self, data): # element qoshish
#         self.stack.append(data)
#         return True
    
#     def pop(self): # element sug'urib olish
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stack.pop()
        
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stack

# stack = Stack()
# stack.push(5)
# stack.push(6)
# stack.push(7)
# stack.push(8)
# print("Top element: ", stack.peek())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.isEmpty())



# m2

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def isEmpty(self): # Bo'sh ekenligini tekshirish
#         return len(self.stack) == 0
    

#     def push(self, data):  # element qoshish
#         for i in range(1, data + 1):
#             self.stack.append(i)
#         return f"Elements: {self.stack}"

    
#     def top(self): # top elementi yani yuqorida tugan element.
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stack[-1]
        
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stack[3]
        
#     def clear(self):  # Stack ichini elementlaradan tozalaydi
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stack.clear()
        
#     def show(self): # stack ichida nechata element borligini korsatadi
#        return self.stack
    


# stack = Stack()
# print(stack.isEmpty())
# print(stack.push(6))
# print(stack.show())
# print(stack.top())
# print(stack.pop())
# print(stack.isEmpty())
# print(stack.clear())
# print(stack.isEmpty())
# print(stack.show())
