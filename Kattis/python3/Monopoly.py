chances = {"2": 0.027777777777777776,
           "3": 0.05555555555555555,
           "4": 0.08333333333333333,
           "5": 0.1111111111111111,
           "6": 0.1388888888888889,
           "7": 0.16666666666666666,
           "8": 0.1388888888888889,
           "9": 0.1111111111111111,
           "10": 0.08333333333333333,
           "11": 0.05555555555555555,
           "12": 0.027777777777777776}

_ = input()
print(sum(chances[steps] for steps in input().split()))
