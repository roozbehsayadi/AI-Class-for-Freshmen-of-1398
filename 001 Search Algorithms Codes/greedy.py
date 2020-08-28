import copy
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

    def get_heuristic(self):
        counter = 0
        for index, value in enumerate(self.board):
            if index != value:
                counter+= 1
        return counter






def goal_test(node):
    return node.board == goal

def find_best_node(list):
    min = list[0]
    for node in list:
        if node.get_heuristic() < min.get_heuristic():
            min = node
    return min



def greedy_search(board):
    closed = []
    next = Node(board)

    while True:
        if goal_test(next):
            print("goal found")
            break

        if next.board not in closed:
            children = next.expand()
            closed.append(next.board)
            next =  find_best_node(children)
            print(next.board)
        else:
            children.remove(next)
            next = find_best_node(children)





board = [3, 1, 0, 6, 4, 5, 2, 7, 8]

greedy_search(board)
