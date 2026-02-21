class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level


class IDDFS:
   def __init__(self):
      self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
      self.N = 0
      self.M = 0
      self.goal = None
      self.path = []
      self.goal_depth = 0

   def init(self, grid, start, goal):
      self.N = len(grid)
      self.M = len(grid[0])
      self.goal = goal

      depth = 0
      limit = self.N * self.M  # safe maximum search depth

      while depth <= limit:
         visited = set()
         self.path = [start]

         if self.dls(grid, start[0], start[1], depth, visited):
            print(f"Path found at depth {self.goal_depth} using IDDFS")
            print("Traversal Order:", self.path)
            return

         depth += 1

      print(f"Path not found at max depth {limit} using IDDFS")

   def dls(self, grid, x, y, depth, visited):

      if (x, y) == self.goal:
         self.goal_depth = len(self.path) - 1
         return True

      if depth == 0:
         return False

      visited.add((x, y))

      for dx, dy in self.directions:
         nx, ny = x + dx, y + dy

         if 0 <= nx < self.N and 0 <= ny < self.M and grid[nx][ny] == 1 and (nx, ny) not in visited:
            self.path.append((nx, ny))

            if self.dls(grid, nx, ny, depth - 1, visited):
               return True

            self.path.pop()

      visited.remove((x, y))
      return False


if __name__ == "__main__":

   n, m = map(int, input().split())

   grid = []
   for _ in range(n):
      grid.append(list(map(int, input().split())))

   sx, sy = map(int, input("Start: ").split())
   gx, gy = map(int, input("Target: ").split())

   solver = IDDFS()
   solver.init(grid, (sx, sy), (gx, gy))