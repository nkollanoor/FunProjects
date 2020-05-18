from IPython.display import clear_output
import os
import time
##### Grid Size ######
global m
m=int(input("Enter number of rows: "))
global n
n=int(input("Enter number of columns: "))

##### Start Direction and spot####
d=str(input("Enter direction: dl,dr,ul,ur"))
if d not in ['dl','dr','ul','ur']:
    print("Enter a valid direction")
    quit()
i=int(input("Enter starting row number: "))
j=int(input("Enter starting column number: "))
if i>=m or j>=n:
    print("Invalid entry for starting point, row cannot exceed %d and column cannot exceed %d" % (m-1,n-1))
    quit()
curr=[i,j]
##################################

###### Function to display grid ####

def disp(curr):
    clear_output(wait=True)
    os.system('cls' if os.name=='nt' else 'clear')
    grid=[["|_|" for i in range(n)] for i in range(m)]
    grid[curr[0]][curr[1]]="|0|"
    for i in grid:
        print("".join(i))
    time.sleep(0.1)
####################################
while(True):
    if d=="ul":
        if curr==[0,0]:
            disp(curr)
            d="dr"
        elif curr[0]-1>=0 and curr[1]-1<0:        
            curr=[curr[0]-1,curr[1]+1]
            d="ur"
            disp(curr)
        elif curr[0]-1<0 and curr[1]-1>=0:
            curr=[curr[0]+1,curr[1]-1]
            d="dl"
            disp(curr)
        else:
            curr=[curr[0]-1,curr[1]-1]
            disp(curr)
    elif d=="ur":
        if curr==[0,n-1]:
            disp(curr)
            d="dl"
        elif curr[0]-1<0 and curr[1]+1>0:        
            curr=[curr[0]+1,curr[1]+1]
            d="dr"
            disp(curr)
        elif curr[0]-1>=0 and curr[1]+1>=n:
            curr=[curr[0]-1,curr[1]-1]
            d="ul"
            disp(curr)
        else:
            curr=[curr[0]-1,curr[1]+1]
            disp(curr)
    elif d=="dl":
        if curr==[m-1,0]:
            disp(curr)
            d="ur"
        elif curr[0]+1>0 and curr[1]-1<0:        
            curr=[curr[0]+1,curr[1]+1]
            d="dr"
            disp(curr)
        elif curr[0]+1>=m and curr[1]-1>=0:
            curr=[curr[0]-1,curr[1]-1]
            d="ul"
            disp(curr)
        else:
            curr=[curr[0]+1,curr[1]-1]
            disp(curr)
    elif d=="dr":
        if curr==[m-1,n-1]:
            disp(curr)
            d="ul"
        elif curr[0]+1<m and curr[1]+1>=n:        
            curr=[curr[0]+1,curr[1]-1]
            d="dl"
            disp(curr)
        elif curr[0]+1>=m and curr[1]+1<n:
            curr=[curr[0]-1,curr[1]+1]
            d="ur"
            disp(curr)
        else:
            curr=[curr[0]+1,curr[1]+1]
            disp(curr)
    else:
        print("Unhandled condition")
        break
