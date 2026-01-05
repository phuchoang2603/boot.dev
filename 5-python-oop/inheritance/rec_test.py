from rec import *

run_cases = [
    ((2, 4), 8, 12),
    ((5,), 25, 20),
]

submit_cases = run_cases + [
    ((1, 1), 1, 4),
    ((3, 4), 12, 14),
    ((6, 7), 42, 26),
    ((8,), 64, 32),
    ((9, 10), 90, 38),
]


def test(inputs, expected_area, expected_perimeter):
    print("---------------------------------")
    if len(inputs) == 2:  # Rectangle
        shape = Rectangle(*inputs)
        shape_type = "Rectangle"
    else:  # Square
        shape = Square(inputs[0])
        shape_type = "Square"

    print(f"Testing {shape_type} with inputs {inputs}")
    area = shape.get_area()
    perimeter = shape.get_perimeter()
    print(f"Expected area: {expected_area}")
    print(f"Actual area:   {area}")
    print(f"Expected perimeter: {expected_perimeter}")
    print(f"Actual perimeter:   {perimeter}")

    if area != expected_area or perimeter != expected_perimeter:
        print("Fail")
        return False
    else:
        print("Pass")
        return True


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
