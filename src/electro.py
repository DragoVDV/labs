import math

def calculate_distance(gap_measure, height_difference):
    
    return (gap_measure ** 2 + height_difference ** 2) ** 0.5


def define_max_wire_length(gap, heights):
    max_top = 0
    max_bottom = 0
    index = 0
    while index < len(heights) - 1:
        height_diff = abs(heights[index] - heights[index + 1])
        top_bottom = max_top + calculate_distance(gap, heights[index] - 1)
        bottom_bottom = max_bottom + gap
        bottom_top = max_bottom + calculate_distance(gap, heights[index + 1] - 1)
        top_top = max_top + calculate_distance(gap, height_diff)
        max_top = max(bottom_top, top_top)
        max_bottom = max(bottom_bottom, top_bottom)
        index += 1
    return max(max_top, max_bottom)




def read_txt(file_path):
    with open(file_path, 'r') as file:
        distance_between_poles = int(file.readline())
        heights = [int(x) for x in file.readline().split()]
        return distance_between_poles, heights

def write_txt(file_path, result):
    with open(file_path, 'w') as file:
        file.write(f"{result:.2f}")  


