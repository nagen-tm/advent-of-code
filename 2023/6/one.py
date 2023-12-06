#part one: 

file = open('input.txt','r')
content = file.read()
# put race and distance in dictionary
def parse_data(data):
    races = {}
    times, distances = content.split('\n')
    time = times.split()
    distance = distances.split()
    for index in range(1,len(time)):
        races[time[index]] = distance[index]
    return races

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
    answer = 1
    races = parse_data(content)
    for time,distance in races.items():
        result = calculations(int(time),int(distance))
        answer = answer * result
    print(answer)
run(content)

file.close()