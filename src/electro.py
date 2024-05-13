import math

def find_total_wire_length(distance_between_poles, heights):
    total_length = 0
    
    for i in range(len(heights) - 1):
        if heights[i] >= heights[i + 1]:
            length = math.sqrt((heights[i] - 1) ** 2 + distance_between_poles ** 2)
            heights[i + 1] = 1
        else:
            length = math.sqrt((heights[i + 1] - 1) ** 2 + distance_between_poles ** 2)
            heights[i] = 1
        
        total_length += length

    return total_length 

def read_txt(file_path):
    with open(file_path, 'r') as file:
        distance_between_poles = int(file.readline())
        heights = [int(x) for x in file.readline().split()]
        return distance_between_poles, heights

def write_txt(file_path, result):
    with open(file_path, 'w') as file:
        file.write(f"{result:.2f}")  



