students = []

class Student:
    def __init__(self, name, score1, score2, grade):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.grade = grade

    def setGrade(self):
        avg = (self.score1 + self.score2) / 2
        if avg >= 90:
            self.grade = 'A'
        elif avg >= 80:
            self.grade = 'B'
        elif avg >= 70:
            self.grade = 'C'
        else:
            self.grade = 'D'

##############  menu 1
def Menu1(name, score1, score2) :
    #사전에 학생 정보 저장하는 코딩
    info = Student(name, score1, score2, 0)
    students.append(info)

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for i in range(len(students)):
        if students[i].grade == 0:
            students[i].setGrade()

##############  menu 3
def Menu3() :
    #출력 코딩
    print("-" * 25)
    print("{:<7}{:<6}{:<7}{:<7}".format("name", "mid", "final", "grade"))
    print("-" * 25) 
    
    for i in range(len(students)):
        print("{:<7}{:<7}{:<7}{:<7}".format(students[i].name, students[i].score1, students[i].score2, students[i].grade))

##############  menu 4
def Menu4(i):
    #학생 정보 삭제하는 코딩
    del students[i]

class ExistName(Exception):
    def __init__(self):
        super().__init__("Already exist name!")

class NotPositive(Exception):
    def __init__(self):
        super().__init__("Score is not positive integer!")

class NoStudentInfo(Exception):
    def __init__(self):
        super().__init__("No student data!")

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":
        try:
            name, score1, score2 = input("Enter name mid-score final-score : ").split()
        except ValueError: # 데이터 입력 갯수
            print("Num of data is not 3!")
        else:
            try:
                for i in range(len(students)):
                    if students[i].name == name:
                        raise ExistName
                try:
                    score1 = int(score1)
                    score2 = int(score2)
                except ValueError:
                    raise NotPositive
                else: 
                    if score1 <= 0 or score2 <= 0: 
                        raise NotPositive
            except NotPositive as e: # 양의 정수
                print(e)
            except ExistName as e: # 이미 존재하는 이름
                print(e)
            else:
                Menu1(name, score1, score2)

    elif choice == "2" :
        try:
            if len(students) == 0:
                raise NoStudentInfo 
        except NoStudentInfo as e: # 저장된 학생 정보의 유무
            print(e)
        else:
            Menu2()
            print("Grading to all students.")

    elif choice == "3" :
        try:
            if len(students) == 0:
                raise NoStudentInfo
        except NoStudentInfo as e: # 저장된 학생 정보의 유무
            print(e)
        else:
            try:
                for i in range (len(students)):
                    if students[i].grade == 0:
                        raise Exception("There is a student who didn't get grade.")
            except Exception as e: # 저장되어 있는 학생들의 학점이 모두 부여되어 있는지
                print(e)
            else:
                print()
                Menu3()

    elif choice == "4" :
        try:
            if len(students) == 0: 
                raise NoStudentInfo
        except NoStudentInfo as e: # 저장된 학생 정보의 유무
            print(e)
        else:
            try:
                name = input("Enter the name to delete : ")
                for i in range(len(students)):
                    if students[i].name == name:
                        Menu4(i)
                        print(f"{name} student information is deleted.")
                        break
                    if i == len(students) - 1:
                        raise Exception("Not exist name!")
            except Exception as e: # 입력 받은 학생의 존재 유무
                print(e)

    elif choice == "5" :
        print("Exit Program!")
        break
    
    else :
        print("Wrong number. Choose again.")
