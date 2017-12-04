def initial():
    puzzle_input = open("Day4.txt").readlines()
    return puzzle_input

def main():
    puzzle = initial()
    correct = 0
    for i in puzzle:
        words = i.rstrip().split(" ")
        if len(words) == len(set(words)):
            correct += 1
    print(correct)
    #part2
    correct2 = 0
    for i in puzzle:
        words = list(map(sorted,i.rstrip().split(" ")))
        unique = [list(i) for i in set(tuple(i) for i in words)]
        if len(words) == len(unique):
            correct2 += 1
    print(correct2)
    return

main()
