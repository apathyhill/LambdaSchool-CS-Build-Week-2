# Problem:
# Implement Queue using Stacks

# URL: 
# https://leetcode.com/problems/implement-queue-using-stacks/

# Solution:
class MyQueue:
    def __init__(self):
        self.storage = [] # Stack container

    def push(self, x: int) -> None:
        storage_temp = [] # Keep temp stack
        while not self.empty():
            storage_temp.insert(0, self.pop()) # Push all to temp
        self.storage.insert(0, x) # Push element
        while len(storage_temp) > 0: # Push elements from temp back
            self.storage.insert(0, storage_temp.pop(0))
        
    def pop(self) -> int:
        if not self.empty():
            return self.storage.pop(0) # If not empty, pop off top of stack
        
    def peek(self) -> int:
        if not self.empty():
            return self.storage[0]  # If not empty, return top of stack wtihout popping
        
    def empty(self) -> bool:
        return len(self.storage) == 0 # Is empty if len(storage) == 0