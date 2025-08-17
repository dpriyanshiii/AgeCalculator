#next time take up birthday to age calculator
#input and data extraction
print("Age Calculator....")
bday=input("Format DD/MM/YYYY: ")
bdata=bday.split("/")
today=input("Enter todays date DD/MM/YYYY: ")
tdata=today.split("/")

#calculating years
#if current months is bigger greater than bday month
if (int(tdata[1])>int(bdata[1])):
  years=int(tdata[2])-int(bdata[2])
  
#if current month is smaller than bday month
elif (int(tdata[1])<int(bdata[1])):
  years=int(tdata[2])-int(bdata[2])-1
  
#when month is same, we go into dates 
else:
  #current date greater than or equal day date
  if (int(tdata[0])>=int(bdata[0])):
    years=int(tdata[2])-int(bdata[2])
    
  #month same but date small
  else:
    years=int(tdata[2])-int(bdata[2])-1
print(years, "years old")


#calculating months
if (tdata[1]>=bdata[1]):
  month=int(tdata[1])-int(bdata[1])
  if (tdata[0]<bdata[0]):
    month=month-1
else:
  month=12-int(bdata[1])+int(tdata[1])
  if(tdata[0]<bdata[0]):
    month=month+int(tdata[1])-1
print(month, "months old")

#calculating days....
arr=[31,28,31,30,31,30,31,31,30,31,30,31]
#dlens=[31,29,31,30,31,30,31,31,30,31,30,31]---> we are assuming leap years dont exist rnn

#finally calculating days
if (tdata[0] >= bdata[0]):
  days=int(tdata[0])-int(bdata[0])
else:
  if (int(tdata[1])>1):
    temp=int(tdata[1])-2 #-1 for prev month and -1 for iteration in array
    new=arr[temp]
    days=new-int(bdata[0])+int(tdata[0])
  else:
    days=31-int(bdata[0])+int(tdata[0])
print(days, "days old")
  
  

#function for leap year check
#def leapcheck(): ---> some other day
