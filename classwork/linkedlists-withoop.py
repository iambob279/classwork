class Node:
    def __init__ (self, name):
        self.name = name
        self.next = None
        


def add_item_at_end(new_name):
    global start

    if start == None: # list was empty
        start= Node(new_name)
    else:
        p=start
        #Go through list till find end
        while not (p.next is None):
            p = p.next # move to next item
       # p nows points at place new name should go after
        new_node = Node(new_name)
        p.next = new_node


def print_list():
    global start
    count = 0
    p=start
    print ("List Contents: ", end= ' ')
    #Go through list till find end
    while not (p is None):
        print(p.name, end= ' ') # move to next item
        p = p.next # move to next item
        count = count + 1
    print('')
    print(count)

def main():
    global start
    
    start = None
    name=input("Enter Data for list (or just hit <Enter> if finished): ")

    while name!="":
        add_item_at_end(name)
        name=input("Enter Data for list (or just hit <Enter> if finished): ")

    print_list()

main()