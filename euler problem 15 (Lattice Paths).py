##Shortest-path diagrams here:  http://www.robertdickau.com/manhattan.html

import math

gridRows = 20

latticePaths = (math.factorial((2 * gridRows))) / (math.factorial(gridRows)*math.factorial(gridRows))
                
print(latticePaths)