"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the 
ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same 
speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is 
ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car 
is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Input: target = 10, position = [3], speed = [3]
Output: 1

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1

Approach:
-The car that is furthest along (closest to target) will always get to the destination first because no car can
pass.
-If you calculate the time to get to the destination for each car and compare it to the order of the cars you
can find which cars will form a fleet.
-If you have an array of times to destination in hrs = [1,1,12,7,3] and positions are [10,8,0,5,3]
-car[0] will arrive alone, car[1] will arrive alone, car[2:4] will all create a fleet because car[3:4] will
catch up to car[2] and slow down to match their speed
"""
def car_fleet(target, position, speed):
    # Create pairs for [position, speed]
    pairs = [[p,s] for p,s in zip(position, speed)]

    # Initate [stack]
    stack = []
    # Calculate time = (target-position)/speed
    # Append time to [stack]
    # If len([stack]) > 1, if stack[-1] <= stack[-2], pop stack[-1]
    for p,s in sorted(pairs)[::-1]:
        time = (target - p)/s
        stack.append(time)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)