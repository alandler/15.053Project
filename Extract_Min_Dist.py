import pandas as pd
df = pd.read_csv("data.csv")
edf = pd.read_csv("electricity.csv")

#Initialize a list to hold results
arr = []
#Run through each cluster
for i in range(len(df)):
    if i%10 == 0:
        print(i)
    #Calculate the nearest electricity grid location. Add this minimum distance to the arr.
    arr.append(min([((df["coord_x"][i]-edf["x"][j])**2+(df["coord_y"][i]-edf["y"][j])**2)**(1/2) for j in range(len(edf))]))

#Set results arr to dataframe
df["Min_Dist"] = arr

#Print to CSV
df.to_csv("Data_With_Dist.csv")