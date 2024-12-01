file = open('input.txt','r')
content = file.readlines()

left_list = []
right_list = []
for line in content:
    one, empty, empty, two = line.split(' ')
    left_list.append(int(one))
    right_list.append(int(two.rstrip()))

sorted_left = sorted(left_list)
sorted_right = sorted(right_list)

sum_part_one = 0
for i in range(len(sorted_left)):
    if sorted_left[i] > sorted_right[i]:
        sum_part_one += sorted_left[i] - sorted_right[i]
    elif sorted_left[i] < sorted_right[i]:
        sum_part_one += sorted_right[i] - sorted_left[i]

sum_part_two = 0
for i in range(len(left_list)):
    num_count = right_list.count(left_list[i])
    sum_part_two += left_list[i] * num_count

print(sum_part_one)
print(sum_part_two)