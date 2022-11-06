number_of_clicks = int(input())

if number_of_clicks % 2 != 0:
    print("still running")
else:
    times = []
    for _ in range(number_of_clicks):
        times.append(int(input()))

    time = 0
    for i in range(len(times)):
        if i % 2 != 0:
            time += times[i] - times[i-1]

    print(time)


