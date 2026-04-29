class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_vel = zip(position, speed)
        car_vel = sorted(car_vel)

        fleets = []

        for i in car_vel:
            print(i, fleets, target)
            while fleets and ((target-i[0])/i[1] >= (target-fleets[-1][0])/fleets[-1][1]):
                fleets.pop()
            
            fleets.append(i)
        
        print(fleets)
        return len(fleets)