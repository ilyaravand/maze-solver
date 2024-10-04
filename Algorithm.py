from _helpers import Node, Stack, Queue, PriorityQueue
import math


class DFS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.stack = Stack()
        self.stack.push(Node(pos=start_pos, parent=None))

    def get_successors(self, x, y):
        return [(x + 1, y + 1), (x+1, y), (x-1, y), (x, y+1), (x, y-1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] <= self.grid_dim[0] and 0 <= pos[1] <= self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        curr_state = self.stack.pop()
        x, y = curr_state.position()
        done = False
        solution_path = []

        for step in self.get_successors(x, y):
            if self.is_valid_cell(step) and grid[step[0], step[1]] in [1, 3]: # 1: empty cell has not explored yet, 3: goal cell
                self.stack.push(Node(pos=step, parent=curr_state))

                if step == self.goal_pos:
                    done = True
                    solution_path = self.backtrack_solution(curr_state)
                    break
            
            grid[x, y] = 4 # visited

        return solution_path, done, grid


class BFS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.queue = Queue()
        self.queue.push(Node(pos=start_pos, parent=None))  # Adjusted to use 'push'
        
    def get_successors(self, x, y):
        
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        
        return 0 <= pos[0] < self.grid_dim[0] and 0 <= pos[1] <= self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
 

        curr_state = self.queue.pop()
        x, y = curr_state.position()
        done = False
        solution_path = []
        for step in self.get_successors(x, y):
            if self.is_valid_cell(step) and grid[step[0], step[1]] in [1, 3]:
                self.queue.push(Node(pos=step, parent=curr_state))
                if step == self.goal_pos:
                    done = True
                    solution_path = self.backtrack_solution(curr_state)
                    break
            
            grid[x, y] = 4 # visited

        return solution_path, done, grid


class IDS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.stack = Stack()
        self.stack.push((Node(pos=start_pos, parent=None), 0))
        self.limit = 0
        self.nodes = []

    def get_successors(self, x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] <= self.grid_dim[0] and 0 <= pos[1] <= self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        if self.stack.isEmpty() == False:
            return self.dls(grid)
        for node, pre_color in self.nodes:
            grid[node[0], node[1]] = pre_color
        
        self.limit += 1
        self.stack.push((Node(pos=self.start_pos, parent=None), self.limit))
        return self.dls(grid)


    def dls(self, grid):
        curr_state, curr_lim = self.stack.pop()

        x, y = curr_state.position()
        done = False
        solution_path = []
        if curr_lim <= 0:
            return solution_path, done, grid
        for step in self.get_successors(x, y):
            if self.is_valid_cell(step) and grid[step[0], step[1]] in [1, 3]: # 1: empty cell has not explored yet, 3: goal cell
                self.nodes.append((step, grid[step[0], step[1]]))
                self.stack.push((Node(pos=step, parent=curr_state), curr_lim - 1))
                
                if step == self.goal_pos:
                    done = True
                    solution_path = self.backtrack_solution(curr_state)
                    break
            
            grid[x, y] = 4 # visited

        return solution_path, done, grid


class A_Star_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.open_list = PriorityQueue()
        self.close_list = PriorityQueue()
        self.open_list.push(Node(pos=start_pos, parent=None, cost=0), 0)
        self.g = dict()
        self.closed_list_f = dict()

    def get_successors(self, x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] <= self.grid_dim[0] and 0 <= pos[1] <= self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        curr_state = self.open_list.pop()
        x, y = curr_state.position()
        g_q = curr_state.cost
        done = False
        solution_path = []

        for step in self.get_successors(x, y):
            if self.is_valid_cell(step) and grid[step[0], step[1]] in [1, 3, 4]: # 1: empty cell has not explored yet, 3: goal cell
                g = g_q + 1
                suc_h = math.sqrt(abs(self.goal_pos[0] - step[0]) ** 2 + abs(self.goal_pos[1] - step[1]) ** 2)
                #suc_h = abs(self.goal_pos[0] - step[0])  + abs(self.goal_pos[1] - step[1])
                suc_f = g + suc_h
                if (((step[0], step[1]) in self.closed_list_f.keys() and self.closed_list_f[step] > suc_f) or (step[0], step[1]) not in self.closed_list_f.keys()):
                    self.open_list.update(Node(pos=step, parent=curr_state, cost=g), suc_f)
                
                if step == self.goal_pos:
                    done = True
                    solution_path = self.backtrack_solution(curr_state)
                    break
            
            grid[x, y] = 4 # visited
        self.closed_list_f[(x, y)] = curr_state.cost
        return solution_path, done, grid


class A_Star_Geometric_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        pass

    def update(self, grid):
        """
        ***************************bonus***************************
        Input: grid (2D array)
        Output:
            solution_path (List of tuples, empty if no solution found)
            done (Boolean, True if the goal is reached, False otherwise)
            grid (Updated 2D array)
        """
        pass