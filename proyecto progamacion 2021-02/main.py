from CoC import coc
from dados import juego
import time
from colorama import init, Fore, Back, Style
import globales 
from pirinolamk2 import pirinola 


def Bienvenida(nombre) -> str:
  logo = """
_________                  .__                     _________  __                              __   
\_   ___ \ _____     ______|__|  ____    ____     /   _____/_/  |_  _______   ____    ____  _/  |_ 
/    \  \/ \__  \   /  ___/|  | /    \  /  _ \    \_____  \ \   __\.\_  __ \_/ __ \ _/ __ \ \   __\.
\     \____ / __ \_ \___ \ |  ||   |  \(  <_> )   /        \ |  |    |  | \/\  ___/ \  ___/  |  |  
 \______  /(____  //____  >|__||___|  / \____/   /_______  / |__|    |__|    \___  > \___  > |__|  
        \/      \/      \/          \/                   \/                      \/      \/        
____________________________________________________________________________________________________
    """
  print(Fore.YELLOW+Style.BRIGHT+logo)
  
  globales.nombre = str(input(Fore.LIGHTWHITE_EX+Style.BRIGHT+"""
  
▒█▀▀█ █░░█ █▀▀█ █░░ 　 █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ 　 █▀▀▄ █▀▀█ █▀▄▀█ █▀▀▄ █▀▀█ █▀▀ ▀█ 
▒█░░░ █░░█ █▄▄█ █░░ 　 █▀▀ ▀▀█ 　 ░░█░░ █░░█ 　 █░░█ █░░█ █░▀░█ █▀▀▄ █▄▄▀ █▀▀ █▀ 
▒█▄▄█ ░▀▀▀ ▀░░▀ ▀▀▀ 　 ▀▀▀ ▀▀▀ 　 ░░▀░░ ░▀▀▀ 　 ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀▀▀░ ▀░▀▀ ▀▀▀ ▄░ \n\n\n """))

  Sn = int(input('\n¿Quieres entrar? \n\n1. si, por qué no?\n \n2. no, mejor no. \n\n'))

  if Sn > 2:

    while Sn > 2:
      print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'alto ahí campeón.\n')
      time.sleep(2)
      print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'lee bien, dice 1 y 2 solo escoge una de esas dos.\n')
      print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'no es difícil, o si?\n')
      time.sleep(2)
      Sn = int(input(Fore.LIGHTWHITE_EX+Style.BRIGHT+'Quieres entrar? \n1. si, por que no? \n2. no, mejor no. \n'))
        
    
  return f'\nBienvenido {globales.nombre}.\n'

def main(nombre:str,fichas:int) -> str:

    print(Bienvenida(globales.nombre))

    print(Fore.RED+Style.BRIGHT+'Hola! soy un jugador recurrente de aqui.\n')
    time.sleep(3)
    print(Fore.RED+Style.BRIGHT+'Te vi y no pude resistirme a acercarme a ti.\n')
    time.sleep(3)
    print(Fore.RED+Style.BRIGHT+'Eres nuevo, verdad?\n')
    time.sleep(3)
    print(Fore.RED+Style.BRIGHT+'Bah, no tiene importancia desde ahora sere tu guia y rival en este street casino.\n')
    time.sleep(3)
    print(Fore.RED+Style.BRIGHT+'No hay tiempo que perder, traes fichas?\n')
    time.sleep(3)
    print(Fore.RED+Style.BRIGHT+'Que estupida esa pregunta, ten.\n')
    time.sleep(3)
    print(Fore.RED+Style.BRIGHT+'estas fichas son la moneda de este casino, ahora mismo tienes 100. \nUsalas bien, no pienso darte mas.\n')
    time.sleep(3)
    print(Fore.RED+Style.BRIGHT+'Vamos de una!\n')
    time.sleep(3)

    globales.fichas += 100
    
    juegos = Fore.RED+Style.BRIGHT+"""
Hay estos juegos.

1. street craps (apuesta maxima 30 fichas, minima 10 fichas).

2. pirinola.

3. Cara o Cruz (Apuesta minima 20 fichas).

4. salir.

    """
    print(juegos)
    time.sleep(3)
    des = int(input(Fore.LIGHTWHITE_EX+Style.BRIGHT+'¿Que jugarás?\n\n'))

    while des < 4:
      if des == 1:
        if globales.fichas >= 10:
          print(juego(globales.nombre,globales.fichas))
        else:
          print(Fore.RED+Style.BRIGHT+'Uy, no puedes jugar a este juego.')
      elif des == 2:
        print(pirinola(globales.nombre,globales.fichas))
      elif des == 3:
        if globales.fichas >= 20:
          print(coc(globales.nombre,globales.fichas))
        else:
          print(Fore.Red+Style.BRIGHT+'faltan fichas...')
      time.sleep(2)
      menj = int(input(Fore.LIGHTWHITE_EX+Style.BRIGHT+'Deseas ver otra ves los juegos que hay? \n1. si \n2. no \n'))
      if menj == 1:
          print(juegos)
      des = int(input(Fore.RED+Style.BRIGHT+'Quieres jugar otro juego? '))
      time.sleep(2)
    return Fore.RED+Style.BRIGHT+f'Bueno, nuestra travesia termina aqui {globales.nombre}. \nTe llevas {globales.fichas} fichas.'


print(main(globales.nombre,globales.fichas))