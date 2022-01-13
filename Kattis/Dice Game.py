'''
aCount = 1
bCount = 1
aSum = 0
bSum = 0
aSides = 0
bSides = 0
pList = []

strings = [input(), input()]

#print(strings)

for string in strings:

    aCount = 1
    bCount = 1

    a1, a2, b1, b2 = string.split()

    a1 = float(a1)
    a2 = float(a2)
    b1 = float(b1)
    b2 = float(b2)

    aSides = a2 - a1 + 1
    bSides = b2 - b1 + 1

    aSum = a1
    bSum = b1

    while a1 + 1 * aCount <= a2:
        aSum += a1 + 1 * aCount
        aCount += 1

    #print(aSum)

    while b1 + 1 * bCount <= b2:
        bSum += b1 + 1 * bCount
        bCount += 1

    #print(bSum)

    pList.append(float((aSum / aSides) + (bSum / bSides)))

#print(pList)

if pList[0] > pList[1]:
    print("Gunnar")

elif pList[0] < pList[1]:
    print("Emma")

else:
    print("Tie")
'''

pList = []

strings = [input(), input()]

for string in strings:

    aCount = 1
    bCount = 1

    a1, a2, b1, b2 = string.split()

    a1 = float(a1)
    a2 = float(a2)
    b1 = float(b1)
    b2 = float(b2)

    aSides = a2 - a1 + 1
    bSides = b2 - b1 + 1

    aSum = a1
    bSum = b1

    while a1 + 1 * aCount <= a2:
        aSum += a1 + 1 * aCount
        aCount += 1

    while b1 + 1 * bCount <= b2:
        bSum += b1 + 1 * bCount
        bCount += 1

    pList.append(float((aSum / aSides) + (bSum / bSides)))

if pList[0] > pList[1]:
    print("Gunnar")

elif pList[0] < pList[1]:
    print("Emma")

else:
    print("Tie")