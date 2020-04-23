# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
import sys

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next
  
  def __str__(self):
    return f"Node: {self.value}, prev: {self.prev}, next: {self.next}"

  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __str__(self):
    return f"head: {self.head}, tail: {self.tail}, length: {self.length}"
    
  def __len__(self):
    return self.length

  def add_to_head(self, value):
    newNode = ListNode(value, None, None)
    self.length += 1
    if not self.head and not self.tail:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
    return newNode.value

  def remove_from_head(self):
    value = self.head.value
    self.delete(self.head)
    return value

  def add_to_tail(self, value):
    newNode = ListNode(value, None, None)
    self.length += 1
    if not self.head and not self.tail:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = newNode
    return newNode.value

  def remove_from_tail(self):
    value = self.tail.value
    self.delete(self.tail)
    return value

  def move_to_front(self, node):
    if self.head is node:
      return self.head.value
    value = node.value
    if self.tail is node:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1
    return self.add_to_head(value)

  def move_to_end(self, node):
    if self.tail is node:
      return 
    value = node.value
    if node is self.head:
      self.remove_from_head()
    else:
      node.delete()
      self.length -= 1

    self.add_to_tail(value)
    return value

  def delete(self, node):
    if not self.head and not self.tail:
      return False
    self.length -= 1
    if self.head is self.tail:
      self.head = None
      self.tail = None
    elif self.head is node:
      self.head = node.next
      node.delete()
    elif self.tail is node:
      self.tail = node.prev
      node.delete()
    else:
      node.delete()
      
  def get_max(self):
    if not self.head:
      return None
    node = self.head
    maxVal = node.value
    while node:
      if node.value > maxVal:
        maxVal = node.value
      node = node.next
    return maxVal

class Stack:
  def __init__(self):
    self.size = 0
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.storage.add_to_tail(value)
    self.size = self.storage.length

  def pop(self):
    value = None
    if self.size > 0:
      value = self.storage.remove_from_tail()
      self.size = self.storage.length
    return value

  def peek(self):
    return self.storage.tail.value

  def len(self):
    return self.size

class Queue:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, newItem):
    # Move all elements from stack1 to stack2  
    while self.stack1.len() != 0:  
      # Take the the last, most recently added item in Stack 1, and add it to Stack 2
      self.stack2.push(self.stack1.peek())
      # Remove that item from stack 1
      self.stack1.pop()

    # Push new item into Stack1
    self.stack1.push(newItem)

    #self.stack1.storage.add_to_head(newItem)

    # Push everything back to stack1  
    while self.stack2.len() != 0:  
      self.stack1.push(self.stack2.peek())  
      self.stack2.pop()

  # Dequeue an item from the queue  
  def dequeue(self):
    # if Stack1 is empty
    if self.stack1.len() == 0:
      print("Q is Empty")
    # Return top of Stack1 => oldest element in the stack
    oldestItem = self.stack1.peek()
    # Remove it from the stack
    self.stack1.pop()
    return oldestItem


  def parse(self, instruction, value = None):
    # print('parse', instruction, value)
    if instruction == 1:
        self.enqueue(value)
    elif instruction == 2:
        self.dequeue()
    elif instruction == 3:
        print(self.stack1.peek())
    else:
        return value

q = Queue()
for line in sys.stdin:
    args = line.replace('\n', '').split(' ')
    instruction = args[0]
    value = args[1] if len(args) > 1 else -1
    q.parse(int(instruction), int(value))

