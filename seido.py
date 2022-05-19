import matplotlib.pyplot as plt
import numpy as np
#10/1 - 12/31 

#getting NOWPAHS data and forecast data at same time and calculating RMSE, MAE, and bias.
#plotting RMSE, MAE, and bia at different terms.

month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+67]
    B2 = A2[c:c+67]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:67]
    D2 = C2[0:67]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 23:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >22:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 23: 
        month = 13

#print(B1)
#print(D1)


rmse1_I_10 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_10 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____10DAYS____')

print('RMSE')
print(rmse1_I_10)
print(rmse2_I_10)

mae1_I_10 = np.mean(np.abs(H1 - H2))
mae2_I_10 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_10)
print(mae2_I_10)

bias1_I_10 = np.mean(H2 - H1)
bias2_I_10 = np.mean(T2 - T1)

print('bias')
print(bias1_I_10)
print(bias2_I_10)


fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(H1, H2)
ax.set_title('ISHK wave height [M]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,4)
ax.set_ylim(0,4)
fig.savefig("ISHIKARI_HEIGHT_s.png")

fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(T1, T2)
ax.set_title('ISHK period [s]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,10)
ax.set_ylim(0,10)
fig.savefig("ISHIKARI_period_s.png")



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+55]
    B2 = A2[c:c+55]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:55]
    D2 = C2[0:55]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 23:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >22:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 23: 
        month = 13


rmse1_I_7 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_7 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____7DAYS____')

print('RMSE')
print(rmse1_I_7)
print(rmse2_I_7)

mae1_I_7 = np.mean(np.abs(H1 - H2))
mae2_I_7 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_7)
print(mae2_I_7)

bias1_I_7 = np.mean(H2 - H1)
bias2_I_7 = np.mean(T2 - T1)

print('bias')
print(bias1_I_7)
print(bias2_I_7)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+39]
    B2 = A2[c:c+39]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:39]
    D2 = C2[0:39]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 25:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >24:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 25: 
        month = 13


rmse1_I_5= np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_5 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____5DAYS____')

print('RMSE')
print(rmse1_I_5)
print(rmse2_I_5)

mae1_I_5 = np.mean(np.abs(H1 - H2))
mae2_I_5 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_5)
print(mae2_I_5)

bias1_I_5 = np.mean(H2 - H1)
bias2_I_5 = np.mean(T2 - T1)

print('bias')
print(bias1_I_5)
print(bias2_I_5)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+31]
    B2 = A2[c:c+31]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:31]
    D2 = C2[0:31]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 25: 
        month = 13


rmse1_I_4 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_4 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____4DAYS____')

print('RMSE')
print(rmse1_I_4)
print(rmse2_I_4)

mae1_I_4 = np.mean(np.abs(H1 - H2))
mae2_I_4 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_4)
print(mae2_I_4)

bias1_I_4 = np.mean(H2 - H1)
bias2_I_4 = np.mean(T2 - T1)

print('bias')
print(bias1_I_4)
print(bias2_I_4)

month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+27]
    B2 = A2[c:c+27]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:27]
    D2 = C2[0:27]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 26: 
        month = 13


rmse1_I_35 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_35 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____3.5DAYS____')

print('RMSE')
print(rmse1_I_35)
print(rmse2_I_35)

mae1_I_35 = np.mean(np.abs(H1 - H2))
mae2_I_35 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_35)
print(mae2_I_35)

bias1_I_35 = np.mean(H2 - H1)
bias2_I_35 = np.mean(T2 - T1)

print('bias')
print(bias1_I_35)
print(bias2_I_35)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+24]
    B2 = A2[c:c+24]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:24]
    D2 = C2[0:24]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 26: 
        month = 13


rmse1_I_3 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_3 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____3DAYS____')

print('RMSE')
print(rmse1_I_3)
print(rmse2_I_3)

mae1_I_3 = np.mean(np.abs(H1 - H2))
mae2_I_3 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_3)
print(mae2_I_3)

bias1_I_3 = np.mean(H2 - H1)
bias2_I_3 = np.mean(T2 - T1)

print('bias')
print(bias1_I_3)
print(bias2_I_3)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+19]
    B2 = A2[c:c+19]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:19]
    D2 = C2[0:19]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 27:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >26:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 27: 
        month = 13

rmse1_I_25 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_25 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____2.5DAY____')

