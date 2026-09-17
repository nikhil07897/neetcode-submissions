class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(positon, speed), reverse = True)

        fleets = 0
        prev = 0

        for pos, spd in cars:
            time = (target - position) / spd

            if time > prev:
                fleets += 1
                time = prev
        return fleets        