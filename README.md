# Maze Solver

A Python-based maze solver that implements various artificial intelligence search algorithms to find paths through mazes. The project includes a visual interface using Pygame to display the solving process in real-time.

## Features

- **Multiple Search Algorithms**: 
  - DFS (Depth-First Search)
  - BFS (Breadth-First Search) 
  - IDS (Iterative Deepening Search)
  - A* (A-Star)
  - ASG (A-Star Geometric) - bonus implementation
- **Visual Interface**: Real-time visualization of the search process using Pygame
- **Customizable Start/Goal**: Set custom start and goal positions
- **Multiple Maze Maps**: 8 pre-built maze configurations
- **Performance Metrics**: Displays exploration statistics and solving time

## Project Structure

```
├── Algorithm.py          # Implementation of all search algorithms
├── game.py              # Main game logic and Pygame visualization
├── main.py              # Command-line interface and argument parsing
├── _helpers.py          # Data structures (Node, Stack, Queue, PriorityQueue)
├── maze_generator.py    # Utility to generate random maze test cases
├── mazes/               # Directory containing maze CSV files
│   ├── maze_0.csv
│   ├── maze_1.csv
│   └── ...
└── requirements.txt     # Python dependencies

```

## Install Requirements

To install requirements, run: 
```bash
pip install -r requirements.txt
```

## Usage

Running the code requires the following parameters:

### Required Parameters

1. **-a, --algorithm**
   - Specifies the search algorithm to use
   - Options: `[dfs, bfs, ids, a_star, asg]`

2. **-m, --map**
   - Selects which maze to solve
   - Options: `[0, 1, 2, 3, 4, 5, 6, 7]`

### Optional Parameters

3. **-s, --start**
   - Custom start position of the agent (format: `row,column`)
   - Default: `(0,0)` - top-left corner
   - Example: `1,2`

4. **-g, --goal**
   - Custom goal position of the agent (format: `row,column`)
   - Default: bottom-right corner of the maze
   - Example: `7,9`

## Examples

### Basic Usage
```shell
python3 main.py -a a_star -m 3
```

### With Custom Start and Goal
```shell
python3 main.py -a a_star -m 3 -s '1,2' -g '6,4'
```

### Compare Different Algorithms
```shell
# DFS - Fast but not optimal
python3 main.py -a dfs -m 1

# BFS - Optimal path, explores many nodes
python3 main.py -a bfs -m 1

# A* - Optimal and efficient
python3 main.py -a a_star -m 1
```

## Maze Format

Mazes are stored as CSV files where:
- `0` = Wall (obstacle)
- `1` = Empty cell (passable)
- `2` = Start position (set automatically)
- `3` = Goal position (set automatically)
- `4` = Visited cell (shown during search)
- `5` = Solution path (shown after completion)

## Algorithm Details

- **DFS**: Uses a stack, explores deeply but may not find optimal path
- **BFS**: Uses a queue, guarantees shortest path in unweighted graphs
- **IDS**: Combines DFS space efficiency with BFS optimality
- **A***: Uses heuristic function (Euclidean distance) for efficient optimal pathfinding
- **ASG**: Geometric variant of A* (bonus implementation)

## Controls

During visualization:
- **SPACE**: Start/pause the solving process
- **ESC/Q**: Quit the application
- **Any key**: Close the result window after solving

## Output Information

The program displays:
- Total empty blocks in the maze
- Number of explored blocks
- Algorithm execution time
- Visual representation of the search process

## Generate Custom Mazes

Use the maze generator to create new test cases:
```shell
python3 maze_generator.py
```

This creates a `test_case.csv` file with a randomly generated maze.

# Install requirements
To install requirement, run: `pip install -r requirements.txt`

# Run the code
Running the code needs 4 parameters:

1. -a, --algorithm
    - this parameter specifies the algorithm which is going to run.
    - `[dfs, bfs, ids, a_star, asg]` are your only options.
2. -m, --map
    - map parameter demonstrates the map which the algorithm solves
    - `[0, 1, 2, 3, 4, 5, 6, 7]` are the options of map
3. -s, --start
    - the start position of your agent, such as `1,2`
4. -g, --goal
    - the goal position of your agent, for instance `7,9`

## Example
 
```shell
python3 main.py -a a_star -m 3 -s '1,2' -g '6,4' 
```
