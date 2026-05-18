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

  def insert(self, data, index):
    new_node = Node(data)
    if index == 0:
      self.prepend(data)
      return
    
    current = self.head
    current_index = 0

    while current is not None and current_index < index - 1:
      current = current.next
      current_index += 1

    if current is None:
      return "Index out of bounds"
    
    new_node.next = current.next
    current.next = new_node

    if new_node.next is None:
      self.tail = new_node




def section(title):
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)

def show(my_list, label="List"):
    items = []
    current = my_list.head
    while current is not None:
        items.append(str(current.data))
        current = current.next
    print(f"{label}: [{' → '.join(items) if items else 'empty'}]")
    head_data = my_list.head.data if my_list.head else None
    tail_data = my_list.tail.data if my_list.tail else None
    print(f"  head={head_data}, tail={tail_data}")


# ──────────────────────────────────────────────
section("PREPEND TESTS")

ll = LinkedList()
show(ll, "Empty")

ll.prepend("a")
show(ll, "After prepend('a')")   # [a], head=a, tail=a

ll.prepend("b")
show(ll, "After prepend('b')")   # [b → a], head=b, tail=a

ll.prepend("c")
show(ll, "After prepend('c')")   # [c → b → a], head=c, tail=a


# ──────────────────────────────────────────────
section("APPEND TESTS")

ll = LinkedList()
ll.append("a")
show(ll, "After append('a') to empty")   # [a], head=a, tail=a

ll.append("b")
ll.append("c")
show(ll, "After appending b, c")         # [a → b → c], head=a, tail=c


# ──────────────────────────────────────────────
section("FIND TESTS")

ll = LinkedList()
ll.append("🍬")
ll.append("🧸")
ll.append("🍪")

result = ll.find("🧸")
print(f"find('🧸')      → {result.data if result else None}   (expected: 🧸)")

result = ll.find("🍕")
print(f"find('🍕')      → {result}                  (expected: None)")

empty = LinkedList()
result = empty.find("anything")
print(f"find on empty   → {result}                  (expected: None)")


# ──────────────────────────────────────────────
section("REMOVE TESTS")

ll = LinkedList()
ll.append("🍬")
ll.append("🧸")
ll.append("🍪")
ll.append("🍩")
show(ll, "Initial")

print(f"\nremove('🧸') (middle): {ll.remove('🧸')}")
show(ll)   # [🍬 → 🍪 → 🍩], head=🍬, tail=🍩

print(f"\nremove('🍬') (head): {ll.remove('🍬')}")
show(ll)   # [🍪 → 🍩], head=🍪, tail=🍩

print(f"\nremove('🍩') (tail): {ll.remove('🍩')}")
show(ll)   # [🍪], head=🍪, tail=🍪    ← critical: tail must update!

print(f"\nremove('🍪') (last remaining): {ll.remove('🍪')}")
show(ll)   # empty, head=None, tail=None    ← both must be None

print(f"\nremove('anything') on empty: {ll.remove('anything')}")
show(ll)   # still empty

print("\nremove non-existent from non-empty:")
ll.append("x")
ll.append("y")
print(f"  remove('zzz'): {ll.remove('zzz')}")    # None (not found)
show(ll)   # [x → y] unchanged


# ──────────────────────────────────────────────
section("INSERT TESTS")

ll = LinkedList()
ll.append("a")
ll.append("b")
ll.append("c")
show(ll, "Initial")

print("\ninsert('FRONT', 0):")
ll.insert("FRONT", 0)
show(ll)   # [FRONT → a → b → c]

print("\ninsert('MID', 2):")
ll.insert("MID", 2)
show(ll)   # [FRONT → a → MID → b → c]

print("\ninsert('END', 5):")
ll.insert("END", 5)
show(ll)   # [FRONT → a → MID → b → c → END], tail=END  ← tail must update!

print(f"\ninsert('oops', 99): {ll.insert('oops', 99)}")
show(ll)   # unchanged, error message returned

print("\ninsert into empty list at index 0:")
empty = LinkedList()
empty.insert("only", 0)
show(empty)   # [only], head=only, tail=only


# ──────────────────────────────────────────────
section("INTEGRATION TEST (mix of operations)")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.insert(99, 2)
show(ll, "After mixed ops")   # [0 → 1 → 99 → 2 → 3]

ll.remove(99)
ll.remove(0)
ll.remove(3)
show(ll, "After removals")    # [1 → 2], head=1, tail=2

found = ll.find(2)
print(f"\nfind(2) → {found.data if found else None}   (expected: 2)")


# ──────────────────────────────────────────────
section("ALL TESTS COMPLETE")