def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    # time: O(NlogN), NlogN for sorting the list of position and speed
    # space: O(N), N for the stack
    stack = []
    positionSpeed = [(p, s) for p, s in zip(position, speed)]
    positionSpeed.sort(reverse=True)
    print(positionSpeed)

    for p, s in positionSpeed:
        if not stack:
            stack.append((target - p) / s)

        peekArriveTime = stack[-1]
        currArriveTime = (target - p) / s

        if currArriveTime > peekArriveTime:
            stack.append(currArriveTime)
    
    return len(stack)