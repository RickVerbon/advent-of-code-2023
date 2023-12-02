# The newly-improved calibration document consists of lines of text; 
# each line originally contained a specific calibration value that the Elves now need to recover.
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# Consider your entire calibration document. What is the sum of all of the calibration values?
total = 0

with open("input.txt", "r") as f:
    data = f.readlines()

count = 1
for item in data:
    item = item.strip()
    item = [int(i) for i in item if i.isdigit()]

    if len(item) == 1:
        new_number = str(item[0]) + str(item[0])
        
    elif len(item) > 1:
        first = item[0]
        last = item[-1]
        new_number = str(first) + str(last)
    total += int(new_number)
