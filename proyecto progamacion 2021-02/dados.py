import globales
import time
from random import randint
from colorama import Fore,Style

def rolls():
   dado = (randint(1,6)) + (randint(1,6))
   return dado

def juego_maquina(fichas:int,point:int,nombre:str) -> int:
  print(Fore.RED+Style.BRIGHT+'\nBien, es mi turno')
  rue = True
  d1 = randint(10,30)
  print(Fore.RED+Style.BRIGHT+f'\napostare {d1} fichas')

  if globales.fichas >= d1:
    apuesta = d1
    print(Fore.GREEN+Style.BRIGHT+f'\napuestas tambien {apuesta} fichas')
    globales.fichas -= apuesta

    while rue == True:
                
      primer_mov = randint(1,2)

      if primer_mov == 1:
      
        dado = rolls()

        print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nlanzan los dados...')
        time.sleep(2)
        print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'... Y sale {dado}\n')
              
        if dado == 7 or dado == 11:
          time.sleep(2)
          print(Fore.MAGENTA+Style.BRIGHT+f'\nJAJAJAJA, gane. \npierdes {apuesta} fichas...')
          time.sleep(3)
          print('\n' * 50 )
          rue = False
          
        elif dado == 2 or dado == 3 or dado == 12:
          time.sleep(2)
          globales.fichas += apuesta * 2
          print(Fore.CYAN+Style.BRIGHT+f'\nAgh ganaste, ten. \nGanas {apuesta*2} fichas')
          time.sleep(3)
          print('\n' * 50 )
          rue = False    

        elif dado >= 4 and dado <= 10:
                
          print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nel "point" ahora es {dado}\n')
          point = dado 
                    
          m = True

          while m == True:

            dado = rolls()

            mov = int(input(Fore.GREEN+Style.BRIGHT+f'\nAntes de que lance, aumentas la apuesta? \n1. si \n2. no \n'))

            if mov == 1:
                    
              apues = int(input(Fore.GREEN+Style.BRIGHT+f'\nCuantas fichas vas a apostar {globales.nombre}? \n'))
              time.sleep(2)
              print(Fore.RED+Style.BRIGHT+f'vale, aumentare la apuesta tambien. \n{apues} fichas\n')
              globales.fichas -= apues
              apuesta += apues
                          
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nlanza los dados...')
              time.sleep(2)
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'...sale {dado}\n')
                    
              if dado == point:
                time.sleep(2)
                print(Fore.MAGENTA+Style.BRIGHT+f'\nmejor suerte para la proxima... \nPierdes {apuesta} fichas.\n')
                time.sleep(3)
                print('\n' * 50 )
                rue = False
                m = False

              elif dado == 7:
                time.sleep(2)
                globales.fichas += apuesta * 2
                print(Fore.CYAN+Style.BRIGHT+f'\nmala suerte la mia, ten tus ganacias... \nObtienes {apuesta * 2} fichas.\n')
                time.sleep(3)
                print('\n' * 50 )
                rue = False
                m = False
              else:
                            
                m = True
                          
            elif mov == 2:
                    
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nlanzan los dados')
              time.sleep(2)
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'...salio un {dado}\n')
                    
              if dado == point:
                time.sleep(2)
                print(Fore.MAGENTA+Style.BRIGHT+f'\nOops, perdiste... \nPerdiste {apuesta} fichas.\n')
                time.sleep(3)
                print('\n' * 50 )
                rue = False
                m = False

              elif dado == 7:
                time.sleep(2)
                globales.fichas += apuesta * 2
                print(Fore.MAGENTA+Style.BRIGHT+f'\nVaya... \nGanas {apuesta * 2} fichas\n')
                time.sleep(3)
                print('\n' * 50 )
                rue = False
                m = False
                          
              else:
                m = True
            
            else:
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\nhey!, ingresa solo 1 o 2')
              time.sleep(1)
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\nTan dificil es? \n')      
              m = True  

      elif primer_mov == 2:
            globales.fichas += apuesta
            apuest = randint(10,30)
            if apuest < globales.fichas:
              apuesta = apuest
              globales.fichas -= apuesta
              print(Fore.RED+Style.BRIGHT+f'\ncambio la apuesta a {apuesta}\n')
              time.sleep(2)
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\ntu apuesta ahora es de {apuesta} y te quedan {globales.fichas} fichas.\n')
              rue = True
            else:
              return Fore.RED+Style.BRIGHT+f'\nel que sigue...'

    else: 
      print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\ntienes {globales.fichas} fichas en total.\n') 
      return globales.fichas
  
  else:
    print(Fore.RED+Style.BRIGHT+f'\nlo siento {globales.nombre} esta ronda no podras jugarla\n')
    return globales.fichas

