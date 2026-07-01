from typing import List


# Matrix Depth-First Search
# Time Complexity: O(4 ^ (n * m))
# Space Complexity: O(n * m)
# where:
#   - n is the number of rows
#   - m is the number of columns
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        return self.__dfs(0, 0)

    def __dfs(self, row: int, col: int) -> int:
        if self.__is_out_of_bounds(row, col) or \
                self.__is_rock(row, col) or \
                self.__is_visited(row, col):
            return 0

        if self.__is_bottom_right_corner(row, col):
            return 1

        self.visited.add((row, col))

        count = 0
        count += self.__dfs(row + 1, col)
        count += self.__dfs(row - 1, col)
        count += self.__dfs(row, col + 1)
        count += self.__dfs(row, col - 1)

        self.visited.remove((row, col))
        return count

    def __is_out_of_bounds(self, row: int, col: int) -> bool:
        return row == -1 or row == self.rows or \
            col == -1 or col == self.cols

    def __is_rock(self, row: int, col: int) -> bool:
        return self.grid[row][col] == 1

    def __is_visited(self, row: int, col: int) -> bool:
        return (row, col) in self.visited

    def __is_bottom_right_corner(self, row: int, col: int) -> bool:
        return row == self.rows - 1 and col == self.cols - 1
