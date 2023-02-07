Encuesta <- read.csv("Encuesta.csv")

library(ggplot2)
library(tidyverse)
######################################################
##################LIMPIEZA############################
######################################################
names(Encuesta)[1] <- 'fecha'
names(Encuesta)[2] <- 'Nombre'
names(Encuesta)[5] <- 'Ubicacion'
names(Encuesta)[7] <- 'Ocupacion'
names(Encuesta)[8] <- 'Cuadro'
names(Encuesta)[9] <- 'Experiencia'
names(Encuesta)[10] <- 'Correo'

Encuesta$Ubicacion[Encuesta$Ubicacion== "Atizapán de Zaragoza"] <- 'Atizapan de Zaragoza'
Encuesta$Cuadro[Encuesta$Cuadro== "Sí"] <- 'Si'
Encuesta$Experiencia[Encuesta$Experiencia== "Sí"] <- 'Si'
Encuesta$Ocupacion[Encuesta$Ocupacion== "Ingeniería o Ciencias Aplicadas"] <- "Ingenieria o Ciencias Aplicadas"


######################################################
##################Cuadro de SI########################
######################################################
Cuadro_si <- Encuesta[Encuesta$Cuadro=="Si",3:7]

#Unicamente por EDAD
ggplot(data=Cuadro_si)+
  geom_boxplot(aes(x=Edad),alpha=0.5,fill='blue')+
  labs(x='Edad',y='',title = 'Box Plot de la EDAD de quienes aceptaron el cuadro')+
  theme_minimal()

summary(Cuadro_si$Edad)
table(Cuadro_si$Sexo)
#POR EDAD Y  SEXO
ggplot(data=Cuadro_si)+
  geom_boxplot(aes(x=Edad,fill=Sexo),alpha=0.5)+
  labs(x='Edad',y='',title = 'Box Plot de la EDAD de quienes aceptaron el cuadro Dividida en Sexo')+
  theme_minimal()

summary(Cuadro_si[Cuadro_si$Sexo=='Masculino',]$Edad) #Hombres
summary(Cuadro_si[Cuadro_si$Sexo=='Femenino',]$Edad)  #Mujeres


#########################################################
#############INTERVALO DE CONFIANZA######################
########PROMEDIO DE LA EDAD QUIENES ACEPTARON############
#################EL CUADRO###############################

library(fBasics)
valor <- shapiroTest(Cuadro_si$Edad)@test$p.value # Prueba de normalidad
ifelse(valor>0.1,'LA MUESTRA ES NORMAL','LA MUESTRA NO ES NORMAL')

library(BSDA)
#EN GENERAL
t.test(Cuadro_si$Edad,conf.level = 0.95)

#HOMBRES
t.test(Cuadro_si[Cuadro_si$Sexo=='Masculino',]$Edad,conf.level = 0.95)

#Mujeres
t.test(Cuadro_si[Cuadro_si$Sexo=='Femenino',]$Edad,conf.level = 0.95)


######################################################
##################Experiencia de SI###################
######################################################
exp_si <- Encuesta[Encuesta$Experiencia=="Si",3:7]

#Unicamente por EDAD
ggplot(data=exp_si)+
  geom_boxplot(aes(x=Edad),alpha=0.5,fill='blue')+
  labs(x='Edad',y='',title = 'Box Plot de la EDAD de quienes aceptaron la EXPERIENCIA')+
  theme_minimal()

summary(exp_si$Edad)

#POR EDAD Y  SEXO
ggplot(data=exp_si)+
  geom_boxplot(aes(x=Edad,fill=Sexo),alpha=0.5)+
  labs(x='Edad',y='',title = 'Box Plot de la EDAD de quienes aceptaron la EXPERIENCIA Dividida en Sexo')+
  theme_minimal()

summary(exp_si[exp_si$Sexo=='Masculino',]$Edad) #Hombres
summary(exp_si[exp_si$Sexo=='Femenino',]$Edad)  #Mujeres

#########################################################
#############INTERVALO DE CONFIANZA######################
########PROMEDIO DE LA EDAD QUIENES ACEPTARON############
#################LA EXPERIENCIA##########################

library(fBasics)
valor_2 <- shapiroTest(exp_si$Edad)@test$p.value # Prueba de normalidad
ifelse(valor_2>0.1,'LA MUESTRA ES NORMAL','LA MUESTRA NO ES NORMAL')

library(BSDA)
#EN GENERAL
t.test(exp_si$Edad,conf.level = 0.95)


#HOMBRES
t.test(exp_si[exp_si$Sexo=='Masculino',]$Edad,conf.level = 0.95)


#Mujeres
t.test(exp_si[exp_si$Sexo=='Femenino',]$Edad,conf.level = 0.95)

