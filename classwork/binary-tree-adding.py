class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def __str__(self): # return nice value when call to print
        return str(self.data)

# add_to_tree method to create nodes
def add_to_tree(current_node, data):

    if current_node.data is None:
        current_node.data = data
    else:
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                add_to_tree(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                add_to_tree(current_node.right, data)
           

def dump_tree (current_node):
    if current_node is not None:
        print ('Data:', current_node.data, ' Left:', current_node.left, ' Right:', current_node.right)
        dump_tree(current_node.left)
        dump_tree(current_node.right)

def find_val(name, current_node): #always returns true
    if name == current_node.data or current_node.left or current_node.right:
        return True
    else:
        return False
        
def main():

    root = None # tree empty

    while True:

        choice = int(input ("""
1 to add data to tree
2 to dump tree structure
3 to check value
99 to quit: """))

        if choice==1:
            data_for_tree=input("Enter item for tree (or hit enter to stop): ")

            while data_for_tree!="":
                if root is None: # create root
                    root = Node(data_for_tree)
                else:
                    add_to_tree(root, data_for_tree)
                data_for_tree=input("Enter item for tree (or hit enter to stop): ")
        elif choice == 2:
            dump_tree (root)
        elif choice == 3:
            name = input("What are you searching for?\n")
            print(find_val(name, root))
        elif choice == 99:
            break
        
main()