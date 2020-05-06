import pandas as pd

df = pd.read_csv("tiff2pixel.csv")


def convert(x):
    '''Take in coordinates as a string (x,y) and return as a tuple'''
    x = x.split(',')
    x = (float(x[0][1:]), float(x[1][:len(x[1])-1]))
    return x

#Convert to tuple-ified dataframe columns
df['Pixel_val'] = df['Pixel_val'].apply(convert)
df['Coord_val'] = df['Coord_val'].apply(convert)

#Separate the tuples into multiple columns
df["pixel_x"] = [p[0] for p in df["Pixel_val"]]
df["pixel_y"] = [p[1] for p in df["Pixel_val"]]
df["coord_x"] = [c[0] for c in df["Coord_val"]]
df["coord_y"] = [c[1] for c in df["Coord_val"]]

df2 = pd.read_csv("Results.csv")

#Add the population density data to the same dataframe
df['value'] = [df2[str(int(row['pixel_x']))][int(row['pixel_y'])] for index, row in df.iterrows()]

#Write a new CSV for input into the model
df.to_csv("data.csv")