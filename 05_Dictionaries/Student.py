student = {"name": "Nihal", "age":18, "course":"BCA"}
print(student)
print(student["course"])
student["city"]="Thrissur"
print(student["city"])
for topic, subject in student.items():
    print(topic,"-",subject)