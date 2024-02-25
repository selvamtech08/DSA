class SingleLList:
    """Single LinkedList class for list of items"""
    def __init__(self, data) -> None:
        self.data = data
        self.head = self
        self.next = None
        self.length = 1

    def append(self, value: any) -> None:
        """Insert element at end of the list"""
        new_node = SingleLList(value) #create new node 
        if self.head:
            curr_node = self.head
            while curr_node.next:       #loop to find-out end position for append an item            
                curr_node = curr_node.next
            curr_node.next = new_node
        else:                           #if list is empty assign new node as head
            self.head = new_node 
        self.length += 1                #increment the length by 1
    
    def prepend(self, value: any) -> None:
        """Inserting element at beginning"""
        new_node = SingleLList(value)       #create new node
        new_node.next = self.head           #assign next pointer to head node
        self.head = new_node                #change new node as head, because inserted as 0 index
        self.length += 1                    #increment the length by 1
    
    def insert(self, pos: int, value: any) -> None:
        """Inserting element at given position
            if position is 0 < pos or pos > length elements will be added beginning or end respectively
        """
        new_node = SingleLList(value)    #create new node
        if pos <= 0:                    #if index given in negative 
            self.prepend(value)
        elif pos > self.length - 1:     #if given index greater then max length, pos will set as max length
            self.append(value)
        else:
            init_pos: int = 0
            curr_node = self.head
            prev_node = self.head
            while curr_node:                #iter the nodes one by one
                if init_pos == pos:         #break the loop if reached the index
                    break
                prev_node = curr_node       #store previous node at given index
                curr_node = curr_node.next  #store next node at given index
                init_pos += 1            
            new_node.next = curr_node       #assign new node next to current index node
            prev_node.next = new_node       #reassign previous node next to new node (current node already linked to new node in previous line)
            self.length += 1

    def display(self) -> None:
        """show all the elements in the list - only Debug prupose"""
        curr_node = self.head        
        print(f"<SingleLList <size: {self.length}>>: ", end=" ")
        while curr_node:            #iter the items and display
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

    def search(self, target: any) -> int:
        """Search given value in the list and return the index
            If value not exist return value will be -1
        """
        curr_node: SingleLList = self.head
        tmp_pos = 0
        while curr_node.next:               #iter the nodes
            if curr_node.data == target:    #if match found return the index position
                return tmp_pos
            curr_node = curr_node.next
            tmp_pos += 1
        return -1                           #return -1 if value not found
    
    def find(self, index: int) -> any:
        """Find the index position and return the value at index
           if index not found Exception will be raised
        """
        if 0 < index > self.length - 1:     #raise error if index not within available list range
            raise IndexError(f"Index out of range <size: {self.length}>")
        curr_node = self.head
        tmp_pos = 0
        while curr_node:                    #iter the nodes
            if tmp_pos == index:            #if index position is available return the value 
                return curr_node.data
            curr_node = curr_node.next
            tmp_pos += 1

    def pop(self, pos = None) -> any:
        pos = pos if pos != None else self.length - 1       #default value set as max length(i.e., last index)
        if not self.head:                                   #Error will raise if list is empty    
            raise IndexError(f"List is empty <size: {self.length}>, couldn't perform the operation!")
        elif pos > self.length - 1:                         #Error will raise if index out of range
            raise IndexError(f"Index `{pos}` out of range, <size: {self.length}>")
        elif pos == 0:                                      # if index a start position 
            temp = self.head.data
            self.head = self.head.next
            self.length -= 1
            return temp
        curr_node = self.head
        prev_node = self.head        
        ini_pos = 0
        while(ini_pos < pos):               #iter the node until reach given index 
            ini_pos += 1
            prev_node = curr_node
            curr_node = curr_node.next
        temp = prev_node.next.data          
        prev_node.next = curr_node.next     #drop the current node by assign previous next to current next
        self.length -= 1
        return temp

    def remove(self, target: any) -> int:
        """Remove given element from the list and return position of the deleteted item
            -1 will return if target item not found in the list"""
        if self.head and self.head.data == target:
            self.head = self.head.next
            self.length -= 1
            return 0
        curr_node = self.head
        prev_node = self.head
        target_pos = -1
        while curr_node:                    #iter the node until reach the target value
            target_pos += 1     
            if curr_node.data == target:    #break the loop if match found
                break
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node:
            prev_node.next = curr_node.next     #drop the node(match value position) and assign previous next to drop node next
            self.length -= 1
            return target_pos               #return the index position 
        return -1                           #false return if match not found 

    def __iter__(self):
        self.iter_node = self.head #node for iteration
        return self
    
    def __next__(self):     #iter implemented 
        if self.iter_node: 
            node_data = self.iter_node.data         #fetch current node value and used where it implement the loop iteration 
            self.iter_node = self.iter_node.next    #move current node position to next point node
            return node_data            
        raise StopIteration("reached at list end!")

    def __str__(self) -> str:
        curr_node = self.head
        linklist  = []
        while curr_node:
            linklist.append(curr_node.data)
            curr_node = curr_node.next
        return f"{linklist}"