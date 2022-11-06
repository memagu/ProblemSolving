
n = int(input())

strat_adrian = ["A", "B", "C"] * n
strat_bruno = ["B", "A", "B", "C"] * n
strat_goran = ["C", "C", "A", "A", "B", "B"] * n

score_adrian = 0
score_bruno = 0
score_goran = 0

for index, letter in enumerate(input()):
    if letter == strat_adrian[index]:
        score_adrian += 1
    if letter == strat_bruno[index]:
        score_bruno += 1
    if letter == strat_goran[index]:
        score_goran += 1

score_list = [score_adrian, score_bruno, score_goran]
score_list.sort()
print(score_list[-1])

if score_adrian >= score_bruno and score_adrian >= score_goran:
    print("Adrian")
if score_bruno >= score_adrian and score_bruno >= score_goran:
    print("Bruno")
if score_goran >= score_adrian and score_goran >= score_bruno:
    print("Goran")