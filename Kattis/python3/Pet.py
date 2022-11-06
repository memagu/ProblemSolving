max_score = 0
player_number = 0
for i in range(5):
    temp = max_score
    max_score = max(sum(map(int, input().split())), max_score)
    if temp != max_score:
        player_number = i+1

print(player_number, max_score)
