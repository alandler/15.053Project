import rasterio as rio
import pandas as pd
import numpy as np
import math

#Print various metadata for comphrension of the dataset and TIF format
dataset = rio.open('hrsl_sle_v1/hrsl_sle_settlement.tif')
print("Width", dataset.width)
print("Height", dataset.height)
print("Bounds", dataset.bounds)
print("Origin transform", dataset.transform * (0, 0))
print("Bottom Right transform", dataset.transform * (dataset.width, dataset.height))
print("CRS", dataset.crs)
print("META", dataset.meta)
band1 = dataset.read(1)

#Initailize empty array to hold the results of combination
results = np.zeros((dataset.height, 50))

#Run through 50 rows and columns to create 2500 clusters
for r in range(0,50):
    for c in range (0,50):
        s = 0
        count = 0
        #Run through each pixel in the cluster and add to the cluster
        for row in range(math.floor(r*(dataset.width/50)), math.floor((r+1)*(dataset.width/50))):
            for column in range(math.floor(c*(dataset.width/50)), math.floor((c+1)*(dataset.width/50))):
                #The empty value is -32768, which is actually 0
                if band1[row][column] != -32768:
                    s+=1
                count+=1
        #Add the average (density) to the results
        results[r][c] = s/count
        print("result", r, ",",c, ":", s/count)

print(np.max(results))

#Write the results to CSV
df = pd.DataFrame(results)
df.to_csv("Results.csv")