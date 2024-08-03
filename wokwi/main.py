#Importa biblioteca
from machine import Pin, ADC, time_pulse_us, PWM, SoftI2C
import time
import utime
from i2c_lcd import I2cLcd


# configuracao
buttonOFF = Pin(26, Pin.IN, Pin.PULL_DOWN)
pot_1_backUP = 9999
pot_1_backUP_1 = 9999
pot_1_backUP_2 = 9999
pot_1_backUP_3 = 9999
pot_1_backUP_4 = 9999
pot_1_backUP_5 = 9999
pot_1_backUP_5 = 9999


# porta Potenciometro
pot1 = ADC(Pin(34)) #potenciometro
pot2 = ADC(Pin(35)) #potenciometro

# configurar ADC
pot1.atten(ADC.ATTN_11DB) 
pot1.width(ADC.WIDTH_10BIT)
pot2.atten(ADC.ATTN_11DB) 
pot2.width(ADC.WIDTH_10BIT)

#Função de mapeamento(conversão)
def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def desligar_aleds():
    led_amarelo_1.off()
    led_amarelo_2.off()
    led_verde_1.off()
    led_verde_2.off()
    led_vermelho_1.off()
    led_vermelho_2.off()




# configuracao led
led_vermelho_1 = Pin(15,Pin.OUT)
led_amarelo_1 = Pin(2,Pin.OUT)
led_verde_1 = Pin(4,Pin.OUT)

led_vermelho_2 = Pin(5,Pin.OUT)
led_amarelo_2 = Pin(18,Pin.OUT)
led_verde_2 = Pin(19,Pin.OUT)




# Parametros configuraçao do display
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
Icd = I2cLcd(i2c, 0x27, 2, 16)


def semaforo_normal_loop():

    led_vermelho_1.on()

    led_verde_2.on()
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    time.sleep(6)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////


    led_verde_2.off()

    led_amarelo_2.on()

    time.sleep(2)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////


    led_vermelho_1.off()

    led_amarelo_2.off()

    led_verde_1.on()

    led_vermelho_2.on()

    time.sleep(6)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_verde_1.off()

    led_amarelo_1.on()

    time.sleep(2)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_vermelho_2.off()

    led_amarelo_1.off()

def semaforo2_rapido_loop():


    led_vermelho_1.on()

    led_verde_2.on()
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    time.sleep(6)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_verde_2.off()

    led_amarelo_2.on()

    time.sleep(1)

    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////


    led_vermelho_1.off()

    led_amarelo_2.off()

    led_verde_1.on()

    led_vermelho_2.on()

    time.sleep(3)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_verde_1.off()

    led_amarelo_1.on()

    time.sleep(1)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_vermelho_2.off()

    led_amarelo_1.off()

def semaforo1_rapido_loop():

    led_vermelho_2.on()

    led_verde_1.on()
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    time.sleep(6)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////


    led_verde_1.off()

    led_amarelo_1.on()



    time.sleep(1)

    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_vermelho_2.off()

    led_amarelo_1.off()

    led_verde_2.on()

    led_vermelho_1.on()

    time.sleep(3)

    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_verde_2.off()

    led_amarelo_2.on()

    time.sleep(1)
    #///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
    #converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
    #///////leitura//////

    led_vermelho_1.off()

    led_amarelo_2.off()

# programa
while True:

#///////////////////////potenciometro/////////////////////////////

#///////leitura//////
    pot_value_1 = pot1.read()
    pot_value_2 = pot2.read()
#converte o valor do potenciometro de o - 1023 para 0 - 100
    pot_1 = convert(pot_value_1, 1023,0,100,0) 
    pot_2 = convert(pot_value_2, 1023,0,100,0) 
#///////leitura//////

    print("\n")
    print("--------------------------------------------------")
    print(f"Rua principal: {pot_1}")
    print(f"Rua secundária: {pot_2}")
    print("--------------------------------------------------")
    print("\n")
