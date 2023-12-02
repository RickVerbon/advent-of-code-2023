# The newly-improved calibration document consists of lines of text; 
# each line originally contained a specific calibration value that the Elves now need to recover.
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# Consider your entire calibration document. What is the sum of all of the calibration values?
total = 0

with open("input.txt", "r") as f:
    data = f.readlines()

for item in data:
    item = item.strip()
    numbers = [int(i) for i in item if i.isdigit()]
    if numbers:
        new_number = str(numbers[0]) + str(numbers[-1])
        total += int(new_number)

print(total)