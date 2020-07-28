# -*- coding: utf-8 -*-
"""
Created on Tue May 12 01:46:08 2020

@author: Rajdeep Deb
"""

import numpy as np
import matplotlib.pyplot as plt
#Define parameters
while True:
    t_max= int(input('Enter the number of days: '))#maximum time in days
    dt=0.1 #time step in days
    t=np.linspace(0,t_max,int(t_max/dt)+1) #create time datapoint
    N=35498714 #total population of assam
    init_vals=1-1/N, 1/N, 0, 0
    alpha=0.2
    gamma=0.5
    beta=1.75
    params= alpha,beta,gamma
    def soc_dist(init_vals, params, t, rho):
        S_0, E_0, I_0, R_0= init_vals
        S,E,I,R=[S_0],[E_0],[I_0],[R_0]
        alpha, beta, gamma=params
        dt=t[1]-t[0]
        for k in t[1:]:
            next_S=S[-1]-(rho*beta*S[-1]*I[-1])*dt
            next_E=E[-1]+(rho*beta*S[-1]*I[-1]-alpha*E[-1])*dt
            next_I=I[-1]+(alpha*E[-1]-gamma*I[-1])*dt
            next_R=R[-1]+(gamma*I[-1])*dt
            S.append(next_S)
            E.append(next_E)
            I.append(next_I)
            R.append(next_R)
        return S, E, I, R, t
    import pandas as pd
    df=pd.DataFrame()
    for rho in (1,0.8,0.6,0.4,0.2):
        print(rho)
        S,E,I,R,t= soc_dist(init_vals, params, t, rho)
        df['time'+str(rho)]=t
        df['Susceptible_rho_'+str(rho)]=S
        df['Exposed_rho_'+str(rho)]=E
        df['Infected_rho_'+str(rho)]=I
        df['Recovered_rho_'+str(rho)]=R
    print(df.head())
    df.plot('time1',y=['Exposed_rho_1','Exposed_rho_0.8','Exposed_rho_0.6','Exposed_rho_0.4','Exposed_rho_0.2'],
            color=['darkblue','mediumblue','darkgreen','limegreen','lime'])
    plt.show()
    df.plot('time1',y=['Infected_rho_1','Infected_rho_0.8','Infected_rho_0.6','Infected_rho_0.4','Infected_rho_0.2'],
            color=['darkblue','mediumblue','darkgreen','limegreen','lime'])
    plt.show()