import sys

def print_vehicle_info():
    if len(sys.argv) != 5:
        print("Usage: python vehicle_registration.py <car_number> <owner_name> <vehicle_type> <rc_expiry_year>")
        sys.exit(1)

    car_number = sys.argv[1]
    owner_name = sys.argv[2]
    vehicle_type = sys.argv[3]
    rc_expiry_year = sys.argv[4]

    print("Vehicle Registration Info:")
    print("-------------------------")
    print(f"Car Number: {car_number}")
    print(f"Owner Name: {owner_name}")
    print(f"Vehicle Type: {vehicle_type}")
    print(f"RC Expiry Year: {rc_expiry_year}")

if __name__ == "__main__":
    print_vehicle_info()

