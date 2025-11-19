import sys

if len(sys.argv) == 5:
    car_number = sys.argv[1]
    owner_name = sys.argv[2]
    vehicle_type = sys.argv[3]
    rc_expiry_year = sys.argv[4]
    print("User inputs provided")
else:
    car_number = "1234"
    owner_name = "xyz"
    vehicle_type = "abc"
    rc_expiry_year = "2025"
    print("Default inputs used")

print("Vehicle Registration Info:")
print("-------------------------")
print(f"Car Number: {car_number}")
print(f"Owner Name: {owner_name}")
print(f"Vehicle Type: {vehicle_type}")
print(f"RC Expiry Year: {rc_expiry_year}")