def juego_usuario(fichas:int,point:int,nombre:str) -> int:
  print(Fore.GREEN+Style.BRIGHT+f'\nes tu turno {globales.nombre}')
  time.sleep(3)
  rue = True
  apuesta = int(input(Fore.GREEN+Style.BRIGHT+'\nCuantas fichas vas a apostar? \n(Apuesta minima 10 fichas, maxima 30 fichas) '))

  while apuesta < 10 or apuesta >30:
    print(Fore.RED+Style.BRIGHT+'\nPor gente como tu es que el shampoo lleva instrucciones.\n ')
    time.sleep(2)
    apuesta = int(input(Fore.GREEN+Style.BRIGHT+'\nCuantas fichas vas a apostar? \n(Apuesta minima 10 fichas, maxima 30 fichas) '))

  if globales.fichas >= apuesta:

      print(Fore.RED+Style.BRIGHT+f'\nJAJAJA, tambien dare {apuesta} fichas.')
      globales.fichas -= apuesta
            
      while rue == True:
                  
        primer_mov = int(input(Fore.GREEN+Style.BRIGHT+'\nLanzas o cambias la puesta? \n1. Lanzo. \n2. Cambio la apuesta. \n'))

        if primer_mov == 1:

            dado = rolls()

            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nlanzan los dados...')
            time.sleep(2)
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'... Y sale {dado}\n')
                  
            if dado == 7 or dado == 11:
              globales.fichas += apuesta * 2
              time.sleep(2)
              print(Fore.CYAN+Style.BRIGHT+f'\nGanaste: {apuesta * 2}')
              time.sleep(1.5)
              print('\n' * 50 )
              rue = False

            elif dado == 2 or dado == 3 or dado == 12:
                time.sleep(2)
                print(Fore.MAGENTA+Style.BRIGHT+'\nlo siento, perdiste')
                time.sleep(1.5)
                print('\n' * 50 )
                rue = False

            elif dado >= 4 and dado <= 10:
              time.sleep(2)
              print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nel "point" ahora es {dado}')
              point = dado 
                      
              m = True

              while m == True:

                dado = rolls()
                time.sleep(2)
                mov = int(input(Fore.GREEN+Style.BRIGHT+f'\nAntes de que lances {globales.nombre}, aumentas la apuesta? \n1. si \n2. no \n'))

                if mov == 1:
                  time.sleep(2)  
                  apues = int(input(Fore.GREEN+Style.BRIGHT+'\nCuantas fichas mas apostaras? '))
                  time.sleep(2)    
                  apuestaf = apues + apuesta

                  globales.fichas -= apues

                  print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nlanzan los dados...')
                  time.sleep(2)
                  print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'... Y sale {dado}\n')
                      
                  if dado == point:
                    globales.fichas += apuestaf * 2
                    time.sleep(2)
                    print(Fore.CYAN+Style.BRIGHT+f'\nfelicidades ganaste: {apuestaf + apuestaf}.')
                    time.sleep(3)
                    print('\n' * 50 )
                    rue = False
                    m = False

                  elif dado == 7:
                    time.sleep(2)
                    print(Fore.MAGENTA+Style.BRIGHT+f'\nlo siento, perdiste.')
                    time.sleep(3)
                    print('\n' * 50 )
                    rue = False
                    m = False

                  else:
                              
                    m = True
                            
                elif mov == 2:
                  time.sleep(2)
                  print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nlanzan los dados...')
                  time.sleep(2)
                  print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'... Y sale {dado}.\n')
                      
                  if dado == point:
                    globales.fichas += apuesta * 2
                    time.sleep(2)
                    print(Fore.CYAN+Style.BRIGHT+f'\nfelicidades ganaste {apuesta * 2}.')
                    time.sleep(3)
                    print('\n' * 50 )
                    rue = False
                    m = False

                  elif dado == 7:
                    time.sleep(2)
                    print(Fore.MAGENTA+Style.BRIGHT+f'\nlo siento, perdiste.')
                    time.sleep(3)
                    print('\n' * 50 )
                    rue = False
                    m = False

                  else:
                    m = True
                else:
                    print(Fore.RED+Style.BRIGHT+'\nalto ahí,solo hay dos opciones y pones otra?')      
                    time.sleep(2)
                    print(Fore.RED+Style.BRIGHT+'\nseriedad por favor.')
                    m = True

        elif primer_mov == 2:
              globales.fichas += apuesta
              apuest = int(input(Fore.GREEN+Style.BRIGHT+'Cuantas fichas vas a apostar entonces? \n(Recuerda que son minimo 10 y maximo 30) '))
              while apuest < 10 or apuest >30:
                print(Fore.RED+Style.BRIGHT+f'Por que no haces caso {globales.nombre}?')
                time.sleep(2)
                apuest = int(input(Fore.GREEN+Style.BRIGHT+'Cuantas fichas vas a apostar entonces? \n(Recuerda que son minimo 10 y maximo 30) '))
              
              if apuest < fichas:
                apuesta = apuest
                globales.fichas -= apuesta
                print(Fore.GREEN+Style.BRIGHT+'bien, yo tambien cambio la apuesta')
                time.sleep(2)
                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'tu apuesta ahora es de {apuesta} y te quedan {fichas} fichas.')
                rue = True

              else:
                print(Fore.RED+Style.BRIGHT+f'fuera de mi vista, maldito pobre.')
                time.sleep(2)
                return globales.fichas

      print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'Tienes {globales.fichas} fichas.')
      return globales.fichas      
  else:
    print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'lo siento, no puedes jugar con tus fichas acutales.')
    return globales.fichas

