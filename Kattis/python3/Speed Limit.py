
loop = True


def velocityAndTimeToDistance(velocity, time):
    return int(velocity) * (int(time) - previousTime)


while loop:

    totalDistance = 0
    previousTime = 0
    userInput = int(input())

    if userInput == -1:
        loop = False
        pass
    else:
        for elements in range(userInput):
            velocityAndTime = input().split()
            totalDistance += velocityAndTimeToDistance(velocityAndTime[0], velocityAndTime[1])
            previousTime = int(velocityAndTime[1])
        print(str(totalDistance) + " miles")
