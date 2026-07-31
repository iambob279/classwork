class Node:
    def __init__ (self, name):  # creates new node with data and next being None
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
        p.next = new_node # new_node.next is set to None when created


def print_list():
    p=start
    if start is None: # list is empty
        print ("Empty List")
        return
    #Go through list till find end
    print("List Items :")
    while not (p is None):
        print(p.name, end=" ") # move to next item
        p = p.next # move to next item
    print("") # end of line
    
def count_list():
    p=start
    count=0
    #Go through list till end
    while not (p is None):
        count +=1
        p = p.next # move to next item
    return count

def delete_item_by_name(name_to_delete):
    global start

    if start is None: # list was empty
        print("List empty")
        return

    #look for node where name is held
    p=start
    last_p=None
    #Go through list till find end
    while not (p.next is None) and p.name!= name_to_delete:
        last_p = p  #keep a record of node pointing to it
        p=p.next # move to next item
        # p nows points at node to be deleted
   
    if p.name!= name_to_delete:  # name wasn't found
        print ("name not found")
        return
    
    if p == start: #delete first item
        start = start.next  # start will now be item after
    else:
        last_p.next = p.next  #chain now bypasses deleted item (p)


def main():
    global start
    
    start = None

    while True:
        print("Enter 1 to add data to end , 2 to delete data, 3 to print list, 4 to quit")
        choice=int(input("Enter option: "))

        if choice == 1:
            name=input("Enter Data for list or hit <enter> key to stop: ")

            while name!="":
                add_item_at_end(name)
                name=input("Enter Data for list or hit <enter> key to stop: ")

        elif choice == 2:
            name=input("Enter data to delete or hit <enter> key to stop: ")

            while name!="":
                delete_item_by_name(name)
                name=input("Enter data to delete or hit <enter> key to stop: ")

        elif choice == 3:
            print_list()
            print ("list has", count_list(), "elements")

        elif choice == 4:
            break
            
main()