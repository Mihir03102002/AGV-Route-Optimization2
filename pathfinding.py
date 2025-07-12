# pathfinding.py
import heapq
import numpy as np
from collections import deque

class PathFinder:
def __init__(self, grid):
self.grid = grid
self.height = len(grid)
self.width = len(grid[0])

def a_star(self, start, end):
'''A* pathfinding algorithm implementation'''
heap = [(0, start)]
came_from = {}
cost_so_far = {start: 0}

while heap:
current_cost, current_pos = heapq.heappop(heap)

if current_pos == end:
break

for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
next_pos = (current_pos[0] + dx, current_pos[1] + dy)
if (0 <= next_pos[0] < self.height and
0 <= next_pos[1] < self.width and
self.grid[next_pos[0]][next_pos[1]] != 1):
new_cost = cost_so_far[current_pos] + 1
if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
cost_so_far[next_pos] = new_cost
priority = new_cost + self.heuristic(end, next_pos)
heapq.heappush(heap, (priority, next_pos))
came_from[next_pos] = current_pos

path = []
if end in came_from:
current = end
while current != start:
path.append(current)
current = came_from[current]
path.append(start)
path.reverse()

return path

def heuristic(self, a, b):
return abs(a[0] - b[0]) + abs(a[1] - b[1])