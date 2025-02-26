# l = [3,3, 4 , 3]

# print(sum(l))
# n = l.count(3)
# # print(n)
# marks = {
# "harry" : 100,
# "monika" : 565,
# 0 : "harry"
# }
# print(marks.items())
# print(marks.keys())
# print(marks["monika"])
marks1 = int(input("Enter the marks 1: "))
marks2 = int(input("Enter the marks 2: "))
marks3 = int(input("Enter the marks 3: "))
total_percentage = (marks1 + marks2 + marks3)/300
if(total_percentage>=40):
    print("you are pass")
else: 
    print("u failed , try again next year")
