from multiple_child import *

run_cases = [
    (
        Wizard("Ron", 50, 90),
        Archer("Odysseus", 80, 2),
        ["shoot", "shoot", "shoot", "cast"],
        [None, None],
        "not enough arrows",
    ),
    (
        Wizard("Harry", 30, 70),
        Archer("Pericles", 100, 3),
        ["cast", "shoot", "shoot"],
        [10, 75],
    ),
]

submit_cases = run_cases + [
    (
        Wizard("Luna", 65, 49),
        Archer("Paris", 85, 2),
        ["cast", "shoot", "shoot", "cast"],
        [None, None],
        "not enough mana",
    ),
    (
        Wizard("Neville", 55, 45),
        Archer("Hector", 75, 3),
        ["shoot", "cast"],
        [45, 50],
    ),
]


def test(wizard, archer, actions, expected_result, expected_err=None):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Wizard: {wizard.get_name()}, HP: {wizard.get_health()}")
    print(f" * Archer: {archer.get_name()}, HP: {archer.get_health()}")
    print(f"Actions: {actions}")
    print("")

    try:
        for action in actions:
            if action == "cast":
                print(f"{wizard.get_name()} casts a spell at {archer.get_name()}")
                wizard.cast(archer)
            elif action == "shoot":
                print(f"{archer.get_name()} shoots an arrow at {wizard.get_name()}")
                archer.shoot(wizard)
        print("")

        if expected_err:
            print(f"Expected Exception: {expected_err}")
            print("Actual Exception:    None")
            return False

        wizard_hp = wizard.get_health()
        archer_hp = archer.get_health()
        print(f"Expected Wizard HP: {expected_result[0]}")
        print(f"Actual Wizard HP:   {wizard_hp}")
        print(f"Expected Archer HP: {expected_result[1]}")
        print(f"Actual Archer HP:   {archer_hp}")

        if wizard_hp == expected_result[0] and archer_hp == expected_result[1]:
            return True
        else:
            return False

    except Exception as e:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception:   {str(e)}")
        if str(e) == expected_err:
            return True
        else:
            return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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
