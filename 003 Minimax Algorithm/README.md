# session 3: Min-max Algorithm
+ min-max
+ minimax
+ saddle point (نقطه زینی)


### review: tuple and enumerate 
+ tuple: immutable list!
+ enumerate: use for-each and still access to indix


### review: recursion

+ review fib: fib(n) use fib(n-1) and fib(n-2)
+ solve smaller problem(s) in order to solve big problem 
+ base case: we already know the answer for the small problem
+ more: [wikipedia](https://en.wikipedia.org/wiki/Recursion_(computer_science))


### intro: backtracking
+ not related to Kali Linux and hack stuff
+ some kind of algorithm
+ explore all possible situations
+ not optimal, but still could be useful
+ use recursion (in DFS order)
+ for example 
    1. explore all combinations to solve a Sudoko
    2. N-queen 
    3. maze solving 
    4. finding all sub-sets
+ more: [backtracking](https://en.wikipedia.org/wiki/Backtracking)


### review: two-player game(!)
+ chess for instance
+ each player try to win
+ they **do best to win** -> play optimum
+ red turn, black turn, red turn, black turn
+ each turn, player try to **maximize** chance of win (minimize chance of loss!).
+ what is chance of win? in chess we can calculate it.
+ we can use minimax to maximize our chance of win and develop some AI



## minimax

+ AI for two player games
+ originally developed for "zero sum" games.
+ main version good enough for Tic-Tac-Toe (XO)
+ it could be useful for chess, backgammon 
+ try to minimize **maximum loss**
  + try to win although other player play optimum
  + we assume that other players plays really well 
+ we are **maximizer** and opponent is **minimizer**. (maximize and minimize chance of our win.)


```pascal
function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value


(* Initial call *)
minimax(origin, depth, TRUE)
```

+ more: [wikipedia](https://en.wikipedia.org/wiki/Minimax)
+ even more: [game theory](https://en.wikipedia.org/wiki/Game_theory) and [nash equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium)



+ example 1
![simple example](./images/1.jpg)
+ example 2
![step1 example](https://media.geeksforgeeks.org/wp-content/uploads/minmax.png)
and then ![filled](https://media.geeksforgeeks.org/wp-content/uploads/minmax1.png)

+ run `step1.py`

### Tree?

+ DS? we don't know what is tree yet.
+ ways to finish game.
+ each player make a choice and we move down in tree.

![XO tree](http://files.codinghell.ch/pictures/2012-08-31-Tic-tac-toe-game-tree.png)



## apply minimax for Tic-Tac-Toe

![XO tree](https://materiaalit.github.io/intro-to-ai/img/exercises/ex2/tree_Ex2_2-90b2e222.png)



+ how to calculate base cases? v=?  	
+ we need **evaluation function**
+ check status of a board:

  1. X wins
  2. O wins
  3. Tie
+ assume that we play as X
  +  X wins: +1
  + O wins: -1
  + Tie: 0

let's write it:

```python
def evaluate(b): 
	# Checking for Rows for X or O victory. 
	for row in range(0, 3): 
		if b[row][0] == b[row][1] and b[row][1] == b[row][2]: 
			if b[row][0] == 'x': 
				return +1
			elif b[row][0] == 'o': 
				return -1
	# Checking for Columns for X or O victory. 
	for col in range(0, 3): 
		if b[0][col] == b[1][col] and b[1][col] == b[2][col]: 
			if b[0][col]=='x': 
				return +1
			elif b[0][col] == 'o': 
				return -1
	# Checking for Diagonals for X or O victory. 
	if b[0][0] == b[1][1] and b[1][1] == b[2][2]: 
		if b[0][0] == 'x': 
			return +1
		elif b[0][0] == 'o': 
			return -1
	if b[0][2] == b[1][1] and b[1][1] == b[2][0]: 
		if b[0][2] == 'x': 
			return +1
		elif b[0][2] == 'o': 
			return -1
	# Else if none of them have won then return 0 
	return 0
	
# Driver code 
if __name__ == "__main__": 
	board = [['x', '_', 'o'], 
			['_', 'x', 'o'], 
			['_', '_', 'x']] 
	value = evaluate(board) 
	print("The value of this board is", value) 
# source: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-2-evaluation-function
```

+ run `./step2.py`



## finally: complete Tic Tac Toe with Minimax

+ run `./step3.py`
+ 
