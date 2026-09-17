class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars =  sorted(zip(speed , position), reverse = True)

        fleets = 0 
        prev = 0
        
        for pos , spd in pairs:
            time = (target - pos) / spd

            if time > prev:
                fleets += 1
                prev = time
        return fleets
        