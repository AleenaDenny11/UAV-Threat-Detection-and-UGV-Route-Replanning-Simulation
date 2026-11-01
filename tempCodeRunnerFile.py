import numpy as np
import matplotlib.pyplot as plt
from detector import generate_threats
#grid size
GRID_SIZE=20
#create grid with all zeros means safe grid
grid=np.zeros((GRID_SIZE,GRID_SIZE))
#UGV start position, top left corner
start=(0,0)
#UGV end position, bottom right corner
end=(19,19)
#start & end
grid[start]=2
grid[end]=3
# Generate threats
threats = generate_threats(2)
#adding threats to the grid
for t in threats:
     x, y = t["location"]
     grid[x][y]=4
     
    
plt.imshow(grid)
plt.title("TACTI-SENSE")
plt.show()

