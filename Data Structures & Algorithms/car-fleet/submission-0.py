class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)

        times = [(target - p) / s for p,s in cars]
        fleet = 0
        flag = 0
        for t in times:
            if t > flag:
                fleet += 1
                flag = t
        return fleet