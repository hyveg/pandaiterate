import pandas as pd

data = pd.read_csv("observationer.csv", sep=",", names=["Artnamn","Antal observationer"])


birds_list = []
observations_list = []
for index, row in data.iterrows():
    bird_name = row["Artnamn"]
    birds_list.append(bird_name)

for index, row in data.iterrows():
    observations = row["Antal observationer"]
    observations_list.append(observations)

bird_set = set()

for x in birds_list:
    bird_set.add(x)

pilfink_num = 0
for x in range(len(birds_list)):
    if birds_list[x] == "pilfink":
        pilfink_num += observations_list[x]

bergfink_num = 0
for x in range(len(birds_list)):
    if birds_list[x] == "bergfink":
        bergfink_num += observations_list[x]

species_list = []
species_list.append(bergfink_num,"bergfink")
species_list.append(pilfink_num)

species_list.sort()
print(species_list)



