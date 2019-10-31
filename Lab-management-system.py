''' python Mai program bnane Mai help krdo
 Computer lab management system by using file handling and function
 Isme ye bnana hai k konse PC kitne tym tk free hai aur konse Nye pc ha'''
from datetime import datetime
from datetime import timedelta
def write_in_file(name,UserId,Branch):
  file=open("Users.dat","a")
  time=datetime.now()
  file.write(f"name={name},UserId={UserId},Branch={Branch},Reg.time={time},{UserId}.lastLogin={time}\n")
  file.close()
  print("\n\n******************************************\nRagistration successfull........")
  print("Your Credential :-")
  print(f"name={name}\nUserId={UserId}\nfirstLogin={time}")

#ragisterd
def ragisterd():
    print("Enter your name : ",end=" ")
    name=input()
    print("Enter you UserId :",end=" ")
    UserId=input()
    print("Enter computer id : ",end="")
    computer_name=input()
    file=open("Users.dat","r")
    data=file.read()
    file.close()
    validate=data.find(f"name={name},UserId={UserId}")
    return computer_name,validate,UserId
#session
def session(a,b,c):
  if b!=-1:
      print("Confirm to start session[y/n] : ",end=" ")
      confirm=input()
      if (confirm=="y" or confirm=="Y") and isFree(a):
        file=open("Users.dat","r")
        data=file.read()
        file.close()
        data=data.split(",")
        data[4]=c+".lastLogin="+str(datetime.now())
        data=",".join(data)
        file=open("Users.dat","w")
        file.write(data)
        file.close()
        print("started")
        thistime=datetime.now()
        print(thistime)
        if thistime==(datetime.now()-timedelta(hours=2, minutes=10)):
          print("time is completed....")
      else:
        print("computer not found")
#ragistration
def ragistration():
    print("For ragistration Enter details ")
    print("Enter your name : ",end="")
    name=input()
    print("Enter your branch : ",end="")
    Branch=input()
    print("Enter your roll no. : ",end="")
    Roll_no=input()
    write_in_file(name,Branch+"000"+Roll_no[-4:],Branch)
#checking computer is free or not
def isFree(string):
  file=open("computer.dat","r")
  strings=file.read()
  file.close()
  strings=strings.split(",")
  if strings[1].find("True")!=-1:
    return True
  else:
    return False
def adminLogin():
  adminId="ADMINCS11"
  idd=input()
  if idd==adminId:
    print("welcome..._/\"\\_")
  else:
    print("Access denide")
#main function  
if __name__=="__main__":
  print("Welcome to ______ lab  ")
  print("For admin Enter a\nfor sturdent Enter b")
  inn=input()
  if inn=="a":
    adminLogin()
  else:
    print("For ragisterd user Enter 1 \nfor ragistration Enter 2")
    confirm=input()
    if confirm=="1":
      a,b,c=ragisterd()
      session(a,b,c)
    else:
      ragistration()
    

