import time

# Sample user database
users = {
    "admin": "12345",
    "user1": "pass@123"
}

# Track login attempts and lock status
attempts = {}
lock_time = {}

MAX_ATTEMPTS = 3
LOCK_DURATION = 30  # seconds

def login(username, password):
    current_time = time.time()

    # Check if account is locked
    if username in lock_time:
        if current_time < lock_time[username]:
            remaining = int(lock_time[username] - current_time)
            return f"Account locked. Try again after {remaining} seconds."
        else:
            # Unlock account after time expires
            del lock_time[username]
            attempts[username] = 0

    # Initialize attempts if first time
    if username not in attempts:
        attempts[username] = 0

    # Validate user
    if username in users and users[username] == password:
        attempts[username] = 0
        return "✅ Login successful!"

    # Wrong password case
    attempts[username] += 1
    remaining_attempts = MAX_ATTEMPTS - attempts[username]

    if remaining_attempts <= 0:
        lock_time[username] = current_time + LOCK_DURATION
        return "❌ Too many failed attempts. Account locked for 30 seconds."

    return f"❌ Wrong password. {remaining_attempts} attempts left."


# ---------------- Demo ----------------
while True:
    u = input("Username: ")
    p = input("Password: ")

    print(login(u, p))
    print("-" * 40)