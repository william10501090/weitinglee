data = {1: [2, 3, 5],
        2: [1, 2],
        3: [1, 2, 4],
        4: [3, 5],
        5: [1, 4]
        }


def BFS(array, start):
    queue = []
    seen = []
    queue.append(start)
    seen.append(start)
    while len(queue) > 0:
        i = queue.pop(0)
        for j in data[i]:
            if j not in seen:
                queue.append(j)
                seen.append(j)
        print(i)
    return


BFS(data, 1)
