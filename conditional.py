# a = int(input("enter your age: "))
# if(a>18):
#     print("age is greater ")

# # elif(a<0):
# #       print("u are entering an invalid age")
# # elif(a==0):
# #       print("u are entering an 0 ")
# else:
#         print("age is not greater than 18")

# print("good")
a1 = int(input("enter the number 1"))
a2 = int(input("enter the number 2"))
a3= int(input("enter the number 3"))
a4 = int(input("enter the number 4"))
 
if (a1>a2 and a1>a2 and a1>a4):
  print("greatest number is a1: ", a1)

elif (a2>a1 and a2>a3 and a2>a4):
  print("greatest number is a2: ", a2)


elif (a3>a1 and a3>a2 and a3>a4):
  print("greatest number is a3: ", a3)

elif (a4>a1 and a4>a2 and a4>a3):
  print("greatest number is a4: ", a4)
