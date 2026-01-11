from siege import *

run_cases = [
    (Siege(100, 10), 100, 4, 40, None),
    (BatteringRam(100, 10, 2000, 5), 100, 5, 70, 10),
    (Catapult(100, 10, 2), 100, 6, 60, 2),
]

submit_cases = run_cases + [
    (Siege(60, 5), 100, 2, 40, None),
    (BatteringRam(80, 5, 2000, 4), 100, 4, 100, 8),
    (Catapult(90, 4, 3), 100, 10, 250, 3),
]


def test(vehicle, distance, food_price, expected_cost, expected_cargo_volume):
    try:
        vehicle_type = vehicle.__class__.__name__
        actual_cost = int(vehicle.get_trip_cost(distance, food_price))
        actual_cargo_volume = vehicle.get_cargo_volume()
        if actual_cargo_volume is not None:
            actual_cargo_volume = int(actual_cargo_volume)
        print("---------------------------------")
        print(f"Testing {vehicle_type}")
        print(f" * Max Speed:  {vehicle.max_speed} kph")
        print(f" * Efficiency: {vehicle.efficiency} km/food")
        print(f"Expected Cargo Volume: {expected_cargo_volume}")
        print(f"Actual Cargo Volume:   {actual_cargo_volume}")
        print("")
        print(f"Inputs:")
        print(f" * Distance: {distance} km")
        print(f" * Price: {food_price} per food")
        print(f"Expected Trip Cost: {expected_cost} ")
        print(f"Actual Trip Cost:   {actual_cost}")
        if (
            actual_cost == expected_cost
            and expected_cargo_volume == actual_cargo_volume
        ):
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
