from tkinter import N


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def Print(self):
        if self.head is None:
            print("list is empty")
        else:
            n=self.head
            while n:
                print(n.data)
                n=n.next
    def add_Begin(self,data):  
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            if n is None:
                print("Not present")
                break
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node




LL1=LinkedList()
LL1.add_Begin(10) 
LL1.add_Begin(20)
LL1.add_after(3,10)
LL1.Print()

    