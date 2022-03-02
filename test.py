import stack
#reverse array
array = [5,3,4,6,6,9,8,7,10]
print(array)
temp = stack.Stack()

for i in array:
    temp.push(i)

array = []

for i in range(len(temp.data)):
    array.append(temp.pop())

print(array)

class Student():
    def __init__(self):
        self.name = ""
        self.studentNumber = ""
        self.examScores = []
    
    def getBestExamScore(self):
        best = 0
        for i in self.examScores:
            if best < i[1]:
                best = i[1]
        return best

    def getFailedModules(self):
        pass
    def addScore(self, subjectCode, examScore):
        self.examScores.append((subjectCode,examScore))
    def printScore(self):
        pass

s1 = Student()
s1.addScore("math", 69)
s1.addScore("data struct", 23)
s1.addScore("OOP", 420)
print(s1.getBestExamScore())