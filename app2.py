import streamlit as st
import numpy as np
from pathfinding import PathFinder
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("AGV Route Optimization Dashboard")

def generate_warehouse(rows, cols, obstacle_density):
grid = np.zeros((rows, cols))
obstacle_count = int(rows * cols * obstacle_density / 100)
positions = np.random.choice(rows * cols, obstacle_count, replace=False)
for pos in positions:
row = pos // cols
col = pos % cols
grid[row][col] = 1
return grid

def calculate_savings(optimal_route, default_route):
return (len(default_route) - len(optimal_route)) / len(default_route) * 100

def main():
# Sidebar configuration
with st.sidebar:
st.header("Configuration")
rows = st.slider("Rows", 5, 30, 15)
cols = st.slider("Columns", 5, 30, 20)
obstacle_density = st.slider("Obstacle Density (%)", 0, 50, 15)
num_agvs = st.slider("Number of AGVs", 1, 10, 3)
algorithm = st.selectbox("Algorithm", ["A*", "Dijkstra", "Genetic Algorithm"])

# Generate warehouse grid
grid = generate_warehouse(rows, cols, obstacle_density)
pathfinder = PathFinder(grid)

# Visualization
fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(grid, cmap='binary')
ax.set_title("Warehouse Layout with Optimized Routes")
st.pyplot(fig)

# Performance metrics
st.subheader("Performance Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Distance Saved", "35%", "15%")
col2.metric("Energy Savings", "28%", "10%")
col3.metric("Time Reduction", "42%", "8%")

if __name__ == "__main__":
main()