def juego(nombre:str,fichas:int):
  menu = """
  
 ██████╗██████╗  █████╗ ██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║     ██████╔╝███████║██████╔╝███████╗
██║     ██╔══██╗██╔══██║██╔═══╝ ╚════██║
╚██████╗██║  ██║██║  ██║██║     ███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝
                                        

"""
  instrucciones = """
   
  _           _                       _                       
 (_)         | |                     (_)                      
  _ _ __  ___| |_ _ __ _   _  ___ ___ _  ___  _ __   ___  ___ 
 | | '_ \/ __| __| '__| | | |/ __/ __| |/ _ \| '_ \ / _ \/ __|
 | | | | \__ \ |_| |  | |_| | (_| (__| | (_) | | | |  __/\__ \.
 |_|_| |_|___/\__|_|   \__,_|\___\___|_|\___/|_| |_|\___||___/
______________________________________________________________________________________________________  
Para este juego necesitamos dos dados, un "shooter" y dinero.
El "shooter" es quien se designa para lanzar los dados, se cambia de "shooter" si el  actual pierde .
Para hacer apuestas debes hacerlo antes de que el "shooter" lance por primera vez, tambien en el transcurso de la ronda.
Bien, ahora hablemos de las apuestas y el juego.
El primer tiro "la salida" define si ganas o pierdes, si te sale un 7 o 11 ganas automaticamente si eres el "shooter" , pero si sale un 2,3 o 12.
pierdes automaticamente. Pasa lo contrario si la otra persona es el "shooter" si esta saca 7 o 11 tu pierdes, si saca 2,3 y 12 tu ganas
si el numero que sale esta entre 4 y 10, se conoce como "point". Si eres "shooter" siempre tu apuesta sera a este "point" y la otra persona apostara por el 7
si sale el 7 pierdes, si sale el point ganas. asi mismo que con "la salida" si la otra persona es el "shooter" tu apuesta es al 7, si sale ganas, sino sale y 
sale el "point" pierdes. en caso de que no salga este "point" se debe seguir hasta que salga.
las apuestas son siempre iguales, si la otra persona apuesta 20 fichas tu debes poner tambien 20 fichas.

Es hora de que empieces a jugar.
   """
  print(Fore.YELLOW+Style.BRIGHT+menu)
  time.sleep(2)
  print(Fore.LIGHTWHITE_EX+Style.BRIGHT+instrucciones)
  time.sleep(4)
  desi = int(input(Fore.GREEN+Style.BRIGHT+f'todo listo,{nombre}? \n1. Si, estoy listo. \n2.No, adios.\n'))
  point = 0
  Counter = 1
  while desi > 2 or desi < 1: 
      print(Fore.RED+Style.BRIGHT+'Alto ahí, solo 1 o 2 \nningun otro numero, entiendes? ')
      desi = int(input(Fore.GREEN+Style.BRIGHT+f'todo listo,{nombre}? \n1. Si, estoy listo. \n2.No, adios.\n'))

  while desi != 2:
     if desi == 1:
        if Counter % 2 != 0:
           juego_usuario(globales.fichas,point,globales.nombre)
           time.sleep(2)
           print('\n' * 50 )
        elif Counter % 2 == 0:
           juego_maquina(globales.fichas,point,globales.nombre)
           time.sleep(2)
           print('\n' * 50 )
     desi = int(input(Fore.GREEN+Style.BRIGHT+'otra ronda? \n1. si\n 2. no \n'))
     Counter += 1
  else:
     return Fore.LIGHTWHITE_EX+Style.BRIGHT+f'Bueno, te vas con {globales.fichas} fichas'



