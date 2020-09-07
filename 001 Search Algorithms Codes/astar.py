import copy
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

class Node():

    def __init__(self, board):
        self.board = board
        #--added fields
        self.parent = None
        self.g = 0

    #sets the parent of the current node
    def set_parent(self, parent):
        self.parent = parent
        self.g = self.parent.g + 1


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


    def h(self):
        counter = 0
        for index, value in enumerate(self.board):
            if index != value:
                counter+= 1
        return counter

    def f(self):
        return self.h() + self.g






def goal_test(node):
    return node.board == goal

def find_best_node(list):
    min = list[0]
    for node in list:
        if node.f() < min.f() :
            min = node
    return min



def astar_search(board):
    closed = []
    frontier = []
    next = Node(board)


    while True:

        if goal_test(next):
            print("goal found")
            break

        if next.board not in closed:
            children = next.expand()
            parent = next
            frontier.extend(children)
            closed.append(next.board)
            next = find_best_node(frontier)
            next.set_parent(parent)
            print(next.board)

        else:
            frontier.remove(next)
            next = find_best_node(frontier)





board = [3, 1, 0, 6, 4, 5, 2, 7, 8]

astar_search(board)
