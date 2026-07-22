def total_marks(eng,math,sci):
    total = (eng + math + sci)
    return total

def average_marks(eng, math, sci):
    avg=((eng + math + sci)/3)
    return avg

def grade(eng,math,sci):
    avg=((eng+math+sci)/3)
    if avg>=90:
        print("Grade A")
    elif avg>=75:
        print("Grade B")
    elif avg>=60:
        print("Grade C")
    else:
        print("Grade D")

eng=int(input("Enter your english mark"))
math=int(input("Enter your maths mark"))
sci=int(input("Enter your science mark"))
print(total_marks(eng,math,sci))
print(average_marks(eng,math,sci))
grade(eng,math,sci)

