def max_experience(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:      
        L = int(file.readline())
        levels = []
        experience = []
       
        for _ in range(L):
            row = list(map(int, file.readline().strip().split()))
            levels.append(row)
            experience.append(row)          
        max_exp = [[0] * len(row) for row in levels]
      
        for i in range(len(levels) - 1, -1, -1):
            for j in range(len(levels[i])):
                
                if i + 1 < len(levels):
                    max_exp[i][j] = experience[i][j] + max(max_exp[i + 1][j], max_exp[i + 1][j + 1])
                else:                  
                    max_exp[i][j] = experience[i][j]

   
    with open(output_file_name, 'w') as out_file:
        out_file.write(str(max_exp[0][0]))





