import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define distance from point A to point B (in km)
distance_AB = 1205

# Define the objective function to minimize fuel consumption
def objective_function(speed):
    # Define the fuel consumption equation (y = x^4)
    fuel_consumption = np.power(speed, 2)
    return fuel_consumption

# Define constraints for travel time (e.g., truck should reach point B within 36 hours)
def constraint(time_limit):
    def time_constraint(speed):
        travel_time = distance_AB / speed
        return time_limit - travel_time
    return {'type': 'ineq', 'fun': time_constraint}

# Initial guess for speed (starting point for optimization)
initial_guess = 1  # Initial guess for speed (km/h)

# Define the maximum time allowed to reach point B (in hours)
max_time = 36  # Increased maximum time to allow more flexibility

# Set bounds for speed (optional but can help guide the optimization)
bounds = [(0, None)]  # Speed should be non-negative

# Optimize the objective function subject to the constraint
result = minimize(objective_function, initial_guess, constraints=constraint(max_time), bounds=bounds)

# Extract the optimal speed
optimal_speed = result.x[0]

# Print the optimal speed and corresponding fuel consumption
print(f"Optimal Speed: {optimal_speed} km/h")
print(f"Corresponding Fuel Consumption: {objective_function(optimal_speed)}")

# Plot the fuel consumption function y = x^4
speed_range = np.linspace(0, 100, 1000)  # Range of speeds for plotting
fuel_consumption_values = np.power(speed_range, 4)
plt.plot(speed_range, fuel_consumption_values, label='Fuel Consumption ($x^4$)')
plt.xlabel('Speed (km/h)')
plt.ylabel('Fuel Consumption')
plt.title('Fuel Consumption vs Speed')
plt.grid(True)

# Mark the optimal speed on the plot
plt.axvline(x=optimal_speed, color='r', linestyle='--', label='Optimal Speed')
plt.legend()
plt.show()
