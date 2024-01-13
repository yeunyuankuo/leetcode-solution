def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    # time: O(N)
    # space: O(N)
    stack = []
    res = [0] * len(temperatures)

    if len(temperatures) > 0:
        stack.append(0)

    for i in range(1, len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            peek = stack.pop()
            res[peek] = i - peek    
        stack.append(i)
        
    return res