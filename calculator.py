# ===  Building a simple Calculator App ===
# Goal: Make sure it works correctly, safely, and meets user expectations.

# Here's  main calculator logic:
class Calculator:
    def add(self, a, b):
        return a + b  # Adds two numbers

    def subtract(self, a, b):
        return a - b  # Subtracts one number from another

    def multiply(self, a, b):
        return a * b  # Multiplies two numbers

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"  # Handles risky division
        return a / b

# === 1. UNIT TESTING ===
# test each operation by itself to make sure they're individually correct.
print("=== Unit Testing ===")
calc = Calculator()
print("Add 5 + 3 =", calc.add(5, 3))
print("Subtract 10 - 4 =", calc.subtract(10, 4))
print("Multiply 2 * 3 =", calc.multiply(2, 3))
print("Divide 8 / 2 =", calc.divide(8, 2))
print("Divide 5 / 0 =", calc.divide(5, 0))  # Testing division safety

# === 2. INTEGRATION TESTING ===
# chain some operations together 
print("\n=== Integration Testing ===")
result = calc.add(10, 5)        # First, the user adds something
result = calc.multiply(result, 2)  # Then multiplies the result
print("Integrated Result ( (10 + 5) * 2 ) =", result)

# === 3. VALIDATION TESTING ===
# Suppose app has a rule: no negative results should be allowed on screen.
print("\n=== Validation Testing ===")
def validate_non_negative(result):
    if result < 0:
        return "Validation Failed: Negative result not allowed"
    return "Validation Passed"

print("Subtract 5 - 10:", validate_non_negative(calc.subtract(5, 10)))  # Should warn
print("Subtract 10 - 5:", validate_non_negative(calc.subtract(10, 5)))  # Should pass

# === 4. SYSTEM TESTING ===
# test a full user journey: Add → Multiply → Divide — all in one flow.
print("\n=== System Testing ===")
a = calc.add(5, 3)        # 5 + 3 = 8
b = calc.multiply(a, 2)   # 8 * 2 = 16
c = calc.divide(b, 4)     # 16 / 4 = 4.0
print("Complete User Flow Result =", c)

# === 5. REGRESSION TESTING ===
# you recently updated the divide function to handle floats better.
# You now want to ensure old functionality still works.
print("\n=== Regression Testing ===")
print("Divide 6 / 3 =", calc.divide(6, 3))  # Should still be 2.0
print("Divide 9 / 3 =", calc.divide(9, 3))  # Should still be 3.0

# === 6. SMOKE TESTING ===
#quick check to confirm the app starts and basic stuff works.
print("\n=== Smoke Testing ===")
try:
    print("Quick test: 1 + 1 =", calc.add(1, 1))
except Exception as e:
    print("Smoke Test Failed:", e)

# === 7. WebApp Testing Simulation ===
# this is a web calculator, now test user input for errors.
print("\n=== WebApp Testing Simulation ===")
def web_input(a, b):
    # If user enters something weird like "five", we catch it
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Please enter numbers only"
    return f"Web input result: {calc.add(a, b)}"

print(web_input("five", 5))  # Should return an error
print(web_input(5, 5))       # Should work fine
