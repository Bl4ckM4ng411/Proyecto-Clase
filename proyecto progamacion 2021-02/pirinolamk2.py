  
import time
from colorama import Fore , Style
import random
import globales

def lanzamiento_jug(f1:int,f2:int,p1:int,nom1:str) -> str:  
        time.sleep(2)
        input(Fore.GREEN+Style.BRIGHT+"**PRESIONE ENTER PARA TIRAR**\n")
        dado =random.choice(["PON 1", "PON 2", "TOMA 1", "TOMA 2", "TOMA TODO", "TODOS PONEN"])
        time.sleep(2)
        print(Fore.WHITE+Style.BRIGHT+f"{nom1} te toca: {dado}")

        if dado == "PON 1":
            time.sleep(1)
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\nPones 1 ficha en el pozo\n')
            globales.fichas -= 1
            globales.p1 += 1
        elif dado == "PON 2":
            time.sleep(1)
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\nPones 2 fichas en el pozo\n')
            globales.fichas -=2
            globales.p1 +=2
        elif dado == "TOMA 1":
            time.sleep(1)
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\ntomas 1 ficha del pozo\n')
            globales.fichas +=1
            globales.p1 -= 1
        elif dado == "TOMA 2":
            time.sleep(1)
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\nCoges 2 fichas del pozo\n')
            globales.fichas += 2
            globales.p1 -= 2
        elif dado == "TOMA TODO":
            time.sleep(1)
            globales.fichas += globales.p1
            globales.p1 -= globales.p1
            return Fore.CYAN+Style.BRIGHT+f'\nFELICIDADES!!! TE LLEVAS TODO\nTus fichas: {globales.fichas}\n'
        elif dado == "TODOS PONEN":
            time.sleep(1)
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\nTe toca poner.\n')
            time.sleep(1)
            print(Fore.RED+Style.BRIGHT+'\nSe le tiene en cuenta...\n')
            f1 -= 1
            f2 -= 1
            globales.p1 += 2
            time.sleep(2)
        return(Fore.GREEN+Style.BRIGHT+f'\n{nom1},tienes {globales.fichas} fichas.\nEl pozo tiene {globales.p1}fichas\n')

def lanzamiento_maq(f1:int,f2:int,p1:int,nom1:str) ->str:
        print(Fore.RED+Style.BRIGHT+"\nES MI TURNO\n")
        time.sleep(2)
        input(Fore.GREEN+Style.BRIGHT+"**PRESIONE ENTER PARA QUE EMPIEZEN**\n")
        dado=random.choice(["PON 1", "PON 2", "TOMA 1", "TOMA 2", "TOMA TODO", "TODOS PONEN"])
        time.sleep(2)
        print(Fore.RED+Style.BRIGHT+f"Me ha tocado {dado}")

        if dado == "PON 1":
            time.sleep(1)
            print(Fore.RED+Style.BRIGHT+'\nPongo 1 ficha\n')
            f2 -= 1
            globales.p1 += 1
        elif dado == "PON 2":
            time.sleep(1)
            print(Fore.RED+Style.BRIGHT+'\nPongo 2 ficha\n')
            f2 -= 2
            globales.p1 += 2
        elif dado == "TOMA 1":
            time.sleep(1)
            print(Fore.RED+Style.BRIGHT+'\nTomo 1 ficha\n')
            f2+=1
            globales.p1-=1
        elif dado == "TOMA 2":
            time.sleep(1)
            print(Fore.RED+Style.BRIGHT+'\nTomo 2 fichas\n')
            f2 += 2
            globales.p1 -= 2
        elif dado == "TOMA TODO":
            time.sleep(1)
            f2 += globales.p1
            globales.p1 -= globales.p1
            return (Fore.RED+Style.BRIGHT+f'\nJAJAJA, le gane.\ntus fichas: {globales.fichas}\n')

        elif dado == "TODOS PONEN":
            time.sleep(1)
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\n{nom1}, Te toca poner.\n')
            time.sleep(1)
            print(Fore.RED+Style.BRIGHT+'\nAaagh, que mamera\n')
            f2 -= 1
            globales.fichas -= 1
            globales.p1 += 2
        
        time.sleep(2)
        return(Fore.GREEN+Style.BRIGHT+f'\n{nom1},tienes {globales.fichas} fichas.\nEl pozo tiene {globales.p1}fichas\n')


