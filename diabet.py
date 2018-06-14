import numpy as np
import matplotlib.pyplot as plt
import sys
from operator import itemgetter
diabet_file = []

with open("diabetes.data","r") as f:
    for i in f:
        diabet_file.append(i.strip("\n").split(";"))


diabet_list = []
counter = 0
for i in diabet_file:
    if i == diabet_file[-1]:
        break
    elif int(i[2]) >= 90:
        counter += 1
        diabet_list.append(counter)

pregnancy_age = [float(i[0])/float(i[7]) for i in diabet_file if int(i[2]) >= 90]
BodyMassIndex_age = [float(i[5])/float(i[7]) for i in diabet_file if int(i[2]) >= 90]
max_pregnancy_age_inst = int(diabet_list[diabet_list.index(pregnancy_age.index(max(pregnancy_age)))])
pregnancy_age = [i if i != 0.0 else 100 for i in pregnancy_age]
min_pregnancy_age_inst = int(diabet_list[diabet_list.index(pregnancy_age.index(min(pregnancy_age)))])
mass_age = [float(i[5])/float(i[7]) for i in diabet_file if int(i[2]) >= 90]
max_mass_inst = int(diabet_list[diabet_list.index(mass_age.index(max(mass_age)))])
mass_age = [i if i != 0.0 else 10000000000 for i in mass_age]
min_mass_inst = int(diabet_list[diabet_list.index(mass_age.index(min(mass_age)))])
age_list = [int(i[7]) for i in diabet_file if int(i[2]) >= 90]
fig,ax = plt.subplots()
ax.set_xticks([i for i in range(1,len(age_list),5)])
plt.plot(age_list,color="blue")
plt.ylabel("Ages")
plt.xlabel("Instances")
ax.annotate('max(#pregnancy/age)', xy=(max_pregnancy_age_inst,age_list[max_pregnancy_age_inst]), xytext=(18.5, 43),
            arrowprops=dict(facecolor='red', shrink=0.01),
            )
ax.annotate('min(#pregnancy/age)', xy=(min_pregnancy_age_inst,age_list[min_pregnancy_age_inst]), xytext=(30, 49),
            arrowprops=dict(facecolor='red', shrink=0.01),
            )
ax.annotate('max(#Body mass index /age)', xy=(max_mass_inst,age_list[max_mass_inst]),xytext=(54.5,25),
            arrowprops=dict(facecolor='green', shrink=5000000),
            )
ax.annotate('min(#Body mass index /age)', xy=(min_mass_inst,age_list[min_mass_inst]),xytext=(35,62.7),
            arrowprops=dict(facecolor='green', shrink=5000000),
            )
plt.savefig("Fig1.pdf")
plt.close()