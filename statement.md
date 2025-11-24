# Bus Route Optimization using Nearest Neighbor Clustering

This project implements a **Bus Route Optimizer** in Python to determine efficient routes for college buses to pick up students, considering the number of available buses and their capacity. The optimization strategy employed is a variation of the **Nearest Neighbor Clustering** algorithm.

## Objective

The primary goal is to **cluster student pickup locations** into distinct bus routes while adhering to the **bus capacity constraint** and aiming to find a sequence of stops within each route that **minimizes the total travel distance**.

## Methodology

The core logic is encapsulated within the `BusRouteOptimizer` class.

### 1. Initialization (`__init__`)

* Stores the **college location** (as the start/end point for all routes), a list of **student pickup locations**, the **number of available buses**, and the **maximum bus capacity**.

### 2. Distance Calculation (`calculate_distance`)

* Uses the standard **Euclidean distance formula** to find the straight-line distance between any two coordinate points $(x_1, y_1)$ and $(x_2, y_2)$:
    $$d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

### 3. Route Clustering (`nearest_neighbor_clustering`)



This function is the main optimization method. It iterates through the available buses and builds a route for each:

* **Start Point:** Each route begins at the **college location**.
* **Sequential Selection:** From the current position (initially the college, then the last picked-up student), it selects the **nearest unassigned student location** using the `calculate_distance` function.
* **Assignment:** The selected student is assigned to the current bus route, and the student's location becomes the new **current position**.
* **Constraint Check:** This process repeats until either the **bus capacity** is reached or there are no more students left to assign.

This method groups students based on their proximity in a sequential manner, aiming to reduce the distance between consecutive stops.

### 4. Route Distance Calculation (`calculate_route_distance`)

* Calculates the total distance for a single route by summing up the Euclidean distances for the entire path:
    1.  **College** to **First Student Stop**.
    2.  **Between** all **consecutive Student Stops**.
    3.  **Last Student Stop** back to the **College**.

### 5. Visualization and Reporting

* **`visualize_routes`:** Uses `matplotlib.pyplot` to generate a scatter plot showing the college (marked with a red star) and student locations. Each bus route is color-coded, with lines connecting the stops in order, and a dashed line indicating the final return trip to the college.
* **`print_route_details`:** Outputs summary statistics, including the number of students, the distance traveled for each bus, and the total distance for all buses combined.

## Example Usage

The provided code demonstrates two examples:

1.  **Randomized Example:** 45 students scattered randomly, 3 buses, and a capacity of 20 per bus.
2.  **Custom Example:** A smaller, clustered set of 12 students, 2 buses, and a capacity of 8 per bus, demonstrating the clustering effect where geographically grouped students are likely assigned to the same bus.

The output provides the optimized route details and a visual representation of the paths taken by each bus.
```
