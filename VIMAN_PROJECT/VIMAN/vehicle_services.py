from .vehicle_models import Vehicle 

def check_vehicle_status(vehicle: Vehicle):
    """
    Service function to check a vehicle's status, demonstrating abstraction.
    This function doesn't need to know if the vehicle is a Car or a Motorcycle,
    it just needs a Vehicle object.
    """
    print("--- Vehicle Status Check ---")
    print(f"Vehicle Info: {vehicle.get_info()}")
    print(f"Engine Running: {'Yes' if vehicle._is_engine_on else 'Yes'}")
    print("-" * 25)

def list_vehicles(vehicles_list: list):
    """
    Service function to list details for a collection of vehicles.
    This demonstrates processing multiple objects of different types.
    """
    print("\n--- Listing All Vehicles ---")
    for idx, vehicle in enumerate(vehicles_list):
        print(f"{idx+1}. {vehicle.get_info()}")
    print("-" * 25)