#///////////////////////potenciometro/////////////////////////////
    
    #diferença de carros entre as ruas //abs(fuciona como o módulo da matematica)
    diferenca = abs(pot_value_1 - pot_value_2)

    if pot_1 == 0 and pot_2 == 0:
        desligar_aleds()
        #display_1
        Icd.clear()
        Icd.move_to(0,0)
        Icd.putstr(f'Rua 1: {pot_1}')
        Icd.move_to(0,1)
        Icd.putstr(f'Rua 2: {pot_2}')
        #display_1

        semaforo_normal_loop()

        #///////leitura//////
        pot_value_1 = pot1.read()
        pot_value_2 = pot2.read()
        #converte o valor do potenciometro de o - 1023 para 0 - 100
        pot_1 = convert(pot_value_1, 1023,0,100,0) 
        pot_2 = convert(pot_value_2, 1023,0,100,0) 
        #///////leitura//////

    elif pot_1 > 0 and pot_2 == 0:
        
        if pot_1_backUP != pot_1:

            pot_1_backUP = pot_1

            desligar_aleds()
            

            #display_1
            Icd.clear()
            Icd.move_to(0,0)
            Icd.putstr(f'Rua 1: {pot_1}')
            Icd.move_to(0,1)
            Icd.putstr(f'Rua 2: {pot_2}')
            #display_1
            led_vermelho_2.on()
            led_verde_1.on()







        #///////leitura//////
        pot_value_1 = pot1.read()
        pot_value_2 = pot2.read()
        #converte o valor do potenciometro de o - 1023 para 0 - 100
        pot_1 = convert(pot_value_1, 1023,0,100,0) 
        pot_2 = convert(pot_value_2, 1023,0,100,0) 
        #///////leitura//////

    elif pot_1 == 0 and pot_2 > 0:
        if pot_1_backUP_1 != pot_1:

                pot_1_backUP_1 = pot_1
                desligar_aleds()
                #display_1
                Icd.clear()
                Icd.move_to(0,0)
                Icd.putstr(f'Rua 1: {pot_1}')
                Icd.move_to(0,1)
                Icd.putstr(f'Rua 2: {pot_2}')
                #display_1

                led_vermelho_1.on()
                led_verde_2.on()








        #///////leitura//////
        pot_value_1 = pot1.read()
        pot_value_2 = pot2.read()
        #converte o valor do potenciometro de o - 1023 para 0 - 100
        pot_1 = convert(pot_value_1, 1023,0,100,0) 
        pot_2 = convert(pot_value_2, 1023,0,100,0) 
        #///////leitura//////
    elif diferenca >= 10:
        if pot_1 != 0 and pot_2 != 0 and pot_1 > pot_2:
            desligar_aleds()       
            #display_1
            Icd.clear()
            Icd.move_to(0,0)
            Icd.putstr(f'Rua 1: {pot_1}')
            Icd.move_to(0,1)
            Icd.putstr(f'Rua 2: {pot_2}')
            #display_1



            semaforo1_rapido_loop()

            #///////leitura//////
            pot_value_1 = pot1.read()
            pot_value_2 = pot2.read()
            #converte o valor do potenciometro de o - 1023 para 0 - 100
            pot_1 = convert(pot_value_1, 1023,0,100,0) 
            pot_2 = convert(pot_value_2, 1023,0,100,0) 
            #///////leitura//////


        elif pot_1 != 0 and pot_2 != 0 and pot_2 > pot_1:
            
            desligar_aleds()

            #display_1
            Icd.clear()
            Icd.move_to(0,0)
            Icd.putstr(f'Rua 1: {pot_1}')
            Icd.move_to(0,1)
            Icd.putstr(f'Rua 2: {pot_2}')
            #display_1

            semaforo2_rapido_loop()

            #///////leitura//////
            pot_value_1 = pot1.read()
            pot_value_2 = pot2.read()
            #converte o valor do potenciometro de o - 1023 para 0 - 100
            pot_1 = convert(pot_value_1, 1023,0,100,0) 
            pot_2 = convert(pot_value_2, 1023,0,100,0) 
            #///////leitura//////
    else:
        #display_1
        Icd.clear()
        Icd.move_to(0,0)
        Icd.putstr(f'Rua 1: {pot_1}')
        Icd.move_to(0,1)
        Icd.putstr(f'Rua 2: {pot_2}')
        #display_1

        semaforo_normal_loop()

        #///////leitura//////
        pot_value_1 = pot1.read()
        pot_value_2 = pot2.read()
        #converte o valor do potenciometro de o - 1023 para 0 - 100
        pot_1 = convert(pot_value_1, 1023,0,100,0) 
        pot_2 = convert(pot_value_2, 1023,0,100,0) 
        #///////leitura//////