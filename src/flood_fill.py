import ast

def flood_fill(input_file_name, output_file_name):
    with open(input_file_name, "r") as file:
        height, width = map(int, file.readline().strip().split(","))
        start_row, start_col = map(int, file.readline().strip().split(","))
        replacement_color = file.readline().strip()
        matrix = [ast.literal_eval(file.readline().strip()) for _ in range(height)]

    rows = len(matrix)
    cols = len(matrix[0])

    if not (0 <= start_row < rows and 0 <= start_col < cols):
        raise ValueError("Початкова точка знаходиться поза межами матриці")

    target = matrix[start_row][start_col]
    

    def fill(row, col):
        if 0 <= row < rows and 0 <= col < cols and matrix[row][col] == target:  
            matrix[row][col] = replacement_color
            fill(row+1, col)
            fill(row-1, col)
            fill(row, col+1)
            fill(row, col-1)

    fill(start_row, start_col)

    with open(output_file_name, "w") as file:
        for row in matrix:
            file.write(str(row) + "\n")





