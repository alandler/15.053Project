import rasterio as rio
# import pandas as pd
import numpy as np
import math

dataset = rio.open('hrsl_sle_v1/hrsl_sle_settlement.tif')
print("Width", dataset.width)
print("Height", dataset.height)
print("Bounds", dataset.bounds)
print("Origin transform", dataset.transform * (0, 0))
print("Bottom Right transform", dataset.transform * (dataset.width, dataset.height))
print("CRS", dataset.crs)
print("META", dataset.meta)


band1 = dataset.read(1)


results = np.zeros((dataset.height, 50))


for r in range(0,50):
    for c in range (0,50):
        s = 0
        count = 0
        for row in range(math.floor(r*(dataset.width/50)), math.floor((r+1)*(dataset.width/50))):
            for column in range(math.floor(c*(dataset.width/50)), math.floor((c+1)*(dataset.width/50))):
                if band1[row][column] != -32768:
                    s+=1
                count+=1
        results[r][c] = s/count
        print("result", r, ",",c, ":", s/count)

print(np.max(results))

#finalresults = np.zeros((10,10))

#bandgroups = results.array_split(10)

# print(bandgroups)


# print(row1split)