# File: main.py
import threading
import time

# Import all necessary classes from the 'models' module
from VIMAN.vehicle_models import Vehicle, Car, Motorcycle, ElectricCar
# Import all service functions from the 'services' module
from VIMAN.vehicle_services import check_vehicle_status, list_vehicles

# ==============================================================================
# Creating and Using Objects
# ==============================================================================
# An object is an instance of a class. 'car1' and 'bike1' are objects.
car1 = Vehicle("Honda", "Civic", 2022, "Red")
bike1 = Vehicle("Kawasaki", "Ninja", 2023, "Green")

print("\n--- Object Information ---")
print(f"Car 1 Info: {car1.get_info()}")
print(f"Bike 1 Info: {bike1.get_info()}")
print("-" * 25)

# Creating objects of the inherited classes
sedan = Car("Tesla", "Model 3", 2024, "Black", 4)
cruiser = Motorcycle("Harley-Davidson", "Iron 883", 2023, "Gray", False)
electric_sedan = ElectricCar("Tesla", "Model Y", 2024, "White", 4, 300)

print("\n--- Polymorphism Example ---")
# We can call 'start_engine' on all three objects, and each one
# will behave differently based on its specific class.
sedan.start_engine()
cruiser.start_engine()
electric_sedan.start_engine()
print("-" * 25)

# ==============================================================================
# Encapsulation & Abstraction
# ==============================================================================
print("\n--- Encapsulation and Abstraction ---")
# '_is_engine_on' is a protected attribute (by convention).
# We should not access it directly. Instead, we use the 'start_engine' and 'stop_engine' methods.
print(f"Is the sedan's engine on? {sedan._is_engine_on}")
sedan.stop_engine()
print(f"Is the sedan's engine on? {sedan._is_engine_on}")

# You cannot access '__secret_code' directly due to name mangling.
try:
    print(sedan.__secret_code)
except AttributeError as e:
    print(f"Error demonstrating encapsulation: {e}")

# The 'get_info' method is an example of abstraction.
# We don't need to know how the info string is constructed, we just call the method.
print(f"Sedan Info: {sedan.get_info()}")
print("-" * 25)

# ==============================================================================
# Using the Services File
# ==============================================================================

# Example 1: Calling 'check_vehicle_status' with a single vehicle object.
# The parameter for this function is a 'Vehicle' type, and we can pass any
# object that inherits from 'Vehicle', like 'sedan' or 'cruiser'.
print("\n--- Calling Service Functions ---")
check_vehicle_status(sedan)
check_vehicle_status(cruiser)

# Example 2: Calling 'list_vehicles' with a list of vehicle objects.
# The parameter is a list, so we create a list containing all our vehicle objects.
all_vehicles = [car1, bike1, sedan, cruiser, electric_sedan]
list_vehicles(all_vehicles)

# ==============================================================================
# Multithreading & Packages
# ==============================================================================
def run_maintenance_task():
    """A background task function."""
    print("Starting background maintenance task...")
    time.sleep(3)# Simulate a long-running task
    print("Background maintenance task completed.")

print("\n--- Multithreading & Packages ---")
# Create a thread for the background task
maintenance_thread = threading.Thread(target=run_maintenance_task)

# Start the thread. This runs the task concurrently.
maintenance_thread.start()

# While the maintenance task is running, the main program can continue.
print("Main program continues running...")
maintenance_thread.join() # Wait for the thread to finish before exiting the main program
print("Main program finished.")
print("-" * 25)
