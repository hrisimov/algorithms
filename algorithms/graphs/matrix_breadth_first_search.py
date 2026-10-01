from collections import deque
from typing import List, Set, Tuple


# Matrix Breadth-First Search
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# where:
#   - n is the number of rows
#   - m is the number of columns
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if self.__is_rock(grid, 0, 0) or \
                self.__is_rock(grid, rows - 1, cols - 1):
            return -1

        queue = deque(((0, 0),))
        visited = {(0, 0)}
        directions = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        )
        path_length = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if self.__is_bottom_right_corner(row, col, rows, cols):
                    return path_length

                for row_delta, col_delta in directions:
                    new_row = row + row_delta
                    new_col = col + col_delta

                    if self.__is_out_of_bounds(new_row, new_col, rows, cols) or \
                            self.__is_rock(grid, new_row, new_col) or \
                            self.__is_visited(visited, new_row, new_col):
                        continue

                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

            path_length += 1

        return -1

    @staticmethod
    def __is_bottom_right_corner(row: int, col: int, rows: int, cols: int) -> bool:
        return row == rows - 1 and col == cols - 1

    @staticmethod
    def __is_out_of_bounds(row: int, col: int, rows: int, cols: int) -> bool:
        return not 0 <= row < rows or not 0 <= col < cols

    @staticmethod
    def __is_rock(grid: List[List[int]], row: int, col: int) -> bool:
        return grid[row][col] == 1

    @staticmethod
    def __is_visited(visited: Set[Tuple[int, int]], row: int, col: int) -> bool:
        return (row, col) in visited
