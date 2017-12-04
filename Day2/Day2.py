def initial_setup():
    puzzle_input = open("Day2.txt").readlines()
    return puzzle_input

def checksums(puzzle_input):
    check = 0;
    for i in puzzle_input:
        row = list(map(int,i.split("\t")))
        check = check + max(row)-min(row)
    return check

def checksums2(puzzle_input):
    check = 0;
    for i in puzzle_input:
        row = sorted(list(map(int,i.split("\t"))),reverse=True)
        for j in range(0,len(row)):
            for k in range(j+1,len(row)):
                if row[j]%row[k] == 0:
                    check = check + row[j]/row[k]
                    break
    return check
    
def main():
    print("Checksum for part 1: ",checksums(initial_setup()))
    print("Checksum for part 2: ",checksums2(initial_setup()))
    
main()

