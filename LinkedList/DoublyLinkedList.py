
class DoublyLList:
    """
    Doubly Linked List class for array items and nodes are connected in both directions
    """
    def __init__(self, value: any) -> None:
        self.head = self
        self.data = value
        self.tail = self.head
        self.next = None
        self.prev = None
        self.length = 1
    
    def append(self, value: any) -> None:
        """Add item at end"""
        new_node = DoublyLList(value)
        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = self.head            
        self.length += 1

    def prepend(self, value: any) -> None:
        """Add item at beginning"""
        new_node = DoublyLList(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index: int, value: any) -> None:
        """
        Insert item at given position
        if index 0 or negative number, add element at beginning
        if index greater then size of list, add at end of list
        """
        if index <= 0: #if index 0 or negative number, add element at beginning
            self.prepend(value)
        elif index >= self.length - 1: #if index greater then size of list, add at end of list
            self.append(value)
        else:
            new_node = DoublyLList(value)
            mid = self.length//2
            if index <= mid: #insert left side half
                tmp_pos: int = 0
                curr_node = self.head
                prev_node = self.head
                while curr_node:
                    if tmp_pos == index:
                        break    
                    prev_node = curr_node
                    curr_node = curr_node.next
                    tmp_pos += 1
            else: #insert right side half
                tmp_pos: int = self.length - 1
                curr_node = self.tail
                prev_node = self.tail
                while curr_node:
                    if tmp_pos == index:
                        break   
                    curr_node = curr_node.prev
                    prev_node = curr_node.prev
                    tmp_pos -= 1
            new_node.prev = prev_node       #assign new node's prev = previous node next (index-1)
            new_node.next = curr_node       #assign new node's next = current node next (index)
            prev_node.next = new_node       #assign previous node next (index-1) = new node
            curr_node.prev = new_node       #assign current node next (index) = new node
            self.length += 1                #increment the length

    def update(self, index: int, value: any) -> None:
        """
        Change the value at given index position and return error if index not found
        """
        if 0 < index > self.length - 1 or self.length == 0:
            raise IndexError(f"Index {index} out of range, <size: (0, {self.length-1})>!")
        if index == 0:
            self.head.data = value
            return
        elif index == self.length - 1:
            self.tail.data = value
            return
        mid = self.length//2
        if index <= mid:
            tmp_pos = 0
            curr_node = self.head
            while curr_node:        #loop the nodes one by one up-to given index
                if tmp_pos == index:  
                    curr_node.data = value      #set node value
                    break                       #break the loop if index matched, no need to check remaining elements
                curr_node = curr_node.next
                tmp_pos += 1
        else:
            tmp_pos = self.length - 1 
            curr_node = self.tail
            while curr_node:        #loop the nodes one by one up-to given index
                if tmp_pos == index:                
                    curr_node.data = value      #set node value
                    break                       #break the loop if index matched, no need to check remaining elements
                curr_node = curr_node.prev        
                tmp_pos -= 1

    def search(self, target: any) -> int:
        """
        Search the item and return index position
        return -1 if value not found
        """        
        if self.head and self.head.data == target:
            return 0
        elif self.tail and self.tail.data == target:
            return self.length - 1
        curr_node = self.head
        tmp_pos = 0
        while curr_node:
            if curr_node.data == target:
                return tmp_pos
            curr_node = curr_node.next
            tmp_pos += 1
        return -1
        
    def find(self, index: int) -> any:
        """Return item at given index position
            Error will raise if index not found
        """
        if 0 < index > self.length - 1:
            raise IndexError(f"Index {index} out of range, <size: (0, {self.length - 1})>")
        mid = self.length//2
        if index <= mid:
            curr_node = self.head
            tmp_pos: int = 0
            while curr_node:
                if tmp_pos == index:
                    return curr_node.data
                tmp_pos += 1
                curr_node = curr_node.next
        else:
            curr_node = self.tail
            tmp_pos: int = self.length - 1
            while curr_node:
                if tmp_pos == index:
                    return curr_node.data
                tmp_pos -= 1
                curr_node = curr_node.prev

    def pop(self, index: int = None) -> any:
        """Remove the item from the list and return the value
            By default last item removed, if index given respective item will be removed
        """
        index = index if index != None else self.length - 1 #set default index as last
        if 0 < index > self.length - 1 or self.length == 0:
            raise IndexError(f"Index {index} out of range, <size: (0, {self.length-1})>!")
        pop_item: any = ""
        if index == 0:  #if index is head item
            pop_item = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.length -1: #if index is tail item
            pop_item = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            mid = self.length//2
            tmp_pos = 0
            if index >= mid: #if index present right side half, loop from head
                tmp_pos = self.length - 1
                curr_node = self.tail
                while curr_node:
                    if tmp_pos == index:
                        break
                    tmp_pos -= 1
                    curr_node = curr_node.prev
            else: #if index present left side half, loop from tail
                curr_node = self.head
                while curr_node:
                    if tmp_pos == index:
                        break
                    tmp_pos += 1
                    curr_node = curr_node.next
            pop_item = curr_node.data
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        self.length -= 1
        return pop_item

    def remove(self, target: any) -> int:
        """Remove given element from the list and return position of the deleted item
            -1 will return if target item not found in the list"""
        if self.head and self.head.data == target:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.length -= 1
            return 0
        elif self.tail and self.tail.data == target:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            self.length -= 1
            return self.length
        curr_node = self.head
        tmp_pos: int = 0
        while curr_node:
            if curr_node.data == target:
                curr_node.prev.next = curr_node.next    #assign target prev node next = target next node
                curr_node.next.prev = curr_node.prev    #assign target next node prev = target prev node
                self.length -= 1
                return tmp_pos
            curr_node = curr_node.next
            tmp_pos += 1
        return -1

    def display(self) -> None:
        """Show the items in the list for debugging"""
        curr_node = self.head
        print(f"<DoublyLList <size: {self.length}>>", end=" ")
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

    def clear(self) -> None:
        """Clear the list and set head and tail as None"""
        self.head = None
        self.tail = self.head
        self.length = 0

    def __iter__(self):
        self.iter_node = self.head
        return self
    
    def __next__(self) -> any:
        if self.iter_node:
            node_data = self.iter_node.data
            self.iter_node = self.iter_node.next
            return node_data
        else:
            raise StopIteration("reached at end position")

    def __str__(self) -> str:
        curr_node = self.head
        str_list = []
        while curr_node:
            str_list.append(curr_node.data)
            curr_node = curr_node.next
        return f"{str_list}"
