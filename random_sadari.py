import random

def getInput():
    
    peopleList = []
    while True:
        person = input("사람 입력!, 0 누르면 사다리 타기!")
        if person == "0":
            break
        else:
            peopleList.append(person)
    return peopleList

def sadari(people):
    random.shuffle(people)
    print("출제자" + "    " + "면접자")
    print("----------------")
    for num in range(len(people)):
        print(people[num-1], '->', people[num])

    return
        
if __name__ == '__main__':
    peopleList = ["주디", "수연", "은선", "상혁", "네오", "해시", "팬시"]
    sadari(peopleList)