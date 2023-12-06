#part one: attempted nested for loops that was okay for the example, killed the computer for the input
# working towards using functions for small sections

file = open('example.txt','r')
content = file.read()

# get the seed numbers and section data
def parse_data(data):
    sections = content.split('\n\n')
    empty, seeds = sections[0].split(': ')
    seed_nums = seeds.split()
    for i, seeds in enumerate(seed_nums):
        seed_nums[i] = int(seeds)
    return seed_nums, sections

# put maps into dict
def get_maps(sections):
    section_maps = {}
    for index in range(1,8):
        sect_key, sect_nums = sections[index].split(':\n')
        maps = sect_nums.split('\n')
        section_maps[sect_key] = maps
    return section_maps

# loop through maps and create dict
def get_range(maps):
    map_dict = {}
    for i, map in enumerate(maps):
        dest, source, range_length = map.split()
        count = 0
        for times in range(int(range_length)):
            map_dict[int(source) + count] = int(dest) + count
            count += 1
    return map_dict
     

def find_min(seed_nums, section_nums):
    current_num = 0
    locations = []
    for num in seed_nums:
        current_num = section_nums.get(0, {}).get(num, num)
        current_num = section_nums.get(1, {}).get(current_num, current_num)
        current_num = section_nums.get(2, {}).get(current_num, current_num)
        current_num = section_nums.get(3, {}).get(current_num, current_num)
        current_num = section_nums.get(4, {}).get(current_num, current_num)
        current_num = section_nums.get(5, {}).get(current_num, current_num)
        current_num = section_nums.get(6, {}).get(current_num, current_num)
        locations.append(current_num)
    min_num = min(locations)
    return min_num

def run(content):
    section_nums = {}
    seeds, section = parse_data(content)
    section_maps = get_maps(section)
    for i, values in enumerate(section_maps.values()):
        section_nums[i] = get_range(values)
    min = find_min(seeds, section_nums)

    print(min)

run(content)

file.close()