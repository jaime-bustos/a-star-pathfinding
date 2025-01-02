# A* Pathfinding Algorithm Visualization

A Python-based visualization tool that demonstrates the A* pathfinding algorithm using Pygame. This interactive application allows users to create barriers, set start and end points, and watch the algorithm find the shortest path in real-time.

## Features

- Interactive grid-based visualization
- Real-time pathfinding demonstration
- Custom barrier placement
- Color-coded states for better understanding
- Manhattan distance heuristic implementation

## Prerequisites

To run this application, you'll need:
- Python 3.x
- Pygame library
- Math module (built-in)
- Queue module (built-in)

Install the required Pygame library using pip:
```bash
pip install pygame
```

## Usage

1. Run the program:
```bash
python astar_visualization.py
```

2. Controls:
   - Left Mouse Button:
     - First click: Set start point (orange)
     - Second click: Set end point (turquoise)
     - Additional clicks: Create barriers (black)
   - Right Mouse Button: Erase/reset nodes
   - Spacebar: Start the algorithm (after setting start and end points)
   - 'C' key: Clear the grid and reset

## Color Guide

- White: Unvisited nodes
- Orange: Start node
- Turquoise: End node
- Black: Barriers
- Red: Closed nodes (already evaluated)
- Green: Open nodes (to be evaluated)
- Purple: Final path
- Grey: Grid lines

## How It Works

1. The algorithm uses a priority queue to determine which nodes to evaluate next
2. Manhattan distance is used as the heuristic function to estimate distances
3. For each node, the algorithm calculates:
   - g_score: The cost to reach the current node from the start
   - h_score: The estimated cost from the current node to the end
   - f_score: The sum of g_score and h_score

## Implementation Details

The visualization is built using several key components:

- `Node` class: Represents each cell in the grid and maintains its state
- `make_grid()`: Creates the visualization grid
- `algorithm()`: Implements the A* pathfinding logic
- `reconstruct_path()`: Traces and displays the final path
- `draw()`: Handles the visualization updates

## Performance

- Grid Size: 50x50 (configurable via `ROWS` variable)
- Window Size: 800x800 pixels
- Real-time visualization with immediate feedback

## Customization

You can modify the following parameters in the code:
- `WIDTH`: Change the window size
- `ROWS`: Adjust the grid density
- Colors: Modify the RGB values at the top of the file

## Limitations

- Diagonal movement is not implemented
- Grid size is fixed during runtime
- Only supports single start and end points

## Contributing

Feel free to fork this project and submit pull requests for any improvements such as:
- Diagonal movement support
- Adjustable grid size
- Additional pathfinding algorithms
- Performance optimizations