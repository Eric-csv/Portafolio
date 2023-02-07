
#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#Calculo de la permeabilidad de un medio conductor
def permeabilidad():
    ji = 2.5e-3 
    mi = (4*np.pi*1e-7)*(1+ji)
    return mi 
# calculo de la frecuencia
def fangular():
    f = [0.01,0.04,0.06,0.08,0.10] #FRECUENCIA EN hz
    O = [] #FRECUENCIA ANGULAR
    for i in f:
      omega = 2*np.pi*i
      O.append(omega)
    return O,f
#Calculo de la distancia
def distancia():
  rocas = {'Rocas Intrusivas' : [[1500,10000],6000,9.9e10,50000000000],
           'Rocas Extrusivas' : [[5000,15000],7000,14.2e10,70000000000]}
  TL = []
  for clave in rocas:
     for d in np.arange(30000,340000,62000):
         V = d/rocas[clave][1]
         TL.append(V)
  rocas['Rocas Intrusivas'] = rocas['Rocas Intrusivas']+TL[0:5]
  rocas['Rocas Extrusivas'] = rocas['Rocas Extrusivas']+TL[5:10]
  return rocas
#Calculo de la intensidad
def intensidad():
 ctd = {"K_11": 2134.9e-32, "alpha" : -0.00397, "E": 6.3e16}
 O,f = fangular()
 mi = permeabilidad()
 rocas = distancia()
 I = [[],[],[],[],[]]
 for clave in rocas:
   for k in range(2):
     for n in range(5):
       for V in np.nditer(rocas[clave][n+4]):
         for j in range(5):
            for t in np.arange(0,V,0.1):
                L = V*rocas[clave][1]
                i = ((ctd['K_11']*mi*O[j]**(4)*ctd['E']**(5/2)*L**(1/2)*rocas[clave][2]**(2)*np.sin(t)**(2))/
                         ((L-(rocas[clave][1]*t))**(2)*rocas[clave][1]*t**(2)*rocas[clave][3]**(3/2)))*np.e**(ctd['alpha']*(L-(rocas[clave][1]*t))*
                          np.sqrt(f[j]/rocas[clave][0][k]))
                I[j].append(i)
                
 return I
#Distancia, tiempor y etiqueta
def dte():
  R = []
  T = []
  z_p = []
  Etiqueta = []
  profundidad = []
  rocas = distancia()
  for clave in rocas:
    for k in range(2):
     for n in range(5):
       for V in np.nditer(rocas[clave][n+4]):
           for t in np.arange(0,V,0.1):
                    L = V*rocas[clave][1]
                    z_pp = L-(rocas[clave][1]*t)
                    z_p.append(z_pp)
                    T.append(t)
                    R.append(rocas[clave][0][k])
                    Etiqueta.append(clave)
                    profundidad.append(L)
  return R,T,z_p,Etiqueta,profundidad
#Creación del Dataframe
def dataframe():
  R,T,z_p,Etiqueta,profundidad = dte()
  I = intensidad()
  df = pd.DataFrame([Etiqueta,R,profundidad,z_p,T,I[0],I[1],I[2],I[3],I[4]])
  df = df.transpose()
  df.columns=(['ROCA','RESISTIVIDAD','PROFUNDIDAD','DISTANCIA','TIEMPO','0.01HZ','0.04HZ',
               '0.06HZ','0.08HZ','0.10HZ'])
  df.dropna(axis=0,inplace=True)
  return df
#Creación de archivo Excel
def excel():
  df = dataframe()
  df.to_excel('C:/Users/Eric Ortiz Pardo/OneDrive/Documentos/Proyecto de Titulación/Programa_Tesis/INTENSIDAD.xlsx')
#Cambiamos el tipo de dato del dataframe
def clean():
  df = dataframe()
  for columna in df.columns:
    if columna == 'ROCA':
     df['ROCA'] = df['ROCA'].astype(str)
    else:
     df[columna] = df[columna].astype(float)
  return df
#Graficador del dataframe
def graficador():
 df = clean()
 for i in df['ROCA'].unique():
  for j in df[df['ROCA'] == i]['RESISTIVIDAD'].unique():
   for k in df['PROFUNDIDAD'].unique():
        df[(df['ROCA'] == i)&
         (df['RESISTIVIDAD'] == j)&
         (df['PROFUNDIDAD'] == k)&
         (df['TIEMPO'] <= 20.0)][df.columns.to_list()[4:]].plot(kind='line',x='TIEMPO')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Intensidad '+'('+r'$\frac{W^2}{m^10}$'+')')
        plt.title('Roca: '+ i + ' Resistividad: '+
                str(int(j))+r'$\Omega$'+'m'  +
                ' Profundidad: ' + 
                str(int(k))+'m',
                loc='center')
#Graficador masivo con correcciones de tiempos en casos especificos
def grafi_masivo():
 df = clean()
 for i in df['ROCA'].unique():
  for j in df[df['ROCA'] == i]['RESISTIVIDAD'].unique():
    for k in df['PROFUNDIDAD'].unique():
      if k == 30000:
         df[(df['ROCA'] == i)&
            (df['RESISTIVIDAD'] == j)&
            (df['PROFUNDIDAD'] == k)&
            (df['TIEMPO'] <= 3.9)][df.columns.to_list()[4:]].plot(kind='line',x='TIEMPO')
         plt.xlabel('Tiempo (s)')
         plt.ylabel('Intensidad '+'('+r'$\frac{W^2}{m^10}$'+')')
         plt.title(i + ' Resistividad: '+
                str(int(j))+r'$\Omega$'+'m'  +
                ' Profundidad: ' + 
                str(int(k))+'m',
                loc='center')
      elif k == 92000:
         df[(df['ROCA'] == i)&
            (df['RESISTIVIDAD'] == j)&
            (df['PROFUNDIDAD'] == k)&
            (df['TIEMPO'] <= 12.5)][df.columns.to_list()[4:]].plot(kind='line',x='TIEMPO')
         plt.xlabel('Tiempo (s)')
         plt.ylabel('Intensidad '+'('+r'$\frac{W^2}{m^10}$'+')')
         plt.title(i + ' Resistividad: '+
                str(int(j))+r'$\Omega$'+'m'  +
                ' Profundidad: ' + 
                str(int(k))+'m',
                loc='center')
      elif k == 278000:
         df[(df['ROCA'] == i)&
            (df['RESISTIVIDAD'] == j)&
            (df['PROFUNDIDAD'] == k)&
            (df['TIEMPO'] <= 35)][df.columns.to_list()[4:]].plot(kind='line',x='TIEMPO')
         plt.xlabel('Tiempo (s)')
         plt.ylabel('Intensidad '+'('+r'$\frac{W^2}{m^10}$'+')')
         plt.title(i + ' Resistividad: '+
                str(int(j))+r'$\Omega$'+'m'  +
                ' Profundidad: ' + 
                str(int(k))+'m',
                loc='center')
      else:
        df[(df['ROCA'] == i)&
           (df['RESISTIVIDAD'] == j)&
           (df['PROFUNDIDAD'] == k)&
           (df['TIEMPO'] <= 30.0)][df.columns.to_list()[4:]].plot(kind='line',x='TIEMPO')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Intensidad '+'('+r'$\frac{W^2}{m^10}$'+')')
        plt.title(i + ' Resistividad: '+
                str(int(j))+r'$\Omega$'+'m'  +
                ' Profundidad: ' + 
                str(int(k))+'m',
                loc='center')
# %%
grafi_masivo()

