#%%
#Bibilotecas necessárias / Necessary libraries
import matplotlib.pyplot as plt
import statistics as st
import yfinance as yf
import numpy as np
import scipy.stats as sci
from scipy.stats import norm
import pandas as pd
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.titlecolor'] = 'w'
plt.rcParams['axes.labelsize'] = 14 
plt.rcParams['axes.labelcolor'] = 'w'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['xtick.color'] = 'w'
plt.rcParams['ytick.color'] = 'w'
plt.rcParams['grid.color'] = 'w'
plt.rcParams['grid.linestyle'] = ':'
plt.rcParams['grid.linewidth'] = 0.5 
plt.rcParams['axes.autolimit_mode'] = 'data'
plt.rcParams['axes.axisbelow'] = True

#Criando base de dados do ativo / Creating data base of stock
stock = 'PETR4.SA'
initial_date = '2005-01-01'
end_date = '2020-12-31'
name = 'PETROBRAS - PETR4'
period = '1d'

data_base = pd.DataFrame(yf.download(stock,start=initial_date,end=end_date,interval=period)['Adj Close'])
days = np.array(data_base.index)
prices = np.array(data_base['Adj Close'])
returns = ((prices[1:] - prices[:-1]) / prices[:-1])

#%%



plt.subplots(figsize=(12,6))

plt.subplot(221)
plt.plot(days,prices,color='royalblue')
plt.xticks(rotation=45)
plt.title(f'{name} {period}')
plt.ylabel('Value')
plt.grid(True)


plt.subplot(223)
plt.plot(days[1:],returns,color='royalblue')
plt.title(f'Retorno {period} do {name}')
plt.xticks(rotation=45)
plt.ylabel('Return')
plt.grid(True)

plt.subplot(222)
plt.hist(returns,bins=20,density=True,color='royalblue')
plt.xlabel('Calsse - Return')
plt.ylabel('Freguency')
plt.title(f'Histograma\nRetornos do {name}')
xmin, xmax = plt.xlim()
media = st.mean(returns)
desv_pad = st.pstdev(returns)
x_axis = np.linspace(xmin,xmax,100)
y_axix = norm.pdf(x_axis,media,desv_pad)
plt.plot(x_axis,y_axix,color='r')
plt.grid(True)

plt.subplot(224)
sci.probplot(returns,dist='norm',plot=plt)
plt.title(f'QQ-plot {name}')
plt.grid(True)
plt.suptitle(f'Análise do comportamento\n retornos da {name}\n'
             f'{initial_date} a {end_date}', fontsize=20, color='w')


plt.subplots_adjust(hspace=0.45)  # Ajusta o espaço vertical entre os subplots
plt.tight_layout()  # Ajusta automaticamente os subplots para evitar sobreposições
plt.savefig('Distribution analysis.png')
plt.show()



# %%
