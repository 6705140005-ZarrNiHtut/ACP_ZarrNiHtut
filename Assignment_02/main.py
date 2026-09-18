#6705140005_Zarr Ni Htut
from rental import Vehicle, Renter, ElectricCar, Motorbike


print("=== CampusWheels Vehicle Rental ===")

# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "2EV567", 75)
motorbike = Motorbike("Honda", "Click", "3MB890", 125)

# Create renter
renter = Renter("John", 12345)

print("\nVehicles:")
print(car)
print(electric_car)
print(motorbike)

# Rent a vehicle
print("\nRenting Toyota Yaris...")
car.rent()
renter.rented.append(car)
print(car)

# Return the vehicle
print("\nReturning Toyota Yaris...")
car.return_vehicle()
renter.rented.remove(car)
print(car)

# Test invalid name
print("\nTesting invalid renter name...")

try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("ValueError caught:", e)

# Test invalid license
print("\nTesting invalid license number...")

try:
    bad_renter = Renter("Alice", 0)
except ValueError as e:
    print("ValueError caught:", e)

# Test changing values
print("\nTesting property validation...")

try:
    renter.name = ""
except ValueError as e:
    print("ValueError caught:", e)

try:
    renter.license_no = -10
except ValueError as e:
    print("ValueError caught:", e)

# Polymorphism
print("\n=== Polymorphism Test ===")

vehicles = [
    Vehicle("Toyota", "Yaris", "1AB234"),
    ElectricCar("Tesla", "Model 3", "2EV567", 75),
    Motorbike("Honda", "Click", "3MB890", 125)
]

for vehicle in vehicles:
    print(vehicle)
