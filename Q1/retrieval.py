# @file Retrieval.py
# @Author Chanakya Sharma
#  @description:-
#               Implements LRU algorithm to cache data
#                   - Uses LinkedNode Data Structure
#                   - LinkedNode is Used in LeastRecentlyUsed class
#               Wrapper function simulates and interacts with the functions of classes
#               test databases have been established and simulations achieved with sql function
# 
#  @bugs:-
#               - Capacity hold is untested may or may not produce error
# 
#  @compilation and runtime:-
#               use the following commmand ```python3 retrieval.py```
# 
#  This program was written on Apple M1 ARM architecture and has not been used on x86 architectures for testing

# 


# Q1 [C, Python] Assume we have a function get_book_info(isbn)
# that takes a string ISBN argument and
# retrieves an object containing the Title, Author, and Language of a book
#   (each represented as a string) that
# takes a nontrivial amount of time to run (perhaps because it’s making a call to a database).
# Write a wrapper function that increases performance by keeping results in memory for the quick lookup.
# To prevent memory from growing unbounded, we only want to store a maximum of N book records.
# At any given time, we should be storing the N books that we accessed most recently.
# Assume that N can be a large number when choosing data structure(s) and algorithm(s).

# FAKE DATABASE

db = {
    "0000000001": {"isbn": "0000000001", "author": "mariah", "language": "English"},
    "0000000011": {"isbn": "0000000011", "author": "cage", "language": "English"},
    "0000000101": {"isbn": "0000000101", "author": "Bruh", "language": "English"},
    "0000000111": {"isbn": "0000000111", "author": "sherlock", "language": "English"},
    "0000001111": {"isbn": "0000001111", "author": "conan", "language": "English"},
    "0000233001": {"isbn": "0000233001", "author": "nick", "language": "English"},
    "0000023401": {"isbn": "0000023401", "author": "trevor", "language": "English"},
    "0001200001": {"isbn": "0001200001", "author": "lopex", "language": "English"},
    "0007850001": {"isbn": "0007850001", "author": "axis", "language": "English"},
    "0012350001": {"isbn": "0012350001", "author": "ape", "language": "English"},
    "0078930001": {"isbn": "0078930001", "author": "jardin", "language": "English"},
    "0009999001": {"isbn": "0009999001", "author": "alpeno", "language": "English"},
    "0088888001": {"isbn": "0088888001", "author": "alpine", "language": "English"},
    "0009860001": {"isbn": "0009860001", "author": "carlos", "language": "English"},
    "6660000001": {"isbn": "6660000001", "author": "celia", "language": "English"},
    "1230000001": {"isbn": "1230000001", "author": "tata", "language": "English"},
    "3210000001": {"isbn": "3210000001", "author": "montana", "language": "English"},
    "7650000001": {"isbn": "7650000001", "author": "creatine", "language": "English"},
    "5670000001": {"isbn": "5670000001", "author": "protein", "language": "English"},
    "1230035001": {"isbn": "1230035001", "author": "losstboi", "language": "English"},
    "3567030001": {"isbn": "3567030001", "author": "rock", "language": "English"},
    "0345678901": {"isbn": "0345678901", "author": "dwayne", "language": "English"},
}

# GLOBAL VALUES
N = 3
# N is the maximum capacity of the list can be changed and does not effect the code

# format {isbn:{isbn and all details}}
cache = {}
    # This holds all the data for quick retrieval
    # Should be configured as a Dictionary for O(1) for lookup

class LinkedNode(object):
    # This the basic data Structure for Caching with Doubly Linked List
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LeastRecentlyUsed():
    # Class Implements Least Recenetly Used Algorithm
    def __init__(self):
        self.head = None  # head is the least recent
        self.tail = None  # tail is the most recent
        self.capacity = 0  # Current Capacity is the length of the list

    # Removes the head and makes appropriate connections in the doubly linked list
    def remove_head_node(self):
        if not self.head:
            return
        prev = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del prev
        self.capacity = self.capacity-1

    # Add a new node at tail and makes appropriate connections in the list
    def append_new_node(self, new_node):
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
        self.capacity = self.capacity + 1

    # Deletes the link of current node to add that node to tail again
    def unlink_cur_node(self, node):
        if self.head is node:
            self.head = node.next
            if node.next:
                node.next.prev = None
            return
        # removing the node from somewhere in the middle; update pointers
        prev, nex = node.prev, node.next
        prev.next = nex
        nex.prev = prev

    # raises a get request from cache and updates the doubly linked list
    def get(self, key):
        if key not in cache:
            return -1
        node = cache[key]
        if node is not self.tail:
            self.unlink_cur_node(node)
            self.append_new_node(node)
        return node

    # raises a put request to cache and updates the doubly linked list
    def put(self, key):
        if len(cache) == self.capacity:
            # remove head node and correspond key
            self.remove_head_node()
        # add new node and hash key
        new_node = LinkedNode(key)
        cache[key] = new_node
        self.append_new_node(new_node)

Agent = LeastRecentlyUsed()
# Agent Object to implement LRU Algorithm

# Independent function to simulates calls to the database
def sql(str):
    if str in db:
        return db[str]
    else:
        print("Not found")
        return -1

# Wrapper function makes appropriate calls to Database and cache
# Logic Implemented in LRU Class
def wrapper(isbn):
    if isbn in cache:
        return Agent.get(isbn) 
    else:
        x = sql(isbn)
        if x == -1:
            print("DB-Error:::Not in DatBase")
        else:
            Agent.put(isbn)
        return x

# Please Use your test main function after this

print(wrapper("0000000001"))
print(wrapper("0000000011"))
print(wrapper("0000000101"))
print(wrapper("0000000111"))
print("\n\n\n\n\n\n")
print(cache)