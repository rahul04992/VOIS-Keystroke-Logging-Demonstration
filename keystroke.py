import time

def record_keystrokes(password):
    timings = []
    print("Type your password:")

    for char in password:
        start = time.time()
        input_char = input()
        end = time.time()

        if input_char != char:
            print("Wrong key pressed!")
            return None

        timings.append(end - start)

    return timings

# Registration
password = "hello"
print("=== Registration ===")
registered_timings = record_keystrokes(password)

if registered_timings:
    print("Keystroke pattern saved!")

# Login
print("\n=== Login ===")
login_timings = record_keystrokes(password)

# Simple comparison
if login_timings:
    difference = sum(abs(a - b) for a, b in zip(registered_timings, login_timings))
    threshold = 1.5

    if difference < threshold:
        print("Login Successful!")
    else:
        print("Login Failed: Typing pattern mismatch!")