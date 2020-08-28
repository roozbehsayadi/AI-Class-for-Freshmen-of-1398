from math import log2 

def minimax(remain_depth: int, index: int, is_max_turn: bool, scores: list):
    if remain_depth == 0: # we are done
        return scores[index]

    if is_max_turn:
        return max(
            minimax(remain_depth-1, index*2, False, scores),
            minimax(remain_depth-1, index*2+1, False, scores)
        )
    else:
        return min(
            minimax(remain_depth-1, index*2, False, scores),
            minimax(remain_depth-1, index*2+1, False, scores),
        )


our_scores = [3, 5, 2, 9]
#our_scores = [3, 5, 2, 9, 12, 5, 23, 23] 
depth = log2(len(our_scores))
print( 
    minimax(remain_depth=depth, index=0, is_max_turn=True, scores=our_scores)
        )
