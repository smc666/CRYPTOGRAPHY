import smtplib
from getpass import getpass
import random
import string
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import string 

dict={}
lst_dcry=[]

def decryption():
  user_key=input("Enter key: ") 
  for k,c in dict.items():
     if(user_key==k):
      for j in c:
        y=int(pow(j-10,0.5))
        val=chr(y)
        lst_dcry.append(val)
  var=''.join(str(ele) for ele in lst_dcry) 
  print(var) 

  lst_dcry.clear()
  main()


        #print(val,end=" ")

  


  


def upload(c,k):
  a=str(c)
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth()


  drive = GoogleDrive(gauth)

  file1 = drive.CreateFile({'title': 'ENCRYPTED DATA '})  # Create GoogleDriveFile instance with title 'Hello.txt'.
  file1.SetContentString(a) # Set content of the file from given string.
  file1.Upload()
  
  
  
  user_mail=input("ENTER YOUR EMAIL ID : ")
  mail=smtplib.SMTP("smtp.gmail.com",587)
  mail.ehlo()
  mail.starttls()
  mail.login("l50688568@gmail.com","Lc@88568")
  mail.sendmail("l50688568@gmail.com",user_mail,"Your key" + k)
  mail.close()

  main()

def keyword():
  ltr=[]
  for i in range(10):
    x=random.choice(string.ascii_uppercase)
    ltr.append(x)
    
  new=""
  for j in ltr:
    new+=j
    
  return new


def encryption():
  
  key=keyword()
  global lst
  lst=[]
  string=input("ENTER THE STRING TO BE ENCRYPTED: ")
  for i in string:
    a=ord(i)
    x=(pow(a,2)+10)
    lst.append(x)
  dict[key]=lst 
  upload(lst,key)

 
  lst.clear()







def main():
  print("CHOOSE AN OPTION")
  print("1.ACCESS DATA")
  print("2.ENTER DATA")
  
  i=0
  
  while(i==0):
    choice=int(input("Enter your choice: "))
  
    if choice==1:
      i=1
      decryption()
      
    elif choice==2:
      i=1
      encryption()
      
      
    else:
      print("Enter valid choice")
def p_wrd(pa):
  if pa=="smc":
    print("WELCOME")
    main()
    
  else:
    exit()

p=getpass("Enter password: ")
p_wrd(p) 

