import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import random

class BusRouteOptimizer:
    def __init__(self, college_location, student_locations, num_buses=2, bus_capacity=30):
        """
        Initialize the bus route optimizer
        
        Parameters:
        - college_location: tuple (x, y) coordinates of college
        - student_locations: list of tuples [(x, y), ...] student pickup points
        - num_buses: number of buses available
        - bus_capacity: maximum students per bus
        """
        self.college = college_location
        self.students = student_locations.copy()  
        self.num_buses = num_buses
        self.bus_capacity = bus_capacity
        self.routes = []
        
    def calculate_distance(self, point1, point2):
        """Calculate Euclidean distance between two points"""
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    def nearest_neighbor_clustering(self):
        """Cluster students into bus routes using nearest neighbor approach"""
        remaining_students = self.students.copy()
        self.routes = []
        
        for bus_num in range(self.num_buses):
            if not remaining_students:
                break
                
            route = []
            current_pos = self.college
            
            
            while len(route) < self.bus_capacity and remaining_students:
                
                nearest_idx = min(range(len(remaining_students)), 
                                key=lambda i: self.calculate_distance(current_pos, remaining_students[i]))
                
                nearest_student = remaining_students.pop(nearest_idx)
                route.append(nearest_student)
                current_pos = nearest_student
            
            self.routes.append(route)
        
        return self.routes
    
    def calculate_route_distance(self, route):
        """Calculate total distance for a route"""
        if not route:
            return 0
        
        total_distance = self.calculate_distance(self.college, route[0])
        
        for i in range(len(route) - 1):
            total_distance += self.calculate_distance(route[i], route[i+1])
        
        total_distance += self.calculate_distance(route[-1], self.college)
        
        return total_distance
    
    def get_route_statistics(self):
        """Get statistics about the optimized routes"""
        stats = []
        total_distance = 0
        
        for i, route in enumerate(self.routes):
            distance = self.calculate_route_distance(route)
            total_distance += distance
            stats.append({
                'bus': i + 1,
                'students': len(route),
                'distance': round(distance, 2)
            })
        
        return stats, round(total_distance, 2)
    
    def visualize_routes(self, figsize=(12, 8)):
        """Visualize the optimized bus routes"""
        plt.figure(figsize=figsize)
        colors = plt.cm.Set3(np.linspace(0, 1, self.num_buses))
        
        plt.plot(self.college[0], self.college[1], 'r*', markersize=25, 
                label='College', zorder=5)
        
        for bus_num, route in enumerate(self.routes):
            if not route:
                continue
            
            color = colors[bus_num]
            

            route_x = [loc[0] for loc in route]
            route_y = [loc[1] for loc in route]
            plt.scatter(route_x, route_y, c=[color], s=100, 
                       label=f'Bus {bus_num + 1} ({len(route)} students)', 
                       edgecolors='black', linewidth=1.5, zorder=3)
            

            plt.plot([self.college[0], route[0][0]], 
                    [self.college[1], route[0][1]], 
                    c=color, linewidth=2, alpha=0.6, zorder=1)
            

            for i in range(len(route) - 1):
                plt.plot([route[i][0], route[i+1][0]], 
                        [route[i][1], route[i+1][1]], 
                        c=color, linewidth=2, alpha=0.6, zorder=1)
            

            plt.plot([route[-1][0], self.college[0]], 
                    [route[-1][1], self.college[1]], 
                    c=color, linewidth=2, linestyle='--', alpha=0.6, zorder=1)
        
        plt.xlabel('X Coordinate (km)', fontsize=12)
        plt.ylabel('Y Coordinate (km)', fontsize=12)
        plt.title('Optimized College Bus Routes', fontsize=14, fontweight='bold')
        plt.legend(loc='upper right', fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    
    def print_route_details(self):
        """Print detailed route information"""
        stats, total_distance = self.get_route_statistics()
        
        print("=" * 50)
        print("BUS ROUTE OPTIMIZATION RESULTS")
        print("=" * 50)
        
        for stat in stats:
            print(f"\nBus {stat['bus']}:")
            print(f"  Students: {stat['students']}/{self.bus_capacity}")
            print(f"  Route Distance: {stat['distance']} km")
        
        print("\n" + "=" * 50)
        print(f"Total Distance (All Buses): {total_distance} km")
        print(f"Total Students: {sum(len(route) for route in self.routes)}")  
        print("=" * 50)



if __name__ == "__main__":

    random.seed(42)
    

    college = (50, 50)
    
    num_students = 45
    student_locations = [(random.uniform(10, 90), random.uniform(10, 90)) 
                         for _ in range(num_students)]
    

    optimizer = BusRouteOptimizer(
        college_location=college,
        student_locations=student_locations,
        num_buses=3,
        bus_capacity=20
    )
    

    print("Optimizing bus routes...")
    optimizer.nearest_neighbor_clustering()
    

    optimizer.print_route_details()
    

    optimizer.visualize_routes()
    

    print("\n\n" + "="*50)
    print("CUSTOM EXAMPLE")
    print("="*50)
    
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
    
    optimizer2.nearest_neighbor_clustering()
    optimizer2.print_route_details()
    optimizer2.visualize_routes(figsize=(10, 8))
