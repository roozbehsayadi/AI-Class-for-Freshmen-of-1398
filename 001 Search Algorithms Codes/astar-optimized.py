import copy
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Node():
    def __init__(self, board, g, h):
        self.board = board
        self.g = g
        self.h = h
        self.board_hash = self.hash_board(board)

    def f(self):
        return self.g + self.h

    def expand(self):
        children = []
        board_copy = copy.deepcopy(self.board)
        zero_index = self.board.index(0)
        new_indices = [
            zero_index - 3,
            zero_index + 3,
            zero_index - 1,
            zero_index + 1
        ]

        for index in new_indices:
            if index in range(-len(board_copy), len(board_copy)):
                board_copy[index], board_copy[zero_index]\
                    = board_copy[zero_index], board_copy[index]
                children.append(Node(board_copy, self.g + 1, h(board_copy)))
                board_copy = copy.deepcopy(self.board)

        return children

    @staticmethod
    def hash_board(board):
        return int(''.join(map(str, board)))

    def __hash__(self):
        return self.board_hash

    def __eq__(self, other):
        return self.board_hash == other.board_hash

    def __lt__(self, other):
        return self.f() < other.f()

goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def h(board):
    result = 0
    for i in range(len(goal)):
        if board[i] != goal[i]:
            result += 1
    return result


def astar_search(board):
    start = Node(board, 0, h(board))
    queue = PriorityQueue()
    queue.put(start, start.f())
    closed_boards = set()
    cost = 0
    while not queue.empty():
        next = queue.get()
        if next in closed_boards:
            continue
        closed_boards.add(next)
        print(next.board)
        children = next.expand()
        cost += 1
        for child in children:
            if child.board == goal:
                print("goal found")
                print(child.board)
                print("cost: ", cost)
                return
            queue.put(child, child.f())
    print("goal not found")
    print("cost: ", cost)

initial_board = [3, 1, 0, 6, 4, 5, 2, 7, 8]

astar_search(initial_board)
