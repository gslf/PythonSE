from typing import List, Tuple
import numpy as np

class GridPathSolver:
    def __init__(self, grid: List[List[int]]):
        self.grid = np.array(grid)
        self.rows, self.cols = self.grid.shape
        self.dp = np.zeros_like(self.grid)
        
    def solve(self) -> Tuple[int, List[Tuple[int, int]]]:
        """
        Finds the shortest path and its cost from top-left to bottom-right
        Returns: (minimum_cost, path_coordinates)
        """
        # Initialize first row and column
        self.dp[0, 0] = self.grid[0, 0]
        
        # Fill first row
        for j in range(1, self.cols):
            self.dp[0, j] = self.dp[0, j-1] + self.grid[0, j]
            
        # Fill first column
        for i in range(1, self.rows):
            self.dp[i, 0] = self.dp[i-1, 0] + self.grid[i, 0]
            
        # Fill rest of the dp table
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                self.dp[i, j] = min(self.dp[i-1, j], self.dp[i, j-1]) + self.grid[i, j]
                
        # Reconstruct path
        path = self._reconstruct_path()
        return self.dp[-1, -1], path
    
    def _reconstruct_path(self) -> List[Tuple[int, int]]:
        """Reconstructs the path from source to destination"""
        path = []
        i, j = self.rows-1, self.cols-1
        
        while i > 0 or j > 0:
            path.append((i, j))
            
            if i == 0:
                j -= 1
            elif j == 0:
                i -= 1
            else:
                if self.dp[i-1, j] < self.dp[i, j-1]:
                    i -= 1
                else:
                    j -= 1
        
        # Aggiungi il punto di partenza una sola volta
        path.append((0, 0))
        return path[::-1]

# Example usage
grid = [
    [1, 3, 1, 2],
    [2, 1, 2, 1],
    [4, 2, 1, 3],
    [1, 1, 2, 1]
]

solver = GridPathSolver(grid)
min_cost, path = solver.solve()

print(f"The best path is: {' -> '.join(f'[{x},{y}]' for x, y in path)}")
print(f"Minimum cost: {min_cost}")