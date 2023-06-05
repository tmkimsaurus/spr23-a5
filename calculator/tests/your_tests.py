#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks that the program outputs "8" for an input of "4 + 4"
assert run("4 + 4").output == "8"
# Checks that the program outputs "0" for an input of "2 / 5"
assert run("2 / 5").output == "0"
# Checks that the program fails (correctly errors) for input "2+5"
assert run("2+5").exit_status != 0

###

print("All tests passed!")
