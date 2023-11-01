import datetime

# Get the current time
current_time = datetime.datetime.now()

# Extract the hour from the current time
current_hour = current_time.hour

# Define the time ranges for greetings
morning_start = 6
afternoon_start = 12
evening_start = 18

# Determine the appropriate greeting based on the current time
if morning_start <= current_hour < afternoon_start:
    greeting = "Good morning"
elif afternoon_start <= current_hour < evening_start:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# Format the time as a string
time_str = current_time.strftime("%H:%M:%S")

# Print the greeting and the current time
print(f"{greeting}, the current time is {time_str}")
