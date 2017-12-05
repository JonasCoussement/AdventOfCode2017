def initial():
    puzzle_input = open("Day5.txt").readlines()
    return list(map(int,puzzle_input))

def main():
    instruct = initial()
    position = 0
    step = 0
    while position < len(instruct) or position < 0:
        new_position = position + instruct[position]
        instruct[position] += 1
        position = new_position
        step += 1
    print("part 1 takes",step,"steps")
    #part2
    instruct = initial()
    position = 0
    step = 0
    while position < len(instruct) or position < 0:
        new_position = position + instruct[position]
        if(instruct[position]>=3):
            instruct[position] += -1
        else:
            instruct[position] += 1
        position = new_position
        step += 1
    print("part 2 takes",step,"steps")
    return

main()
