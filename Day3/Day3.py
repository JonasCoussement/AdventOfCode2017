def grid():
    input_value = 325489
    current_value = 1
    input_coordinates = [0,0]
    current_jump = 1
    direction = 1
    while current_value < input_value:
        for i in range(0,2):
            for j in range(0,current_jump):
                current_value = current_value+1
                if direction == 1:
                    input_coordinates[0] = input_coordinates[0]+1
                elif direction == 2:
                    input_coordinates[1] = input_coordinates[1]+1
                elif direction == 3:
                    input_coordinates[0] = input_coordinates[0]-1
                elif direction == 4:
                    input_coordinates[1] = input_coordinates[1]-1
                if current_value == input_value:
                    print("Final coordinates are:",input_coordinates)
                    print("Total Manhattan distance:",sum(list(map(abs,input_coordinates))))
            direction = direction%4+1
        current_jump = current_jump+1
    #part 2
    current_value = 1
    input_coordinates = [0,0]
    current_jump = 1
    direction = 1
    grid_filled = [[1]]
    grid_visited = [[0,0]]
    while current_value < input_value:
        for i in range(0,2):
            for j in range(0,current_jump):
                if direction == 1:
                    input_coordinates[0] = input_coordinates[0]+1
                    current_value = find_neighbours(grid_visited,grid_filled,input_coordinates)
                    grid_visited.append(input_coordinates[:])
                    grid_filled.append([current_value])
                elif direction == 2:
                    input_coordinates[1] = input_coordinates[1]+1
                    current_value = find_neighbours(grid_visited,grid_filled,input_coordinates)
                    grid_visited.append(input_coordinates[:])
                    grid_filled.append([current_value])
                elif direction == 3:
                    input_coordinates[0] = input_coordinates[0]-1
                    current_value = find_neighbours(grid_visited,grid_filled,input_coordinates)
                    grid_visited.append(input_coordinates[:])
                    grid_filled.append([current_value])
                elif direction == 4:
                    input_coordinates[1] = input_coordinates[1]-1
                    current_value = find_neighbours(grid_visited,grid_filled,input_coordinates)
                    grid_visited.append(input_coordinates[:])
                    grid_filled.append([current_value])
                if current_value > input_value:
                    print("Final coordinates are:",input_coordinates)
                    print("First value larger than input:",current_value)
                    return 
            direction = direction%4+1
        current_jump = current_jump+1

def find_neighbours(cur_grid,cur_values,current_coordinates):
    neighbour_sum = 0
    for i in range(current_coordinates[0]-1,current_coordinates[0]+2):
        for j in range(current_coordinates[1]-1,current_coordinates[1]+2):
            if [i,j] in cur_grid:
                neighbour_sum = neighbour_sum + cur_values[cur_grid.index([i,j])][0]
    return neighbour_sum

      
grid()