def pirinola(nombre:str,fichas:int) -> str:
    menu = """
       _____          _          _______  _____  _______     _____  ____  _____   ___   _____          _        
      |_   _|        / \        |_   __ \|_   _||_   __ \   |_   _||_   \|_   _|.'   `.|_   _|        / \       
        | |         / _ \         | |__) | | |    | |__) |    | |    |   \ | | /  .-.  \ | |         / _ \      
        | |   _    / ___ \        |  ___/  | |    |  __ /     | |    | |\ \| | | |   | | | |   _    / ___ \     
       _| |__/ | _/ /   \ \_     _| |_    _| |_  _| |  \ \_  _| |_  _| |_\   |_\  `-'  /_| |__/ | _/ /   \ \_   
      |________||____| |____|   |_____|  |_____||____| |___||_____||_____|\____|`.___.'|________||____| |____|  
                                                                                                                
    """
    print(Fore.YELLOW+Style.BRIGHT+menu)
    time.sleep(2)
    print(Fore.WHITE+Style.BRIGHT+"\n\nVaya, vaya... vemos que te gusta nuestro casino. Muy bien, pon tu nombre y jugarás contra uno de nosotros... Necesitas que te deseemos suerte? Jajajaj igual no ibamos a hacerlo... A jugar!!!\n\n")
    time.sleep(3)
    nom1= globales.nombre
    win = 0
    cont = 1
    print(Fore.WHITE+Style.BRIGHT+"\nPara comenzar cada jugador debe apostar 1 ficha\n")
    globales.fichas -= 1
    globales.f2 -= 1
    desi = 1
    globales.p1 += 2 
    time.sleep(2)
    input(Fore.WHITE+Style.BRIGHT+"**PARA INGRESAR TU MAGNIFICA APUESTA DEBES PRESIONAR ENTER**\n")
    print(Fore.GREEN+Style.BRIGHT+f"\n{nom1},tiene {globales.fichas} fichas;\nEl pozo es de {globales.p1} fichas\n\n")
    time.sleep(2)
  
    while win == 0:

       
        while desi <2 and globales.p1 > 0:
    
            if cont % 2 != 0:
                if globales.fichas > 0 and globales.f2 > 0 and globales.p1 > 0:
                    print(lanzamiento_jug(globales.fichas,globales.f2,globales.p1,nom1))
                    cont += 1
                else:
                    if globales.fichas <= 0:
                        time.sleep(2)
                        win=2
                        return Fore.MAGENTA+Style.BRIGHT+f'\nUyy!! {nom1}, Parece que tus fichas se acabaron...\n'
                    elif globales.f2 <= 0:
                        time.sleep(2)
                        win=1
                        return Fore.CYAN+Style.BRIGHT+f'\nAy no jodás me quede sin fichas.\nGanas esta vez {nom1}\n'   
                    elif globales.p1 <= 0:
                        win = 3
                        return Fore.RED+Style.BRIGHT+f'\nBueno,{nom1} creo que esto es un empate\n'
            else:
                if globales.fichas > 0 and globales.f2 > 0 and globales.p1 >0:    
                    print(lanzamiento_maq(globales.fichas,globales.f2,globales.p1,nom1))
                    cont += 1
                else:
                    if globales.fichas <= 0:
                        time.sleep(2)
                        win=2
                        return Fore.MAGENTA+Style.BRIGHT+f'\nUyy!! Parece que tus fichas se acabaron...\n'
                    elif globales.f2 <= 0:
                        time.sleep(2)
                        win=1
                        return Fore.CYAN+Style.BRIGHT+f'\nAy no jodás me quede sin fichas.\nGanas esta vez {nom1}\n'
                    elif globales.p1 <= 0:
                        win = 3
                        return Fore.RED+Style.BRIGHT+f'\n{nom1} empate.\n'
            
            time.sleep(2)
            desi = int(input(Fore.RED+Style.BRIGHT+'\notra ronda? \n1. si\n 2. no \n')) 
        else:
            if globales.fichas < globales.f2:
                win = 2
            elif globales.f2 < globales.fichas:
                win = 1
            elif globales.f2 == globales.fichas:
                win = 3
    else:
        
            if win==2:
                time.sleep(2)
                print(Fore.MAGENTA+Style.BRIGHT+"\nJAJAJAJJA AHÍ TIENE!!!!! YO FELIZ DE GANAR!!!!")
            elif win==1:
                time.sleep(2)   
                print(Fore.CYAN+Style.BRIGHT+f'\n {nom1}, AH BUENO!! NO TOMA NADA? FELICITACIONES POR GANAR!!')
            elif  win == 3:
                time.sleep(2)
                print(Fore.RED+Style.BRIGHT+"\nJUMMMMM JUSTO A ESO LE LLAMAMOS EMPATE")    
 
    
    return Fore.LIGHTWHITE_EX+Style.BRIGHT+f'\nBueno, te vas con {globales.fichas} fichas'
