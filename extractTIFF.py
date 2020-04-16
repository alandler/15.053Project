import rasterio as rio
# import pandas as pd
import numpy as np

dataset = rio.open('hrsl_sle_v1/hrsl_sle_settlement.tif')
print("Width", dataset.width)
print("Height", dataset.height)
print("Bounds", dataset.bounds)
print("Origin transform", dataset.transform * (0, 0))
print("Bottom Right transform", dataset.transform * (dataset.width, dataset.height))
print("CRS", dataset.crs)
print("META", dataset.meta)


band1 = dataset.read(1)


results = np.zeros((dataset.height, 10))
for i, row in enumerate(band1):
    rowsplit = np.array_split(row, 10)
    for j, l in enumerate(rowsplit):
        results[i][j] = np.nanmean([x for x in l if x!= -32768])

finalresults = np.zeros((10,10))

bandgroups = results.array_split(10)

print(bandgroups)


print(row1split)