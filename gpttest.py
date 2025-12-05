import re

def pad_to_four_digits(input_str):
    # Define the regex pattern to check for 1-4 leading digits
    pattern = r'^(\d{1,4})(\D|$)'

    # Use re.match to find the leading digits
    match = re.match(pattern, input_str)

    # Starts with hours, padding out to 4
    if match:
        leading_digits = match.group(1)
        hours = f"{leading_digits.zfill(4)}h"
        formatted_input = f"PT{hours}"

    # Then checks if there's anything at the end, if not, pads out to 2 and adds an m for minutes
        if len(input_str) == len(match.group()):
            formatted_input += "00m"
        else:
            minutes = input_str[len(leading_digits): -1].zfill(2)
            formatted_input += f"{minutes}m"

        return formatted_input.upper()
    else:
        return input_str

# Example usage:
input_str1 = "37h"  # This will return "0123abc"
input_str2 = "01h15m"  # This will return "4567xyz"

print(pad_to_four_digits(input_str1))
print(pad_to_four_digits(input_str2))
