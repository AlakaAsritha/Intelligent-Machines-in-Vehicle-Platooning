import pygame
import random
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Geographic Routing Protocol Visualization")
FONT = pygame.font.SysFont("Arial", 16)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 200, 200)

class Vehicle:
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.neighbors = []
        self.speed = random.uniform(1, 5)  # Speed in units per second
        self.latency = random.uniform(10, 100)  # Latency in milliseconds
        self.reliability = random.uniform(0.7, 1.0)  # Reliability between 0.7 and 1.0
        self.network_efficiency = self.calculate_network_efficiency()

    def calculate_network_efficiency(self):
        """Calculate network efficiency based on speed and reliability."""
        return self.speed * self.reliability

    def update_neighbors(self, all_vehicles, threshold=150):
        """Update neighbors based on a distance threshold."""
        self.neighbors = [v for v in all_vehicles if v.id != self.id and self.distance(v) < threshold]

    def distance(self, other_vehicle):
        """Calculate Euclidean distance to another vehicle."""
        return math.sqrt((self.position[0] - other_vehicle.position[0]) ** 2 + 
                         (self.position[1] - other_vehicle.position[1]) ** 2)

    def send_message(self, destination):
        """Send message to destination vehicle (visualized as an arrow)."""
        pygame.draw.line(screen, CYAN, self.position, destination.position, 2)
        draw_arrow(screen, self.position, destination.position, CYAN)
        pygame.display.flip()
        pygame.time.delay(300)

        # Print communication metrics
        print(f"Vehicle {self.id} sending message to Vehicle {destination.id}:")
        print(f"  Speed: {self.speed:.2f} units/s")
        print(f"  Latency: {self.latency:.2f} ms")
        print(f"  Reliability: {self.reliability:.2f}")
        print(f"  Network Efficiency: {self.network_efficiency:.2f}")

class GeographicRoutingProtocol:
    def route(self, sender, destination, visited=None):
        """Route message using Geographic Routing Protocol with neighbor constraint."""
        if visited is None:
            visited = set()
        
        # Check if we've already visited this vehicle to prevent loops
        if sender.id in visited:
            print(f"Vehicle {sender.id} already visited; stopping recursion.")
            return
        
        print(f"Routing from Vehicle {sender.id} to Vehicle {destination.id}")
        visited.add(sender.id)

        if not sender.neighbors:
            print(f"Vehicle {sender.id} has no neighbors to route to.")
            return
        
        # Filter only neighbors who are closer to the destination
        eligible_neighbors = [v for v in sender.neighbors if v.distance(destination) < sender.distance(destination)]
        
        # If there are no eligible neighbors, stop routing
        if not eligible_neighbors:
            print(f"No eligible closer neighbors found for Vehicle {sender.id}. Routing stops.")
            return
        
        # Find the closest eligible neighbor
        closest_neighbor = min(eligible_neighbors, key=lambda v: v.distance(destination))
        
        # Visualize message passing
        sender.send_message(closest_neighbor)

        # If destination is reached
        if closest_neighbor.id == destination.id:
            print(f"Vehicle {destination.id} received the message.")
            return

        # Recursive call to continue routing
        self.route(closest_neighbor, destination, visited)

def draw_arrow(screen, start_pos, end_pos, color, arrow_size=10):
    """Draw an arrow from start_pos to end_pos."""
    pygame.draw.line(screen, color, start_pos, end_pos, 2)
    angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
    arrow_end1 = (end_pos[0] - arrow_size * math.cos(angle - math.pi / 6),
                  end_pos[1] - arrow_size * math.sin(angle - math.pi / 6))
    arrow_end2 = (end_pos[0] - arrow_size * math.cos(angle + math.pi / 6),
                  end_pos[1] - arrow_size * math.sin(angle + math.pi / 6))
    pygame.draw.polygon(screen, color, [end_pos, arrow_end1, arrow_end2])

def find_farthest_vehicles(vehicles):
    """Find the two farthest-apart vehicles."""
    max_distance = 0
    farthest_pair = (vehicles[0], vehicles[1])
    for i in range(len(vehicles)):
        for j in range(i + 1, len(vehicles)):
            dist = vehicles[i].distance(vehicles[j])
            if dist > max_distance:
                max_distance = dist
                farthest_pair = (vehicles[i], vehicles[j])
    return farthest_pair

def simulate_grp(num_vehicles):
    vehicles = [Vehicle(i, (random.randint(50, 550), random.randint(50, 550))) for i in range(num_vehicles)]
    
    # Update neighbors for each vehicle
    for vehicle in vehicles:
        vehicle.update_neighbors(vehicles)

    # Find the farthest-apart vehicles as sender and destination
    sender, destination = find_farthest_vehicles(vehicles)
    
    running = True
    while running:
        screen.fill(WHITE)

        # Draw vehicles and neighbors
        for vehicle in vehicles:
            color = BLUE
            if vehicle == sender:
                color = GREEN
            elif vehicle == destination:
                color = RED
            pygame.draw.circle(screen, color, vehicle.position, 10)
            label = FONT.render(str(vehicle.id), True, WHITE)
            screen.blit(label, (vehicle.position[0] - 5, vehicle.position[1] - 5))
            
            # Draw neighbor connections
            for neighbor in vehicle.neighbors:
                pygame.draw.line(screen, CYAN, vehicle.position, neighbor.position, 1)

        pygame.display.flip()

        # Start routing visualization
        grp = GeographicRoutingProtocol()
        grp.route(sender, destination)

        # Main loop to keep the window open
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

# Run the simulation
simulate_grp(10)
