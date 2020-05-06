import pandas as pd
import csv 

#Import the results of the various methods
df1 = pd.read_csv("method1.csv")
df2 = pd.read_csv("method2.csv")
df3 = pd.read_csv("method3.csv")
df4 = pd.read_csv("method4.csv")

#Initailize data structures to hold results
dfs = [df1,df2,df3,df4]
freqs = [{},{},{},{}]
nodes = set()

#For each dataframe, extract the list of clusters in the solution, and convert them from strings and tabulate their frequencies for that method
for i, frame in enumerate(dfs):
    for node_string in frame['6']:
        node_list = node_string.strip('][').split(', ') 
        for node in node_list:
            nodes.add(node)
            current = freqs[i].setdefault(node, 0)
            freqs[i][node] = current + 1

print("Nodes", len(nodes))

#Even if a node isn't included in one dataset, set the frequency to 0 for easy comparison
for i, frame in enumerate(dfs):
    for node in nodes:
        if node not in freqs[i]:
            freqs[i][node] = 0

#Write 4 different CSV's (one for each method)
for i, frame in enumerate(dfs):
    j = i+1
    file1 = open("freq%i.csv" %j, "w")
    writer = csv.writer(file1)
    for key, value in freqs[i].items():
        writer.writerow([key, value])
    file1.close()
