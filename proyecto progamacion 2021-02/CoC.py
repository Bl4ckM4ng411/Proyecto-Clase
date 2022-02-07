import time
from random import randint
from colorama import init, Fore, Back, Style
import globales

def lanzamiento() -> int:
	numero = randint(1,2)

	if numero == 1:
		return numero
	elif  numero == 2:
		return numero

def suspenso(n:int) -> str:
	print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'\nSe lanza la moneda y...\n\n')
	time.sleep(3)
	if n == 1:
		return Fore.LIGHTWHITE_EX+Style.BRIGHT+'CAE CARA...\n'
	elif n == 2: 
		return Fore.LIGHTWHITE_EX+Style.BRIGHT+'CAE CRUZ...\n'

def apuesta_maquina(n:int,apuesta2:int) -> str:
  if n == 1:
    return Fore.RED+Style.BRIGHT+f'Breves, le voy a Cruz con {apuesta2}'

  elif n == 2:
    return Fore.RED+Style.BRIGHT+f'Bueno, entonces le voy a Cara con{apuesta2}'  

def coc(nombre:str,fichas:int) -> str:
	menu = """
    .,-:::::    :::.     :::::::..     :::.             ...           .,-:::::  :::::::..    ...    ::::::::::::    
  ,;;;'````'    ;;`;;    ;;;;``;;;;    ;;`;;         .;;;;;;;.      ,;;;'````'  ;;;;``;;;;   ;;     ;;;'`````;;;    
  [[[          ,[[ '[[,   [[[,/[[['   ,[[ '[[,      ,[[     \[[,    [[[          [[[,/[[['  [['     [[[    .n[['    
  $$$         c$$$cc$$$c  $$$$$$c    c$$$cc$$$c     $$$,     $$$    $$$          $$$$$$c    $$      $$$  ,$$P"      
  `88bo,__,o,  888   888, 888b "88bo, 888   888,    "888,_ _,88P    `88bo,__,o,  888b "88bo,88    .d888,888bo,_   
   "YUMMMMMP" YMM   " "`  MMMM   "W"  YMM   ""`       "YMMMMMP"       "YUMMMMMP" MMMM   "W"  "YmmMMMM"" `""*UMM    
     """
	
	Instrucciones= """
  En este juego podrás ganar o perder con un solo movimiento, se bienvenido a CARA O CRUZ
	  """

	print(Fore.YELLOW+Style.BRIGHT+menu)
	time.sleep(4)
	print(Fore.LIGHTWHITE_EX+Style.BRIGHT+Instrucciones)
	time.sleep(3)

	des = int(input(Fore.LIGHTWHITE_EX+Style.BRIGHT+'Jugaras?\n\n(1) De una!! (2) Naaah\n\n'))

	while des < 2 and des > 0:
		
		respuesta= int(input(Fore.GREEN+Style.BRIGHT+f'''Y bien {globales.nombre} ¿que escoges?\n \n        


    ░░██╗░░███╗░░██╗░░░░░░█████╗░░█████╗░██████╗░░█████╗░
    ░██╔╝░████║░░╚██╗░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ██╔╝░██╔██║░░░╚██╗░░░██║░░╚═╝███████║██████╔╝███████║
    ╚██╗░╚═╝██║░░░██╔╝░░░██║░░██╗██╔══██║██╔══██╗██╔══██║
    ░╚██╗███████╗██╔╝░██╗╚█████╔╝██║░░██║██║░░██║██║░░██║
    ░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝. \n                                
    ░░██╗██████╗░██╗░░   ░█████╗░██████╗░██╗░░░██╗███████╗
    ░██╔╝╚════██╗╚██╗░   ██╔══██╗██╔══██╗██║░░░██║╚════██║
    ██╔╝░░░███╔═╝░╚██╗   ██║░░╚═╝██████╔╝██║░░░██║░░███╔═╝
    ╚██╗░██╔══╝░░░██╔╝   ██║░░██╗██╔══██╗██║░░░██║██╔══╝░░
    ░╚██╗███████╗██╔╝░██╗╚█████╔╝██║░░██║╚██████╔╝███████╗
    ░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝.\n\n
'''))
		
		while respuesta < 1 or respuesta > 2:
			time.sleep(2)
			print(Fore.RED+Style.BRIGHT+f'parce {globales.nombre}, 1 o 2 nada mas!')
			time.sleep(3)
			respuesta= int(input(Fore.GREEN+Style.BRIGHT+f'y bien {globales.nombre} que escoges? \n\n(1) Cara. \n\n(2) Cruz.\n\n'))
		
		apuesta= int(input(Fore.RED+Style.BRIGHT+'¿Cuanto le apuestas? \n(Apuesta miníma 20 fichas) \n\n'))
		
		while apuesta < 20:
			time.sleep(2)
			print(Fore.RED+Style.BRIGHT+f'Frena el carro {globales.nombre},apuestas por debajo de 20 no se aceptan.')
			time.sleep(3)
			apuesta= int(input(Fore.RED+Style.BRIGHT+'¿Cuanto le apuestas? \n(Apuesta miníma 20 fichas) \n\n'))
		
		while apuesta > fichas:
			time.sleep(2)
			print(Fore.RED+Style.BRIGHT+f'Que tal este?')
			time.sleep(3)
			apuesta= int(input(Fore.RED+Style.BRIGHT+'¿Cuanto apuestas? \n(Apuesta miníma 20 fichas) \n\n'))
		
		apuesta2 = randint(20,30)
		
		print(apuesta_maquina(respuesta,apuesta2))

		if globales.fichas >= 20:

			carocru = lanzamiento()

			print(suspenso(carocru))
			
			globales.fichas -= apuesta
			
			if respuesta == carocru:

				globales.fichas += apuesta + apuesta2
				time.sleep(3)
				print(Fore.CYAN+Style.BRIGHT+'\nUʏʏʏ ᴏ̨ᴜɪᴇᴛᴏ sᴏᴄɪᴏ!!! Gᴀɴᴀsᴛᴇ!!! sɪɢᴜᴇ ᴀsɪ ʏ ᴍᴜᴄʜᴀ sᴜᴇʀᴛᴇ!')
				time.sleep(3)
				print('\n' * 50 )
			
			elif respuesta != carocru:
				time.sleep(3)
				print(Fore.MAGENTA+Style.BRIGHT+f'Mala suerte {globales.nombre}, perdiste...Pero no te preocupes. \nPuedes volver a jugar y perder.')
				time.sleep(3)
				print('\n' * 50 )
		
		else:
			time.sleep(1.5)
			return Fore.RED+Style.BRIGHT+'Que asco, largo! \nTe faltan fichas juega otra vaina.'	
		
		time.sleep(2)
		
		des = int(input(Fore.RED+Style.BRIGHT+'Otra? \n(1) R. \n(2) No, me voy. \n'+Back.RESET))
	
	else:
		time.sleep(2)
		return Fore.LIGHTWHITE_EX+Style.BRIGHT+f'te vas con {globales.fichas} fichas, espero vuelvas y pierdas. '


