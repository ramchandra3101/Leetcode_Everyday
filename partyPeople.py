q = 3
people = [1, 2, 1]
status = ['+', '+', '-']

def partyPeople(q, people, status):
    currentCount, maxCount = 0, 0
    for i in range(q):
        if status[i] == '+':
            currentCount += 1
        else:
            currentCount -= 1
        maxCount = max(maxCount, currentCount)
    return maxCount
print(partyPeople(q, people, status))


