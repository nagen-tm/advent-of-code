import re

def read_file(filename):
    with open(filename) as file:
        content = file.readlines()
        total = 0
        total_pt_two = 0
        enabled = True
        for line in content:
            multipliers = re.findall("mul\(\d{1,3}\,\d{1,3}\)", line)
            mult_part_two = re.findall("mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", line)
            for group in multipliers:
                nums = re.findall("\d{1,3}\,\d{1,3}", group)
                nums = [int(n) for n in nums[0].split(',')]
                total += nums[0] * nums[1]
            pairs = []
            for i in range(len(mult_part_two)):
                if "don\'t()" in mult_part_two[i]:
                    enabled = False
                elif "do()" in mult_part_two[i]:
                    enabled = True
                elif enabled and "mul" in mult_part_two[i]:
                    pairs.append(mult_part_two[i])
            for group in pairs:
                nums = re.findall("\d{1,3}\,\d{1,3}", group)
                nums = [int(n) for n in nums[0].split(',')]
                total_pt_two += nums[0] * nums[1]
        return total, total_pt_two


print("Example: ", read_file("2024/3/example.txt"))
print("Input: ", read_file("2024/3/input.txt"))