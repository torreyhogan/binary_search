#! python3.6
# binary search in python

class Node:
	def __init__(self,value_v):
		self.value = value_v
		self.parent = None
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.arr = None
		self.head = None
		self.hash_store = {}

	def build_tree(self):
		self.head = Node(self.arr[0])
		node = self.head
		print(self.head.value)
		insert_level(node,0)

	def insert_level(self,node,i):
		if i == 0:
			node.left = insert_level(node, int(2 * i + 1))
			node.left.parent = node
			node.right = insert_level(node, int(2 * i + 2))
			node.right.parent = node 
		elif i < len(self.arr):
			node = Node(self.arr[i])
			node.left = insert_level(node, int(2 * i +1))
			if node.left != None:
				node.left.parent = node 
			node.right = insert_level(node, int(2*i + 2))
			if node.right != None:
				node.right.parent = node 
		else:
			return None

		return node 

	def print_tree(self):
		self.hash_store.setdefault(1,None)
		self.hash_store[1] = self.head.value
		# node_print(self.head, 2)

	def node_print(self,node,level):
		if node.left == None and node.right == None:
			return
		elif node.right == None:
			self.hash_store.setdefault(level,[])
			hash_store[level].append(node.left.value)
		else:
			self.hash_store.setdefault(level,[])
			self.hash_store.append([node.left.value,node.right.value])
			node_print(node.left,int(level + 1))
			node_print(node.right,int(level+1))



tree = Tree()
tree.arr = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
tree.build_tree()
tree.print_tree()
print(tree.hash_store)






