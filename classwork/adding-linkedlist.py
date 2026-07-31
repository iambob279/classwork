def add_item_at_end(new_name):
    global start, nextfree, Names

    #check if list is full and if so, print error message
    if nextfree == -1:
        print("List full")
        return

    if start == -1: # list was empty
        start= nextfree #move entry from free list to start
        nextfree= Names[nextfree][1] # save where the next entry in the free list
        Names[start][0] = new_name #[0] is data, [1] pointer to next item
        Names[start][1] = -1 #only one item in list
    else:
        p=start
        #Go through list till find end
        while Names[p][1] != -1:
            p = Names[p][1] # move to next item
       # p nows points at place new name should go after
        new_place = nextfree     # save current free list head, this is where new data will go
        nextfree = Names[nextfree][1] # move nextfree to next item in free list
        Names [p][1] = new_place      ## p now points to new item
        Names[new_place][0] = new_name #[0] is data, [1] pointer to next item
        Names[new_place][1] = -1 ## new item now at end of list

def main():
    global start, nextfree, Names
    Names=[]
    count = 0
    for i in range(20): # creates 20 rows of 2 columns - 2D array - makes a list of Lists
        Names.append(['',i+1]) # each row points to the next one
    Names[-1][1] = -1 #last row 

    start = -1   #Nothing in list when created
    nextfree = 0  # all table slots start off in free list

    name=input("Enter Data for list or just hit <enter> to finish: ")

    while name!="":
        add_item_at_end(name)
        name=input("Enter Data for list or just hit <enter> to finish: ")

    print (f"start = {start}, nextfree = {nextfree}")

    for n in Names:
        print (n)

    for i in Names:
        count += 1
    print(count)
main()