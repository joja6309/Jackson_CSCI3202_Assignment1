import Queue
import random




# Stack Question 2.
class Stack:
   
	def __init__(self):
		self.items = []
	
	
	def push(self, item):
		self.items.append(item)
							
	def pop(self):
		return self.items.pop()
									
									
	def checkSize(self):
		return len(self.items)
# Binary Tree Questoin 3.
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.parent = None
		self.integer_key = key
class BinaryTree:
	def __init__(self):
		self.root = None
	def add(self,value,parent_value):
		if (self.root == None):
			rootNode = Node(value)
			self.root = rootNode
			print "Root added"

		else:
			current = self.root
			while 1:
				
				if (current.integer_key == parent_value):
					if (current.left and current.right):
						print "Parent has two children"
						break
					
		
					elif (not(current.left) and not(current.right)):
						newNode = Node(value)
						current.left = newNode
						newNode.parent = current
						print "added"
						print newNode.integer_key
						break
					
					elif (current.left):
						newNode = Node(value)
						current.right = newNode
						newNode.parent = current
						print "added"
						print newNode.integer_key
						break
						
				else:
					print
					if parent_value < current.integer_key:
						if current.left:
						   current = current.left
						elif current.right:
							 current = current.right
					elif parent_value > current.integer_key:
						if current.right:
						   current = current.right
						elif current.left:
							 current = current.left
						else:
							print "Parent not found"
							break
	def delete(self, value):
		 current = self.root
		 
		 while 1:


			if current.integer_key != value:
				if value < current.integer_key:
					if current.left:
					   current = current.left
					elif current.right:
						 current = current.right
					else:
						print "Node not found"
						break
				elif value > current.integer_key:
					if current.right:
					   current = current.right
					elif current.left:
						 current = current.left
					else:
						 print "Node not found"
						 break
			elif (not(current.left) and not(current.right)):
			 
			 if (current == current.parent.left):
					current.parent.left = None
			 elif (current == current.parent.right):
					current.parent.right = None
				
			 current.parent = None
				
			 print "Deleting"
			 print current.integer_key
			 del current
			 break
			else:
				print "Node not deleted, has children"
				break


	def preorder(self,node):
			current = node
			if current is not None:
				 print "Current Node:"
				 print current.integer_key
				 print "----------------"
				 if current.left:
					print"Left kid"
					print current.left.integer_key
				 elif current.right:
					print"Right kid"
					print current.right.integer_key
				 self.preorder(current.left)
				 self.preorder(current.right)
# Graph Question 4.
# Using Weighted Graph from another course 
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def addVertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def findVertex(self, n):
        if n in self.vert_dict:
        	
            return self.vert_dict[n]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


# Question 5 - Testing
# Part A (Queue)
q = Queue.Queue()
for i in range(10):
	print i
	print "Added to the Queue"
q.put(i)
while not q.empty():
	print q.get()
# Part B (Stack)
s = Stack()
for i in range (10):
	s.push(i)
while (s.checkSize() !=	 0):
	print s.pop()
# Part C (Binary Tree) 
B_Tree = BinaryTree()
B_Tree.add(9,0)
B_Tree.add(7,9)
B_Tree.add(8,7)
B_Tree.add(10,9)
B_Tree.add(12,10)
B_Tree.add(11,12)
B_Tree.add(13,12)
B_Tree.add(1,7)
B_Tree.add(24,13)
B_Tree.add(25,24)
rootNode = B_Tree.root
B_Tree.preorder(rootNode)
B_Tree.delete(25)
B_Tree.delete(24)
B_Tree.preorder(rootNode)
# Part D (Graph)
dict = {} 
the_graph = Graph()
for i in range(11): 
	the_graph.addVertex(i)
	print "Adding Vertex: "
	print i 
for x in range(21): 
	random_x = random.randrange(0,10)
	random_y = random.randrange(0,10)
	print random_x 
	print random_y 
	the_graph.addEdge(random_x,random_y)


	for t in range(6): 
		print "Seaching for " 
		print t 
		print the_graph.findVertex(t)





