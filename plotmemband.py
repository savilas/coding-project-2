"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

peakbandwith = 900
bytestransf = 8 

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

code1_bandwith = [(problemsize * bytestransf) / (peakbandwith * time * (10**9)) * 100
    for problemsize, time in zip(problem_sizes, code1_time)]
code2_bandwith = [(problemsize * bytestransf) / (peakbandwith * time * (10**9)) * 100
    for problemsize, time in zip(problem_sizes, code2_time)]
code3_bandwith = [(problemsize * bytestransf) / (peakbandwith * time * (10**9)) * 100
    for problemsize, time in zip(problem_sizes, code3_time)]

plt.title("Comparison of 3 Codes: Memory Bandwidth Used")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#

plt.plot(code1_bandwith, "r-o", label=var_names[1])
plt.plot(code2_bandwith, "b-x", label=var_names[2])
plt.plot(code3_bandwith, "g-^", label=var_names[3])

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("Memory Bandwidth Utilized")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
    