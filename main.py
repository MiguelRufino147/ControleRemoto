import keyboard
import time

#Inicio
class ControleRemoto:
    def __init__(self,cor,altura,peso):
        self.cor=cor
        self.altura=altura
        self.peso=peso

#Funções
    def passar_canal(self):
        canal=0
        while True:
                if keyboard.is_pressed('alt'):
                    canal=canal+1
                    time.sleep(0.5)
                    print(f'Você esta no canal {canal} aperte[tab] para mudar de função')
                elif keyboard.is_pressed('tab'):
                    break
                elif keyboard.is_pressed('Shift'):
                    canal=canal-1
                    time.sleep(0.5)
                    print(f'Você esta no canal {canal} aperte[tab] para mudar de função')
                elif keyboard.is_pressed('tab'):
                    
                    c=input('Qual controle deseja? [preto/cinza]').lower()
                    f=input('Deseja[MUDAR CANAL] ou [OI]').lower()
                        

    def print(self):
        while True:
            if keyboard.is_pressed('p'):
                time.sleep(0.5)
                print('oi')
                           
#lista controles
controle1=ControleRemoto("preto","30cm","100g")
controle2=ControleRemoto("cinza","30cm","100g")

#Execução  
while True:
    c=input('Qual controle deseja? [preto/cinza]').lower()
    f=input('Deseja[MUDAR CANAL] ou [OI]').lower()
    if c =="preto" and f =='mudar canal':
        print(f'Você escolheu o controle {controle1.cor} o qual possui {controle1.altura} de altura e {controle1.peso} de peso')
        print('aperte alt para aumentar um canal e shift para diminuir e tab para mudar a função')
        controle1.passar_canal()
        
    elif c=="cinza" and f=='mudar canal':
        print(f'Você escolheu o controle {controle2.cor} o qual possui {controle2.altura} de altura e {controle2.peso} de peso')
        print('aperte alt para aumentar um canal e shift para diminuir e tab para mudar a função')
        controle2.passar_canal()

        

    elif c=='preto' and f== 'oi':
        controle1.print()

    elif c=='cinza' and f== 'oi':
        controle2.print()



asfasfasf
  















