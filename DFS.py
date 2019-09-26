data = {1: [2, 3, 5],
        2: [1, 2],
        3: [1, 2, 4],
        4: [3, 5],
        5: [1, 4]
        }


def DFS(array, start):
    stack = []
    seen = []
    stack.append(start)
    seen.append(start)
    while len(stack) > 0:
        i = stack.pop()
        for j in data[i]:
            if j not in seen:
                stack.append(j)
                seen.append(j)
        print(i)
    return


DFS(data, 1)
