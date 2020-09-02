import copy
from collections import deque

goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

class Node():
    def __init__(self, board):
        self.board = board

    def expand(self):
        children = []
        board_copy = copy.deepcopy(self.board)
        zero_index = self.board.index(0)
        new_indices = [zero_index - 3, zero_index + 3, zero_index - 1, zero_index + 1]

        for index in new_indices:
            if index in range(-len(board_copy), len(board_copy)):
                board_copy[index], board_copy[zero_index] = board_copy[zero_index], board_copy[index]
                children.append(Node(board_copy))
                board_copy = copy.deepcopy(self.board)

        return children


def goal_test(list):
    for node in list:
        if node.board == goal:
            return True
    else:
        return False


def bfs(board):
    start = Node(board)
    queue = deque()
    queue.append(start)

    cost = 0
    while queue:
        next = queue.popleft()
        print(next.board)
        children = next.expand()
        cost += 1

        if goal_test(children):
            print("goal found")
            print("cost: ",cost)
            break

        for child in children:
            queue.append(child)







board = [3, 1, 0, 6, 4, 5, 2, 7, 8]
#fast exmple: [3, 1, 0, 2, 4, 5, 6, 7, 8]
#long example: [7, 2, 4, 5, 0, 6, 8, 3, 1]
bfs(board)