print('RMSE')
print(rmse1_I_25)
print(rmse2_I_25)

mae1_I_25 = np.mean(np.abs(H1 - H2))
mae2_I_25 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_25)
print(mae2_I_25)

bias1_I_25 = np.mean(H2 - H1)
bias2_I_25 = np.mean(T2 - T1)

print('bias')
print(bias1_I_25)
print(bias2_I_25)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+15]
    B2 = A2[c:c+15]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:15]
    D2 = C2[0:15]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_I_2 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_2 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____2DAYS____')

print('RMSE')
print(rmse1_I_2)
print(rmse2_I_2)

mae1_I_2 = np.mean(np.abs(H1 - H2))
mae2_I_2 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_2)
print(mae2_I_2)

bias1_I_2 = np.mean(H2 - H1)
bias2_I_2 = np.mean(T2 - T1)

print('bias')
print(bias1_I_2)
print(bias2_I_2)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+11]
    B2 = A2[c:c+11]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:11]
    D2 = C2[0:11]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 28:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >27:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 28: 
        month = 13

rmse1_I_15 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_15 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____1.5DAY____')

print('RMSE')
print(rmse1_I_15)
print(rmse2_I_15)

mae1_I_15 = np.mean(np.abs(H1 - H2))
mae2_I_15 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_15)
print(mae2_I_15)

bias1_I_15 = np.mean(H2 - H1)
bias2_I_15 = np.mean(T2 - T1)

print('bias')
print(bias1_I_15)
print(bias2_I_15)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+8]
    B2 = A2[c:c+8]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:8]
    D2 = C2[0:8]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_I_1 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_1 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____1DAY____')

print('RMSE')
print(rmse1_I_1)
print(rmse2_I_1)

mae1_I_1 = np.mean(np.abs(H1 - H2))
mae2_I_1 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_1)
print(mae2_I_1)

bias1_I_1 = np.mean(H2 - H1)
bias2_I_1 = np.mean(T2 - T1)

print('bias')
print(bias1_I_1)
print(bias2_I_1)

fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(H1, H2)
ax.set_title('KAS wave height (1day) [M]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,4)
ax.set_ylim(0,4)
fig.savefig("ISHIKARI_HEIGHT_s2.png")


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+3]
    B2 = A2[c:c+3]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:3]
    D2 = C2[0:3]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    #print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_I_05 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_I_05 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____0.5DAY____')

print('RMSE')
print(rmse1_I_05)
print(rmse2_I_05)

mae1_I_05 = np.mean(np.abs(H1 - H2))
mae2_I_05 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_I_05)
print(mae2_I_05)

bias1_I_05 = np.mean(H2 - H1)
bias2_I_05 = np.mean(T2 - T1)

print('bias')
print(bias1_I_05)
print(bias2_I_05)


























##RUMOI

month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+67]
    B2 = A2[c:c+67]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:67]
    D2 = C2[0:67]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 23:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >22:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 23: 
        month = 13

#print(B1)
#print(D1)


rmse1_10 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_10 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____10DAYS____')

print('RMSE')
print(rmse1_10)
print(rmse2_10)

mae1_10 = np.mean(np.abs(H1 - H2))
mae2_10 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_10)
print(mae2_10)

bias1_10 = np.mean(H2 - H1)
bias2_10 = np.mean(T2 - T1)

print('bias')
print(bias1_10)
print(bias2_10)


fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(H1, H2)
ax.set_title('KAS wave height [M]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,4)
ax.set_ylim(0,4)
fig.savefig("KASHIMA_HEIGHT_s.png")

fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(T1, T2)
ax.set_title('KAS period [s]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,10)
ax.set_ylim(0,10)
fig.savefig("KASHIMA_period_s.png")



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+55]
    B2 = A2[c:c+55]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:55]
    D2 = C2[0:55]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 23:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >22:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 23: 
        month = 13


rmse1_7 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_7 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____7DAYS____')

print('RMSE')
print(rmse1_7)
print(rmse2_7)

mae1_7 = np.mean(np.abs(H1 - H2))
mae2_7 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_7)
print(mae2_7)

bias1_7 = np.mean(H2 - H1)
bias2_7 = np.mean(T2 - T1)

