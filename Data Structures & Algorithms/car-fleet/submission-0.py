class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        arrival_times = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars = sorted(cars, reverse=True, key=lambda item: item[0])

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if len(arrival_times) == 0:
                arrival_times.append(time)
            else:
                if time <= arrival_times[-1]:
                    continue
                else:
                    arrival_times.append(time)
        return len(arrival_times)


        