class Car:
    def __init__(self, identifier, base_speed, boost_speed, boost_cooldown, boost_duration):
        self.identifier = identifier
        self.base_speed = base_speed
        self.boost_speed = boost_speed
        self.boost_cooldown = boost_cooldown
        self.boost_duration = boost_duration

        self.position = 0
        self.is_boosting = True
        self.duration_timer = self.boost_duration
        self.cooldown_timer = self.boost_duration

    def update(self):
        if self.is_boosting:
            self.position += self.boost_speed
            self.duration_timer -= 1

            if self.duration_timer <= 0:
                self.is_boosting = False
                self.cooldown_timer = self.boost_cooldown

            return

        self.position += self.base_speed
        self.cooldown_timer -= 1

        if self.cooldown_timer <= 0:
            self.is_boosting = True
            self.duration_timer = self.boost_duration

    def __repr__(self):
        return f"Car({self.identifier}, {self.base_speed}, {self.boost_speed}, {self.boost_cooldown}, {self.boost_duration}, pos={self.position})"


def main():
    number_of_test_cases = int(input())
    with open("output.txt", "w") as f:
        for test_case in range(1, number_of_test_cases + 1):
            track_length, number_of_cars = map(int, input().split())
            cars = [Car(*map(int, input().split())) for _ in range(number_of_cars)]

            candidates = []
            while not candidates:
                for car in cars:
                    car.update()
                    if car.position >= track_length:
                        candidates.append(car)

            f.write(f"Case #{test_case}: {min(candidates, key=lambda x: x.identifier).identifier}\n")


if __name__ == "__main__":
    main()
