import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

volCa  = open('RedCathode.txt','r')
volCa = volCa.read().splitlines()
volAn  = open('RedAnode.txt','r')
volAn = volAn.read().splitlines()

# names = [volCa, volAn]
# colors = ['red', 'blue']
# labels = ['Cathode(V)', 'Anode(V)']
# i = 0;
#
# fig, ax1 = plt.subplots()
# for na in names:
#     time = []
#     val = []
#     for w in na[1:]:
#         t, v = w.split('\t')
#         time.append(t)
#         val.append(v)
#
#     time = np.array(list(map(float,time)))
#     val = np.array(list(map(float,val)))
#     ax1.plot(time, val, color=colors[i], label=labels[i])
#     i = i+1
#
# ax1.set_xlabel('Voltage (V)')
# ax1.set_ylabel('Voltage (V)')
# ax1.legend(loc='upper right')
# ax1.grid()
current = open('DiffoP.txt', 'r')
current = current.read().splitlines()
timeC = []
valC = []
for w in current[1:]:
    t, v = w.split('\t')
    timeC.append(t)
    valC.append(v)

timeC = np.array(list(map(float,timeC)))
valC = np.array(list(map(float,valC)))*1000

plt.figure()
plt.plot(timeC, valC, color='green', label='Diode(I)')
plt.xlabel("Voltage(v)")
plt.ylabel("Current(mA)")
plt.legend(loc='upper right')
plt.grid()
plt.show()

# ax2 = ax1.twinx()
# ax2.plot(timeC, valC, color='green', label='Diode(I)')
# ax2.set_ylabel("Current (mA)")
# ax2.legend(loc='lower right')
# # ax2.grid()
# fig.tight_layout()
# plt.show()
#
# print(max(valC))