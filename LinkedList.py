class node:
    def __init__(self,d):
        self.data=d
        self.nextt=None
class sll:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,"==>",end="")
            temp=temp.nextt
        print("None")
    def insert_beg(self):
        print("Enter the value node")
        data=input()
        temp=node(data)
        if(self.head!=None):
            temp.nextt=self.head
            self.head=temp
        else:
            self.head=temp
        obj.printlist()
    def insert_mid(self):
        print("Enter the vlue of node")
        data=input()
        print("Enter the position of node")
        pos=int(input())
        temp1=node(data)
        temp=self.head
        c=1
        while(c!=(pos-1)):
            temp=temp.nextt
            c+=1
        temp1.nextt=temp.nextt
        temp.nextt=temp1
        obj.printlist()
    def insert_last(self):
        print("Enter the vlue of node")
        data=input()
        temp1=node(data)
        temp=self.head
        if(self.head!=None):
            while(temp.nextt!=None):
                temp=temp.nextt
            temp.nextt=temp1
        else:
            self.head=temp1
        obj.printlist()
    def delete_mid(self):
        print("Enter the position of node")
        pos=int(input())
        c=1 
        temp=self.head
        while(c!=(pos-1)):
            temp=temp.nextt
            c+=1
        temp1=temp.nextt
        temp1.nextt=temp.nextt
        temp.nextt=None
        obj.printlist()
    def delete_last(self):
        temp1=self.head
        temp2=temp1.nextt
        while(temp2.nextt!=None):
            temp2=temp2.nextt
            temp1.nextt=temp2
        temp1.nextt=None
        obj.printlist()
    def delete_beg(self):
        temp=self.head
        self.head=self.head.nextt
        temp.nextt=None
        obj.printlist()
obj=sll()
ch=0
while(ch!=8):
    print("Linked List Implementation\n","1.INSERTION AT BEGINNING 2.INSERTION AT MIDDLE 3.INSERTION AT END 4.DELETION AT BEGINNING 5.DELETION AT MIDDLE 6.DELETION AT END 7.DISPALY 8.EXIT")
    ch=int(input())
    if(ch==1):
        obj.insert_beg()
    elif(ch==7):
        obj.printlist()
    elif(ch==4):
        obj.delete_beg()
    elif(ch==2):
        obj.insert_mid()        
    elif(ch==5):
        obj.delete_mid()
    elif(ch==3):
        obj.insert_last()
    elif(ch==6):
        obj.delete_last()
