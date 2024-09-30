# This is very simple implementaion of Data Structure like Stack and Singly Linked List

## Main Data Structures collections:- <br> Stack, Singly LinkedList, Doubly LinkedList, SinglyCirclular LinkedList, DoublyCircular LinkedList.

* In Stack you can use many methods.

    ```python
    1) push(val) #provide any valu as argument to push into stack
    2) pop() #It will pop or delete the top element of stack
    3) peek() #It will give you the top element
    4) isEmpty() #It will tell you whether the stack is empty or not
    5) printStack() #It will print the stack in form of list
    ```
<h3><b>Note:- if you initialize the stack size to 5 and you push only 3 element or less then 5 element then rest of the stack will print as 0 because initially all the value in stack is 0.</b></h3>
---

## In linked list I implement singly, doubly, singlyCircular.

* In Singly Linked List you can use so many methods, here is the list:-

  
    ```python
        1) len()
        2) is_empty() #Make sure you use this method inside the print function
        3) traverse() #To print the linked list
        4) insertAtHead(val) #Provide any value as argument
        5) insertAtTail(val) #Provide any value as argument
        6) insertAtPos(val, pos) #First provide the value and then position
        7) deleteHead() #It will delete the head node
        8) deleteTail() #It will delete the tail node
        9) deleteAtPosition(pos) #Provide the position of node you want to delete
        10) insertAfter(val, newVal) #First provide the value after which you want to add a new value. E.g:- after 5 you want to add 6 then insertAfter(5, 6)
        11) insertBefore(val, newVal) #First provide the value before which you want to add a new value. E.g:- before 5 you want to add 6 then insertBefore(5, 6)
        12) mergeTwoLL(l1, l2) #Give two arguments. The first argument is the first linked list and second argument is second linked list
        13) get_tail() #It will print the tail node
        14) get_head() #It will print the head node
    ```

# Here is the exmaple 

<h2><b>Stack</b></h2>
    
```python
     from DScollection import *

    #OR
    # from DScollection import Stack
    # from DScollection import SinglyLL

    s1 = Stack(5) #here 5 is the size of stack
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.push(5)
    #you can also use loop to push to avoid this number of lines
    s1.pop()
    s1.peek()
    s1.isEmpty()
    s1.printStack()
```
<h2><b>Singly Linked List</b></h2>
    
```python
    from DScollection import *

    #OR
    # from DScollection import Stack
    # from DScollection import SinglyLL

    l1 = SinglyLL()
    l2 = SinglyLL()

    l1.insertAtTail(1)
    l1.insertAtTail(2)
    l1.insertAtTail(3)
    l1.traverse()

    l2.insertAtTail(4)
    l2.insertAtTail(5)
    l2.insertAtTail(6)
    l2.traverse()

    merged_list = SinglyLL()
    merged_list.mergeTwoLL(l1, l2)

    merged_list.traverse()
    len(merged_list)
```

# I will update this with all the data structure with ready to use, stay updated.