print('bias')
print(bias1_7)
print(bias2_7)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+39]
    B2 = A2[c:c+39]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:39]
    D2 = C2[0:39]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 25:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >24:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 25: 
        month = 13


rmse1_5= np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_5 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____5DAYS____')

print('RMSE')
print(rmse1_5)
print(rmse2_5)

mae1_5 = np.mean(np.abs(H1 - H2))
mae2_5 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_5)
print(mae2_5)

bias1_5 = np.mean(H2 - H1)
bias2_5 = np.mean(T2 - T1)

print('bias')
print(bias1_5)
print(bias2_5)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+31]
    B2 = A2[c:c+31]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:31]
    D2 = C2[0:31]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 25: 
        month = 13


rmse1_4 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_4 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____4DAYS____')

print('RMSE')
print(rmse1_4)
print(rmse2_4)

mae1_4 = np.mean(np.abs(H1 - H2))
mae2_4 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_4)
print(mae2_4)

bias1_4 = np.mean(H2 - H1)
bias2_4 = np.mean(T2 - T1)

print('bias')
print(bias1_4)
print(bias2_4)

month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+27]
    B2 = A2[c:c+27]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:27]
    D2 = C2[0:27]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 26: 
        month = 13


rmse1_35 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_35 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____3.5DAYS____')

print('RMSE')
print(rmse1_35)
print(rmse2_35)

mae1_35 = np.mean(np.abs(H1 - H2))
mae2_35 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_35)
print(mae2_35)

bias1_35 = np.mean(H2 - H1)
bias2_35 = np.mean(T2 - T1)

print('bias')
print(bias1_35)
print(bias2_35)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+24]
    B2 = A2[c:c+24]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:24]
    D2 = C2[0:24]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 26: 
        month = 13


rmse1_3 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_3 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____3DAYS____')

print('RMSE')
print(rmse1_3)
print(rmse2_3)

mae1_3 = np.mean(np.abs(H1 - H2))
mae2_3 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_3)
print(mae2_3)

bias1_3 = np.mean(H2 - H1)
bias2_3 = np.mean(T2 - T1)

print('bias')
print(bias1_3)
print(bias2_3)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+19]
    B2 = A2[c:c+19]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:19]
    D2 = C2[0:19]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 27:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >26:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 27: 
        month = 13

rmse1_25 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_25 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____2.5DAY____')

print('RMSE')
print(rmse1_25)
print(rmse2_25)

mae1_25 = np.mean(np.abs(H1 - H2))
mae2_25 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_25)
print(mae2_25)

bias1_25 = np.mean(H2 - H1)
bias2_25 = np.mean(T2 - T1)

print('bias')
print(bias1_25)
print(bias2_25)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+15]
    B2 = A2[c:c+15]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:15]
    D2 = C2[0:15]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_2 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_2 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____2DAYS____')

print('RMSE')
print(rmse1_2)
print(rmse2_2)

mae1_2 = np.mean(np.abs(H1 - H2))
mae2_2 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_2)
print(mae2_2)

bias1_2 = np.mean(H2 - H1)
bias2_2 = np.mean(T2 - T1)

print('bias')
print(bias1_2)
print(bias2_2)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+11]
    B2 = A2[c:c+11]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:11]
    D2 = C2[0:11]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 28:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >27:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 28: 
        month = 13

rmse1_15 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_15 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____1.5DAY____')

print('RMSE')
print(rmse1_15)
print(rmse2_15)

mae1_15 = np.mean(np.abs(H1 - H2))
mae2_15 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_15)
print(mae2_15)

bias1_15 = np.mean(H2 - H1)
bias2_15 = np.mean(T2 - T1)

print('bias')
print(bias1_15)
print(bias2_15)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+8]
    B2 = A2[c:c+8]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:8]
    D2 = C2[0:8]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_1 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_1 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____1DAY____')

print('RMSE')
print(rmse1_1)
print(rmse2_1)

mae1_1 = np.mean(np.abs(H1 - H2))
mae2_1 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_1)
print(mae2_1)

bias1_1 = np.mean(H2 - H1)
bias2_1 = np.mean(T2 - T1)

print('bias')
print(bias1_1)
print(bias2_1)

fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(H1, H2)
ax.set_title('KAS wave height (1day) [M]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,4)
ax.set_ylim(0,4)
fig.savefig("KASHIMA_HEIGHT_s2.png")


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_RUM{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+3]
    B2 = A2[c:c+3]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:3]
    D2 = C2[0:3]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    #print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_05 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_05 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____0.5DAY____')

