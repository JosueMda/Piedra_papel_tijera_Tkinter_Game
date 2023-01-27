
import random
import tkinter as tk 



scoreusuario= 0
scoremaquina= 0
usuario=" "

def comparacion(usuario):
  maquina = random.randint(1,3)
  ganador = ""
  if usuario == "PIEDRA" and maquina == 1:

    return "\n\n\nTU: PIEDRA\nMAQUINA: PIEDRA\n\nEMPATE"
    ganador = ""
    
    
  elif usuario == "PIEDRA" and maquina == 2:
    
    return "\n\n\nTU: PIEDRA\nMAQUINA: PAPEL\n\nHAS PERDIDO JAJA"
    ganador = "maquina"
  elif usuario == "PIEDRA" and maquina == 3:
    
    return "\n\n\nTU: PIEDRA\nMAQUINA: TIJERA\n\nHAS GANADO"
  
  elif usuario == "PAPEL" and maquina == 1:
     
     return "\n\n\nTU: PAPEL\nMAQUINA: PIEDRA\n\nHAS GANADO"
     ganador = "usuario"
    
  elif usuario == "PAPEL" and maquina == 2:
    
    return "\n\n\nTU: PAPEL\nMAQUINA: PAPEL\n\nEMPATE"
    ganador = ""
  elif usuario == "PAPEL" and maquina == 3:
    
    return"\n\n\nTU: PAPEL\nMAQUINA: TIJERA\n\nHAS PERDIDO JAJA"
    ganador = "maquina"
  elif usuario == "TIJERA" and maquina == 1:
    
    return"\n\n\nTU: TIJERA\nMAQUINA: PIEDRA\n\nHAS PERDIDO JAJA"
    ganador = "maquina"
    
  elif usuario == "TIJERA" and maquina == 2:
    
    return"\n\n\nTU: TIJERA\nMAQUINA: PAPEL\n\nHAS GANADO"
    ganador = "usuario"
  elif usuario == "TIJERA" and maquina == 3:
    
    return"\n\n\nTU: TIJERA\nMAQUINA: TIJERA\n\nEMPATE"
    ganador = " "
  
  else:
    
    return"\n***NO PUDE ENTENDERTE***"
    