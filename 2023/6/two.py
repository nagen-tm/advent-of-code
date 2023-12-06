#part two: 

file = open('example.txt','r')
content = file.read()
# put race and distance in dictionary
def parse_data(data):
    race = {}
    times, distances = content.split('\n')
    empty, time = times.split(':')
    empty, distance = distances.split(':')
    time = "".join(time.split())
    distance = "".join(distance.split())
    race[time] = distance
    return race

# put maps into dict
def calculations(time, distance):
    count = 0
    # time is the range, calculate and add to counter for each winning option
    for index in range(1, time):
        total_distance = index * (time - index)
        if total_distance > distance:
            count += 1
    return count

# run the functions
def run(content):
    answer = 0
    races = parse_data(content)
    for time,distance in races.items():
        answer = calculations(int(time),int(distance))
    print(answer)
run(content)

file.close()