print('RMSE')
print(rmse1_05)
print(rmse2_05)

mae1_05 = np.mean(np.abs(H1 - H2))
mae2_05 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_05)
print(mae2_05)

bias1_05 = np.mean(H2 - H1)
bias2_05 = np.mean(T2 - T1)

print('bias')
print(bias1_05)
print(bias2_05)
































#KASHIMA

month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+67]
    B2 = A2[c:c+67]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:67]
    D2 = C2[0:67]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 23:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >22:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 23: 
        month = 13

#print(B1)
#print(D1)


rmse1_K_10 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_10 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____10DAYS____')

print('RMSE')
print(rmse1_K_10)
print(rmse2_K_10)

mae1_K_10 = np.mean(np.abs(H1 - H2))
mae2_K_10 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_10)
print(mae2_K_10)

bias1_K_10 = np.mean(H2 - H1)
bias2_K_10 = np.mean(T2 - T1)

print('bias')
print(bias1_K_10)
print(bias2_K_10)


fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(H1, H2)
ax.set_title('KAS wave height [M]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,4)
ax.set_ylim(0,4)
fig.savefig("KASHIMA_HEIGHT_s.png")

fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(T1, T2)
ax.set_title('KAS period [s]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,10)
ax.set_ylim(0,10)
fig.savefig("KASHIMA_period_s.png")



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+55]
    B2 = A2[c:c+55]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:55]
    D2 = C2[0:55]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 23:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >22:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 23: 
        month = 13


rmse1_K_7 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_7 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____7DAYS____')

print('RMSE')
print(rmse1_K_7)
print(rmse2_K_7)

mae1_K_7 = np.mean(np.abs(H1 - H2))
mae2_K_7 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_7)
print(mae2_K_7)

bias1_K_7 = np.mean(H2 - H1)
bias2_K_7 = np.mean(T2 - T1)

print('bias')
print(bias1_K_7)
print(bias2_K_7)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+39]
    B2 = A2[c:c+39]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:39]
    D2 = C2[0:39]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 25:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >24:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 25: 
        month = 13


rmse1_K_5= np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_5 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____5DAYS____')

print('RMSE')
print(rmse1_K_5)
print(rmse2_K_5)

mae1_K_5 = np.mean(np.abs(H1 - H2))
mae2_K_5 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_5)
print(mae2_K_5)

bias1_K_5 = np.mean(H2 - H1)
bias2_K_5 = np.mean(T2 - T1)

print('bias')
print(bias1_K_5)
print(bias2_K_5)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+31]
    B2 = A2[c:c+31]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:31]
    D2 = C2[0:31]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 25: 
        month = 13


rmse1_K_4 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_4 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____4DAYS____')

print('RMSE')
print(rmse1_K_4)
print(rmse2_K_4)

mae1_K_4 = np.mean(np.abs(H1 - H2))
mae2_K_4 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_4)
print(mae2_K_4)

bias1_K_4 = np.mean(H2 - H1)
bias2_K_4 = np.mean(T2 - T1)

print('bias')
print(bias1_K_4)
print(bias2_K_4)

month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+27]
    B2 = A2[c:c+27]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:27]
    D2 = C2[0:27]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 26: 
        month = 13


rmse1_K_35 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_35 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____3.5DAYS____')

print('RMSE')
print(rmse1_K_35)
print(rmse2_K_35)

mae1_K_35 = np.mean(np.abs(H1 - H2))
mae2_K_35 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_35)
print(mae2_K_35)

bias1_K_35 = np.mean(H2 - H1)
bias2_K_35 = np.mean(T2 - T1)

print('bias')
print(bias1_K_35)
print(bias2_K_35)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+24]
    B2 = A2[c:c+24]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:24]
    D2 = C2[0:24]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 26:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >25:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 26: 
        month = 13


rmse1_K_3 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_3 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____3DAYS____')

print('RMSE')
print(rmse1_K_3)
print(rmse2_K_3)

mae1_K_3 = np.mean(np.abs(H1 - H2))
mae2_K_3 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_3)
print(mae2_K_3)

bias1_K_3 = np.mean(H2 - H1)
bias2_K_3 = np.mean(T2 - T1)

