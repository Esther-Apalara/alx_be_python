def convert_hours_to_seconds(hours):
    """Convert hours to seconds."""
    return hours * 3600

# Assign the number of hours
hours = 2

# Perform the conversion
seconds = convert_hours_to_seconds(hours)

# Print the result
print(f"{hours} hour(s) is {seconds} seconds.")