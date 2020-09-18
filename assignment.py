import numpy as np
import pandas as pd
from statistics import stdev
from statistics import mode
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_json("individuals.json")
data.drop(["id","household","wardIndex","wardNo","lat","lon","CommunityCentreDistance","employed","workplace","workplaceType","school"],axis=1, inplace=True)


mean = data["age"].mean()
variance = data["age"].var()
std = data["age"].std()
data.head(50)

plt.figure()
plt.hist(data["age"], bins=80, histtype="step", density="True", color="red")
#plt.plot(data["age"], y, color="red", marker="o")
plt.grid()
plt.show()