print('bias')
print(bias1_K_3)
print(bias2_K_3)



month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+19]
    B2 = A2[c:c+19]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:19]
    D2 = C2[0:19]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 27:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >26:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 27: 
        month = 13

rmse1_K_25 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_25 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____2.5DAY____')

print('RMSE')
print(rmse1_K_25)
print(rmse2_K_25)

mae1_K_25 = np.mean(np.abs(H1 - H2))
mae2_K_25 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_25)
print(mae2_K_25)

bias1_K_25 = np.mean(H2 - H1)
bias2_K_25 = np.mean(T2 - T1)

print('bias')
print(bias1_K_25)
print(bias2_K_25)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+15]
    B2 = A2[c:c+15]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:15]
    D2 = C2[0:15]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_K_2 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_2 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____2DAYS____')

print('RMSE')
print(rmse1_K_2)
print(rmse2_K_2)

mae1_K_2 = np.mean(np.abs(H1 - H2))
mae2_K_2 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_2)
print(mae2_K_2)

bias1_K_2 = np.mean(H2 - H1)
bias2_K_2 = np.mean(T2 - T1)

print('bias')
print(bias1_K_2)
print(bias2_K_2)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+11]
    B2 = A2[c:c+11]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:11]
    D2 = C2[0:11]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 28:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >27:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 28: 
        month = 13

rmse1_K_15 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_15 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____1.5DAY____')

print('RMSE')
print(rmse1_K_15)
print(rmse2_K_15)

mae1_K_15 = np.mean(np.abs(H1 - H2))
mae2_K_15 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_15)
print(mae2_K_15)

bias1_K_15 = np.mean(H2 - H1)
bias2_K_15 = np.mean(T2 - T1)

print('bias')
print(bias1_K_15)
print(bias2_K_15)


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+8]
    B2 = A2[c:c+8]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:8]
    D2 = C2[0:8]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
   # print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_K_1 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_1 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____1DAY____')

print('RMSE')
print(rmse1_K_1)
print(rmse2_K_1)

mae1_K_1 = np.mean(np.abs(H1 - H2))
mae2_K_1 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_1)
print(mae2_K_1)

bias1_K_1 = np.mean(H2 - H1)
bias2_K_1 = np.mean(T2 - T1)

print('bias')
print(bias1_K_1)
print(bias2_K_1)

fig, ax = plt.subplots(1, 1)
ax.plot([0,10], [0,10],color="black",linestyle="dashed",alpha=0.3)
ax.scatter(H1, H2)
ax.set_title('KAS wave height (1day) [M]')
ax.set_xlabel("Real")
ax.set_ylabel("Forecast")
ax.set_xlim(0,4)
ax.set_ylim(0,4)
fig.savefig("KASHIMA_HEIGHT_s2.png")


month = 10
day = 1
c = 1
H1 = np.empty(0)
H2 = np.empty(0)
T1 = np.empty(0)
T2 = np.empty(0)
while month < 13:
    day2 = str(day)
    if day < 10:
        day2 = str(0)+str(day)
    fname1 = 'Z_KAS{0}.txt'.format(month)
    ZIKYOU = np.loadtxt(fname1)
    fname2 = 'Y2{0}{1}.txt'.format(month,day2)
    YOHOU = np.loadtxt(fname2, skiprows=1)
    A1 = ZIKYOU[:,0]
    A2 = ZIKYOU[:,1]
    B1 = A1[c:c+3]
    B2 = A2[c:c+3]
    C1 = YOHOU[:,0]
    C2 = YOHOU[:,1]
    D1 = C1[0:3]
    D2 = C2[0:3]
    H1 = np.append(H1,B1)
    H2 = np.append(H2,D1)
    T1 = np.append(T1,B2)
    T2 = np.append(T2,D2)
    #print(month,"/",day)
    #print(B1)
    #print(D1)
    #print(month,day,len(H1),len(H2))

    day += 1
    c += 8
    if day > 29:
        month += 1
        day = 1
        c = 1
    if month ==11 and day >28:
        month += 1
        day = 1
        c = 1
    if month == 12 and day == 29: 
        month = 13


rmse1_K_05 = np.sqrt(np.mean((H1 - H2) ** 2))
rmse2_K_05 = np.sqrt(np.mean((T1 - T2) ** 2))

print('____0.5DAY____')

