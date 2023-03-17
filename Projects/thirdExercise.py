def bomberMan(n,grid):
    if n == 1:
        return grid
    if n % 2 == 0:
        for column in grid:
            newC = column.replace(".","0")
            ind = grid.index(column)
            grid[ind] = newC
        return grid

    n //= 2
    r = len(grid)
    c = len(grid[0])

    def createState(grid):
        newGrid = []
        setOfBomb = set()
        for i in range(r):
            row = []
            for j in range(c):
                if grid[i][j] ==".":
                    row.append("0")
                else:
                    row.append(".")     
                    setOfBomb.add((i,j)) 
            newGrid.append(row)
        for x,y in setOfBomb:
            for dx,dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x = x+dx
                new_y = y+dy
                if 0 <= new_x < r and 0 <= new_y < c:
                    if newGrid[new_x][new_y] == "0":
                        newGrid[new_x][new_y] == "."
        grid = newGrid
        return grid
        
    for s in range(1+(not n & 1)):
            grid = createState(grid)
    grid = ["".join(row) for row in grid]

    return grid 
    




# # count the seconds
# # if n = 7, 1 -> does nothing, 2 -> plants bombs, 3-> initial bombs blow up. 
# # 4 -> plants bombs, 5 -> bombs that he planted on 2nd second blow up. 6 -> plants bombs, 7-> bombs that he planted on 4th second blow up.
# # 8-> plants bombs, 9 - bombs blowup  and so on. 

# # gets indexes of initial bombs

# # lstOFindex = []
# # for i in grid:
# #     # print(type(i))
# #     index = i.find("0")
# #     lstOFindex.append(index)
# # print(lstOFindex)
# # print(grid)
# # otherInd= []
# # # blow up bombs , with indexes

# # for column in grid:
# #     indofspace = column.find("0")
# #     otherInd.append(indofspace)
# #     if "0" in column and indofspace in lstOFindex:
# #         newC = column.replace("0",".")
# #         ind = grid.index(column)
# #         grid[ind] = newC
# # print(otherInd)
# # print(grid)

# # test exercies flow blowing up algorithm


# # nd = grid[0][2].replace("0",".")


# grid = [".0.","000",".0."]
# print(grid)

# # for column in grid:
# #     cd = grid.index(column)
# #     for row in column:
# #         rd = column.index(row)
# #         if grid[cd][rd] == "0":
# #             s = grid[rd].replace("0",".")
# #             grid[cd] = s
# # print(grid)

# if grid[1][1] =="0":
#     s = grid[2].replace("0",".")
#     grid[2] = s
# print(grid)
# ## bomb = [c,r] other detonations should happen -> [c-1,r] [c+1,r] [c,r-1] [c,j+l]


