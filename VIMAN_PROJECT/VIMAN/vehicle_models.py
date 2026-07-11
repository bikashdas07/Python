# This file contains all the class definitions for the Vehicle Management System.

# ==============================================================================
# 1. Classes, Objects, and Constructors (__init__)
# ==============================================================================
# A Class is a blueprint for creating objects.
# The 'Vehicle' class is our blueprint for all vehicles.

class Vehicle:
    """
    A base class representing a generic vehicle.
    This class demonstrates the core principles of OOP.
    """
    
    # The constructor (__init__) is a special method that is automatically called
    # when a new object is created. It initializes the object's attributes.
    def __init__(self, brand, model, year, color):
        print(f"Constructor called for {brand} {model}.")
        self.brand = brand      # Attribute 1: brand
        self.model = model      # Attribute 2: model
        self.year = year        # Attribute 3: year
        self.color = color      # Attribute 4: color
        self._is_engine_on = False  # Encapsulated attribute (private-like)
        self.__secret_code = "ABC123" # Name-mangled attribute (truly private)

    # A method is a function that belongs to a class. It operates on the object's data.
    def start_engine(self):
        if not self._is_engine_on:
            self._is_engine_on = True
            print(f"The {self.brand} {self.model}'s engine is now running.")
        else:
            print(f"The {self.brand} {self.model}'s engine is already running.")
    
    def stop_engine(self):
        if self._is_engine_on:
            self._is_engine_on = False
            print(f"The {self.brand} {self.model}'s engine has been turned off.")
        else:
            print(f"The {self.brand} {self.model}'s engine is already off.")
    
    # Abstraction: This method hides the internal implementation of how the info is displayed.
    # The user only needs to call 'get_info()' and not worry about the details.
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}"

# ==============================================================================
# 2. Inheritance
# ==============================================================================
# Inheritance allows a new class (child) to inherit attributes and methods
# from an existing class (parent). This promotes code reuse.

class Car(Vehicle):
    """
    A child class inheriting from Vehicle. It has all Vehicle's attributes and methods.
    """
    def __init__(self, brand, model, year, color, num_doors):
        # The 'super()' function calls the constructor of the parent class.
        super().__init__(brand, model, year, color)
        self.num_doors = num_doors # New attribute specific to Car

    # This method is specific to the Car class.
    def honk(self):
        print(f"The {self.brand} {self.model} goes 'BEEP BEEP!'")

class Motorcycle(Vehicle):
    """
    Another child class inheriting from Vehicle.
    """
    def __init__(self, brand, model, year, color, has_sidecar):
        super().__init__(brand, model, year, color)
        self.has_sidecar = has_sidecar # New attribute specific to Motorcycle
    
    # This method is specific to the Motorcycle class.
    def wheelie(self):
        print(f"The {self.brand} {self.model} pops a wheelie!")

# ==============================================================================
# 3. Polymorphism
# ==============================================================================
# Polymorphism means "many forms." It allows objects of different classes
# to be treated as objects of a common class, often by sharing a method name.

class ElectricCar(Car):
    def __init__(self, brand, model, year, color, num_doors, battery_range):
        super().__init__(brand, model, year, color, num_doors)
        self.battery_range = battery_range
    
    # Polymorphism: This method has the same name as the parent method
    # but provides a specific implementation for an electric car.
    def start_engine(self):
        if not self._is_engine_on:
            self._is_engine_on = True
            print(f"The {self.brand} {self.model}'s electric motor hums to life.")
        else:
            print(f"The {self.brand} {self.model}'s electric motor is already humming.")
