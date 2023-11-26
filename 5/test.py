from main import *

run_cases = [
    (Sword("bronze"), Sword("bronze"), "iron"),
    (Sword("iron"), Sword("iron"), "steel"),
]

submit_cases = run_cases + [
    (Sword("bronze"), Sword("iron"), "can not craft"),
    (Sword("iron"), Sword("bronze"), "can not craft"),
    (Sword("steel"), Sword("steel"), "can not craft"),
    (Sword("bronze"), Sword("steel"), "can not craft"),
    (Sword("steel"), Sword("iron"), "can not craft"),
]


def test(sword1, sword2, expected_result):
    print("---------------------------------")
    print(f"Crafting a {sword1.sword_type} sword with a {sword2.sword_type} sword...")
    print(f"Expecting: {expected_result} sword")
    try:
        sword3 = sword1 + sword2
        print(f"A new {sword3.sword_type} sword was crafted")
        result = sword3.sword_type
    except Exception as e:
        print(e)
        result = str(e)

    if result == expected_result:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
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
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