print('RMSE')
print(rmse1_K_05)
print(rmse2_K_05)

mae1_K_05 = np.mean(np.abs(H1 - H2))
mae2_K_05 = np.mean(np.abs(T1 - T2))

print('MAE')
print(mae1_K_05)
print(mae2_K_05)

bias1_K_05 = np.mean(H2 - H1)
bias2_K_05 = np.mean(T2 - T1)

print('bias')
print(bias1_K_05)
print(bias2_K_05)





fig, ax = plt.subplots(1, 1)
ax.set_title('RMSE 10/1 - 12/22')
ax.set_xlabel('Days')
ax.set_ylabel('Height [m]')
XX = [0.5,1,1.5,2,2.5,3,3.5,4,5,7,8.5]
ax.set_xlim(0.5,8.5)
YY1 = [rmse1_I_05,rmse1_I_1,rmse1_I_15,rmse1_I_2,rmse1_I_25,rmse1_I_3,rmse1_I_35,rmse1_I_4,rmse1_I_5,rmse1_I_7,rmse1_I_10]
YY2 = [rmse1_05,rmse1_1,rmse1_15,rmse1_2,rmse1_25,rmse1_3,rmse1_35,rmse1_4,rmse1_5,rmse1_7,rmse1_10]
YY3 = [rmse1_K_05,rmse1_K_1,rmse1_K_15,rmse1_K_2,rmse1_K_25,rmse1_K_3,rmse1_K_35,rmse1_K_4,rmse1_K_5,rmse1_K_7,rmse1_K_10]
ax.plot(XX,YY1,c='red',label='ISHK')
ax.plot(XX,YY2,c='blue',label='RUM')
ax.plot(XX,YY3,c='green',label='KAS')
ax.plot([0,10], [0,0],color="black",linestyle="dashed",alpha=0.3)
ax.legend(loc='best')
fig.savefig("RMSE_HEIGHT.png")

fig, ax = plt.subplots(1, 1)
ax.set_title('RMSE 10/1 - 12/22')
ax.set_xlabel('Days')
ax.set_ylabel('period [s]')
XX = [0.5,1,1.5,2,2.5,3,3.5,4,5,7,8.5]
ax.set_xlim(0.5,8.5)
YY1 = [rmse2_I_05,rmse2_I_1,rmse2_I_15,rmse2_I_2,rmse2_I_25,rmse2_I_3,rmse2_I_35,rmse2_I_4,rmse2_I_5,rmse2_I_7,rmse2_I_10]
YY2 = [rmse2_05,rmse2_1,rmse2_15,rmse2_2,rmse2_25,rmse2_3,rmse2_35,rmse2_4,rmse2_5,rmse2_7,rmse2_10]
YY3 = [rmse2_K_05,rmse2_K_1,rmse2_K_15,rmse2_K_2,rmse2_K_25,rmse2_K_3,rmse2_K_35,rmse2_K_4,rmse2_K_5,rmse2_K_7,rmse2_K_10]
ax.plot(XX,YY1,c='red',label='ISHK')
ax.plot(XX,YY2,c='blue',label='RUM')
ax.plot(XX,YY3,c='green',label='KAS')
ax.plot([0,10], [0,0],color="black",linestyle="dashed",alpha=0.3)
ax.legend(loc='best')
fig.savefig("RMSE_period.png")

fig, ax = plt.subplots(1, 1)
ax.set_title('mae 10/1 - 12/22')
ax.set_xlabel('Days')
ax.set_ylabel('Height [m]')
XX = [0.5,1,1.5,2,2.5,3,3.5,4,5,7,8.5]
ax.set_xlim(0.5,8.5)
YY1 = [mae1_I_05,mae1_I_1,mae1_I_15,mae1_I_2,mae1_I_25,mae1_I_3,mae1_I_35,mae1_I_4,mae1_I_5,mae1_I_7,mae1_I_10]
YY2 = [mae1_05,mae1_1,mae1_15,mae1_2,mae1_25,mae1_3,mae1_35,mae1_4,mae1_5,mae1_7,mae1_10]
YY3 = [mae1_K_05,mae1_K_1,mae1_K_15,mae1_K_2,mae1_K_25,mae1_K_3,mae1_K_35,mae1_K_4,mae1_K_5,mae1_K_7,mae1_K_10]
ax.plot(XX,YY1,c='red',label='ISHK')
ax.plot(XX,YY2,c='blue',label='RUM')
ax.plot(XX,YY3,c='green',label='KAS')
ax.plot([0,10], [0,0],color="black",linestyle="dashed",alpha=0.3)
ax.legend(loc='best')
fig.savefig("mae_HEIGHT.png")

