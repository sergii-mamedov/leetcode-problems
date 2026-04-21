"""
36. Valid sudoku
https://leetcode.com/problems/valid-sudoku/description/
https://neetcode.io/problems/valid-sudoku/question

Use three sets to track seen values for each row, column, and 3x3 sub-box.
Iterate through the board once, skipping empty cells.
For each number, check whether it already exists in the corresponding row, column, or sub-box.
If it does, the board is invalid; otherwise, add it to all three sets.
The sub-box index can be computed as (i // 3) + 3 * (j // 3).
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9

        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        blocks = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                el = board[i][j]
                if el == '.':
                    continue

                block_id = i // 3 + 3*(j // 3)
                if el in rows[i] or el in columns[j] or el in blocks[block_id]:
                    return False
                
                rows[i].add(el)
                columns[j].add(el)
                blocks[block_id].add(el)
        
        return True