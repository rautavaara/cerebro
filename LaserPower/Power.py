import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Laser power
# df=pd.read_csv('Test_10_27.csv')
# t = np.array(df['Optical Power Monitor 3.1.3778.562'].keys()[18:])
# pwr = np.array(df.values[18:])
# pwr = np.squeeze(pwr)
# pwr = pwr.astype(float)
# pwr = pwr*1000
# t = t.astype(float)

df=pd.read_csv('Protocol_1.csv')
tf = np.array(df['Optical Power Monitor 3.1.3778.562'].keys()[18:])
pwrf = np.array(df.values[18:])
pwrf = np.squeeze(pwrf)
pwrf = pwrf.astype(float)
pwrf = pwrf*1000
tf = tf.astype(float)

print(max(pwrf), min(pwrf))


t5 = tf[tf<10000]
pwi = np.logical_and(tf<10000, pwrf > 5)
pwf = np.logical_and(tf<170000, pwrf > 5)


# avpwr = np.average(pwr[pwr>2])
avpwi = np.average(pwrf[pwi])
avpwf = np.average(pwrf[pwf])
perc = avpwf/avpwi*100
print(avpwi, avpwf, 100-perc)

# fig = plt.figure()
# plt.plot(tf[pwi], pwrf[pwi], color='orange')
# plt.xlabel('T(ms)')
# plt.ylabel('P(mW)')
# plt.show()

