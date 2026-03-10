def create ():
    nm =input(" Enter your Name:")
    ad=input ("Enter your Address:")
    cn=input("Enter your Contact No:")
    DE=input ("Enter your amount you deposited:")
    ac=input ("enter your account no") 
    f=open("customer.txt","a")
    f.write(nm+"\t")
    f.write(ad+"\t")
    f.write(cn+"\n")
    f.write(DE+"\n")
    f.write(ac+"\t")
    print("Account Created Succesfully ")
    f.close()
def delete ():
    i=input("enter the account no  that you want to remove from file ")
    with open("customer.txt","r")as f:
        wh=f.readlines()
    with open("customer.txt","w")as f:
        for data in wh :
           d=data.split("\t",1)
           if(d[0]!=i):
              f.writelines(data)
    print("record deleted ")
def update():
    i=input("Enter the account no to be updated from file")
    with open("customer.txt","r")as f:
        all=f.readlines()
    with open("customer.txt","w")as f:
        for data in all:
            d=data.split("\t",1)
            if(d[0]==i):
                nn=input("new name")
                na=input("new address")
                f.writelines(d[0]+"\t"+nn+"\t"+na+"\n")
            else:
                f.writelines(data)
                print("record updated")            
def search():
    i=input("Enter the account no to be searched from file :")
    with open("customer.txt","r")as f:
        all=f.readlines()
        for data in all :
            d=data.split("\t",1)
            if(d[0]==i):
                print(data)
                
def show():
    f=open("customer.txt","r")
    print("name\t address\t contact\t deposit\t account no")
    print(f.read())
    f.close        
while True:
   print ("WELCOME TO BANK PORTAL ")
   print ("1.Create Your Account")
   print ("2.Delete Your Account")
   print ("3.Update Your Account")
   print ("4.Search Any Account ")
   print ("5.Display all Customer details")
   print ("6.Exit")
   ch=int(input("Enter your choice:"))
   if ch==1:
       create()
       continue
   if ch==2:
       delete()
   if ch==3:
       update()
   if ch==4:
       search ()
   if ch==5:
       show()
   if ch==6:
       break 
       

   
            
    
