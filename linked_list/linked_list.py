#Singly Linked List
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    
  def traverse(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

  def append(self, data):
    new_node = Node(data)
    if self.tail is None:
      self.tail = new_node
      self.head = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def find(self, target):
    current = self.head
    while current is not None:
      if current.data == target:
        return current
      current = current.next
    return None
  
  def remove(self, target):
    if self.head is None:
      return "List is empty!"
    
    if self.head.data == target:
      if self.head is self.tail:
        self.head = None
        self.tail = None
      else: 
        self.head = self.head.next
      return f"Removed {target}"
    
    current = self.head
    while current.next is not None:
      if current.next.data == target:
        if current.next is self.tail:
          self.tail = current
        
        current.next = current.next.next
        return f"Removed {target}"
      
      current = current.next
    return None


###
my_list = LinkedList()
my_list.append("🍬")
my_list.append("🧸")
my_list.append("🍪")
my_list.append("🍩")

print("Initial list:")
my_list.traverse()

print("\nRemove middle (🧸):")
print(my_list.remove("🧸"))
my_list.traverse()

print("\nRemove head (🍬):")
print(my_list.remove("🍬"))
my_list.traverse()

print("\nRemove tail (🍩):")
print(my_list.remove("🍩"))
my_list.traverse()
print(f"Tail is now: {my_list.tail.data if my_list.tail else None}")

print("\nRemove last remaining (🍪):")
print(my_list.remove("🍪"))
my_list.traverse()
print(f"Head: {my_list.head}, Tail: {my_list.tail}")

print("\nRemove from empty list:")
print(my_list.remove("🍕"))

print("\nRemove non-existent from non-empty:")
my_list.append("a")
my_list.append("b")
print(my_list.remove("zzz"))   # this is the one that was looping forever!
my_list.traverse()