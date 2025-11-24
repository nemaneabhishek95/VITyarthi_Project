# College Bus Route Optimizer

This project implements a simple **Bus Route Optimization** solution using Python, focusing on clustering student pickup locations and generating routes based on the **Nearest Neighbor** heuristic. The goal is to efficiently transport students from their scattered pickup points to a central college location using a limited number of buses, each with a maximum capacity.

## How It Works

The core logic is encapsulated in the `BusRouteOptimizer` class.

### 1. Nearest Neighbor Clustering (VRP-NN)

The `nearest_neighbor_clustering` method is the heart of the optimization. It uses a **greedy approach** to build each route:

1.  **Starts** at the College Location.
2.  **Iterative Selection:** For the current bus, it repeatedly selects the unassigned student pickup point that is **closest (nearest neighbor)** to the bus's **current location** (the last student picked up).
3.  **Capacity Check:** This continues until the bus reaches its `bus_capacity` or all remaining students are assigned.
4.  **New Route:** The process repeats for the next available bus, starting again from the **College Location**.



### 2. Route Distance Calculation

The `calculate_route_distance` method calculates the total Euclidean distance for a complete round-trip route.

## Requirements

This script requires the following standard Python libraries:

* `matplotlib` (for visualization)
* `numpy` (for distance calculation)

You can install them using pip:

pip install matplotlib numpy
🚀 Usage
The following examples demonstrate how to initialize and run the optimizer. To execute the code, save it as script.py and run it from your terminal using python script.py.

Example 1: Random Data (45 students, 3 buses)
This code snippet is part of the if __name__ == "__main__": block in your Python file.

Python

# Initialize with random student locations
import random
random.seed(42) # For reproducibility
college = (50, 50)
num_students = 45
student_locations = [(random.uniform(10, 90), random.uniform(10, 90)) for _ in range(num_students)]

# Initialize the optimizer
optimizer = BusRouteOptimizer(
    college_location=college,
    student_locations=student_locations,
    num_buses=3,
    bus_capacity=20
)

# Run optimization
print("Optimizing routes for 45 students with 3 buses...")
optimizer.nearest_neighbor_clustering()
optimizer.print_route_details()
# optimizer.visualize_routes() # Uncomment this line to see the plot
Example 2: Custom Data (12 students, 2 buses)
Python

# Initialize with specific, clustered student locations
custom_students = [
    (20, 30), (25, 35), (22, 28),   
    (70, 70), (75, 68), (72, 73),   
    (40, 80), (38, 82), (42, 78),   
    (80, 20), (82, 18), (78, 22),   
]

optimizer2 = BusRouteOptimizer(
    college_location=(50, 50),
    student_locations=custom_students,
    num_buses=2,
    bus_capacity=8
)

# Run optimization
print("\nOptimizing routes for 12 students with 2 buses...")
optimizer2.nearest_neighbor_clustering()
optimizer2.print_route_details()
# optimizer2.visualize_routes(figsize=(10, 8)) # Uncomment this line to see the plot
