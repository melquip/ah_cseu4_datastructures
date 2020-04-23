# Queue
# First In First Out -> FIFO
# A good example of a queue is any queue of consumers where the consumer that came first is served first


# Stack
# Last In First Out -> LIFO



# The difference between queues and stacks is in removing.
# In a queue, we remove the item the least recently added.
# In a stack we remove the item the most recently added.

# Implement Queue using Stacks
# This method makes sure that oldest entered element is always at the top of stack 1, so that dequeue operation just pops from stack1. To put the oldest element at top of stack1, stack2 is used.

class Queue:
  def __init__(self):
    # items from old => new
    # 1,2,3,4
    self.stack1 = []
    # items from new => old
    # 4,3,2,1
    self.stack2 = []

  def enqueue(self, newItem): 
    # Move all items in stack 1 to stack 2
    while len(self.stack1) != 0:
      # take the last, most recently added item in Stack 1 and add it to stack 2
      self.stack2.append(self.stack1[-1])
      # Remove that last item from stack 1
      self.stack1.pop()

    # Push the new item into stack 1
    self.stack1.push(newItem)

    # Move all items in stack 2 to stack 1
    while len(self.stack2) != 0:
      self.stack1.append(self.stack2[-1])
      self.stack2.pop()

  def dequeue(self):
    if len(self.stack1) == 0:
      print('Queue is empty')
      return False
    
    # return top of stack 1, which is the oldest item
    # remove it from the stack
    oldestItem = self.stack1[-1]
    self.stack1.pop()

    return oldestItem