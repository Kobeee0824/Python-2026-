number_grid = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9], 
  [0]
]
                
print(number_grid[2][1]) #[row][column]

print("----------------------------------")

number_grid = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9], 
  [0]
]
                
for row in number_grid:# row = sa bawat value sa number_grid, puntahan mo yon (nakastore na sa row yung value)
  for col in row: # col = sa bawat value sa row (nakastore yung mga values), puntahan mo yon 
    print(col) #then dito ipprint
    
  