def part1():
    sensor_beacon_data = []
    with open("data.in", 'r') as f:
        for line in map(str.strip, f.readlines()):
            sensor_beacon_data_raw = line.split()
            sensor_beacon_data.append(tuple(map(lambda s: int(s.split('=')[1].replace(',', '').replace(':', '')),
                                                (sensor_beacon_data_raw[2], sensor_beacon_data_raw[3],
                                                 sensor_beacon_data_raw[8], sensor_beacon_data_raw[9]))))

    occupied = set()

    for sx, sy, bx, by in sensor_beacon_data:
        sensor_reach = abs(sx - bx) + abs(sy - by)
        distance_to_y = abs(sy - 2_000_000)

        if distance_to_y > sensor_reach:
            continue

        occupied.add(sx)
        for dx in range(1, sensor_reach - distance_to_y + 1):
            occupied.add(sx + dx)
            occupied.add(sx - dx)

    for _, _, bx, by in sensor_beacon_data:
        if by == 2_000_000 and bx in occupied:
            occupied.remove(bx)

    return len(occupied)


def part2():
    sensor_beacon_data = []
    with open("data.in", 'r') as f:
        for line in map(str.strip, f.readlines()):
            sensor_beacon_data_raw = line.split()
            sensor_beacon_data.append(tuple(map(lambda s: int(s.split('=')[1].replace(',', '').replace(':', '')),
                                                (sensor_beacon_data_raw[2], sensor_beacon_data_raw[3],
                                                 sensor_beacon_data_raw[8], sensor_beacon_data_raw[9]))))

    max_x = 4_000_000
    max_y = 4_000_000

    for y in range(max_y + 1):
        x = 0

        while x <= max_x:
            for sx, sy, bx, by in sensor_beacon_data:
                sensor_reach = abs(sx - bx) + abs(sy - by)
                dist = abs(x - sx) + abs(y - sy)

                if dist <= sensor_reach:
                    vertical_dist = abs(y - sy)
                    x = sx + sensor_reach - vertical_dist + 1
                    break

            else:
                return x * 4_000_000 + y


if __name__ == "__main__":
    print(part1())
    print(part2())
