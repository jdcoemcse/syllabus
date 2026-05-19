import matplotlib.pyplot as plt
import numpy as np

def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], label="Line")

def draw_rectangle(x, y, width, height):
    rectangle = plt.Rectangle((x, y), width, height, fill=False, edgecolor='blue', label="Rectangle")
    plt.gca().add_patch(rectangle)

def draw_circle(x, y, radius):
    circle = plt.Circle((x, y), radius, fill=False, edgecolor='red', label="Circle")
    plt.gca().add_patch(circle)

def draw_polygon(vertices):
    polygon = plt.Polygon(vertices, fill=False, edgecolor='green', label="Polygon")
    plt.gca().add_patch(polygon)

def create_2d_objects():
    plt.figure(figsize=(6,6))
    
    # Line
    draw_line(0, 0, 5, 5)
    # Rectangle
    draw_rectangle(1, 1, 4, 2)
    # Circle
    draw_circle(3, 3, 2)
    # Polygon
    vertices = [(2, 5), (3, 8), (5, 7), (4, 4)]
    draw_polygon(vertices)
    
    # Display settings
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-1, 7)
    plt.ylim(-1, 9)
    
    # Workaround for legend
    handles, labels = plt.gca().get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))
    plt.legend(unique_labels.values(), unique_labels.keys(), loc="upper left")
    
    plt.title("2D Objects in Python")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Run the function to create and display 2D objects
create_2d_objects()