fig, ax = plt.subplots(1, 1)
ax.set_title('mae 10/1 - 12/22')
ax.set_xlabel('Days')
ax.set_ylabel('period [s]')
XX = [0.5,1,1.5,2,2.5,3,3.5,4,5,7,8.5]
ax.set_xlim(0.5,8.5)
YY1 = [mae2_I_05,mae2_I_1,mae2_I_15,mae2_I_2,mae2_I_25,mae2_I_3,mae2_I_35,mae2_I_4,mae2_I_5,mae2_I_7,mae2_I_10]
YY2 = [mae2_05,mae2_1,mae2_15,mae2_2,mae2_25,mae2_3,mae2_35,mae2_4,mae2_5,mae2_7,mae2_10]
YY3 = [mae2_K_05,mae2_K_1,mae2_K_15,mae2_K_2,mae2_K_25,mae2_K_3,mae2_K_35,mae2_K_4,mae2_K_5,mae2_K_7,mae2_K_10]
ax.plot(XX,YY1,c='red',label='ISHK')
ax.plot(XX,YY2,c='blue',label='RUM')
ax.plot(XX,YY3,c='green',label='KAS')
ax.plot([0,10], [0,0],color="black",linestyle="dashed",alpha=0.3)
ax.legend(loc='best')
fig.savefig("mae_period.png")

fig, ax = plt.subplots(1, 1)
ax.set_title('bias 10/1 - 12/22')
ax.set_xlabel('Days')
ax.set_ylabel('Height [m]')
XX = [0.5,1,1.5,2,2.5,3,3.5,4,5,7,8.5]
ax.set_xlim(0.5,8.5)
YY1 = [bias1_I_05,bias1_I_1,bias1_I_15,bias1_I_2,bias1_I_25,bias1_I_3,bias1_I_35,bias1_I_4,bias1_I_5,bias1_I_7,bias1_I_10]
YY2 = [bias1_05,bias1_1,bias1_15,bias1_2,bias1_25,bias1_3,bias1_35,bias1_4,bias1_5,bias1_7,bias1_10]
YY3 = [bias1_K_05,bias1_K_1,bias1_K_15,bias1_K_2,bias1_K_25,bias1_K_3,bias1_K_35,bias1_K_4,bias1_K_5,bias1_K_7,bias1_K_10]
ax.plot(XX,YY1,c='red',label='ISHK')
ax.plot(XX,YY2,c='blue',label='RUM')
ax.plot(XX,YY3,c='green',label='KAS')
ax.plot([0,10], [0,0],color="black",linestyle="dashed",alpha=0.3)
ax.legend(loc='best')
fig.savefig("bias_HEIGHT.png")

fig, ax = plt.subplots(1, 1)
ax.set_title('bias 10/1 - 12/22')
ax.set_xlabel('Days')
ax.set_ylabel('period [s]')
XX = [0.5,1,1.5,2,2.5,3,3.5,4,5,7,8.5]
ax.set_xlim(0.5,8.5)
YY1 = [bias2_I_05,bias2_I_1,bias2_I_15,bias2_I_2,bias2_I_25,bias2_I_3,bias2_I_35,bias2_I_4,bias2_I_5,bias2_I_7,bias2_I_10]
YY2 = [bias2_05,bias2_1,bias2_15,bias2_2,bias2_25,bias2_3,bias2_35,bias2_4,bias2_5,bias2_7,bias2_10]
YY3 = [bias2_K_05,bias2_K_1,bias2_K_15,bias2_K_2,bias2_K_25,bias2_K_3,bias2_K_35,bias2_K_4,bias2_K_5,bias2_K_7,bias2_K_10]
ax.plot(XX,YY1,c='red',label='ISHK')
ax.plot(XX,YY2,c='blue',label='RUM')
ax.plot(XX,YY3,c='green',label='KAS')
ax.plot([0,10], [0,0],color="black",linestyle="dashed",alpha=0.3)
ax.legend(loc='best')
fig.savefig("bias_period.png")


