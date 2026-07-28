def average(marks):
    return sum(marks)/len(marks)
marks=[]
n=int(input("enter the no of marks"))
for i in range(n-1):
    list=int(input("Enter the marks"))
marks.append(list)
print("Average =", average(marks))
