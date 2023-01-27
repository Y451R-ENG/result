a=int(input("Enter marks of English: "))
b=int(input("Enter marks of Physics: "))
c=int(input("Enter marks of Chemstry: "))
d=int(input("Enter marks of Maths: "))
e=int(input("Enter marks of Computer: "))
if a>100:
   print("Invalid")
elif b>100:
   print("Invalid")
elif c>100:
   print("Invalid")
elif d>100:
   print("Invalid")
elif e>100:
   print("Invalid")
else:
    f=a+b+c+d+e
    print("Total Marks is:",f)
per=f/500*100
print("You scored:-",per)
if per>=80:
          print("You have got Grade A")
elif per>=60:
          print("You have got Grade B")
elif per>=33:
          print("You have got Grade C")
else:
          print("You are Fail But failure is a pillar of Succes")
