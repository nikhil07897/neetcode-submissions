class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars =  sorted(zip(target, position), reverse = True)

        fleets = 0 
        prev = 0
        
        for pos , spd in pair:
            target = (target - pos) / spd

            if fleets > prev:
                fleets += 1
                prev = fleets
        return prev
        