uitleg0 = 'Dit is een meethulp om te berekenen\nhoe warm het badwater kan worden\nna het toevoegen van (liefst) kokend water.\n\nHierbij wordt rekening gehouden met:\n\n1: De helling waarop het zwembad staat.\n2: Het maximale volume wat hierdoor kleiner wordt dan\n   wanneer het bad waterpas staat.\n3: Het max volume dat nog toegevoegd kan worden.\n\nU hoeft enkel de instructies op te volgen:\n'

uitleg1 = 'De inhoud van het bad is nu '
uitleg1a = 'liter.'
uitleg2 = 'De maximale inhoud is: '
uitleg2a = ' liter.'
uitleg3 = 'Er kan dus nog '
uitleg3a = ' liter worden bijgevuld.'
uitleg4 = 'Als u dit doet met water van '
uitleg4a = 'graden celcius, '
uitleg4b = 'dan wordt de temperatuur van een '
uitleg4c = 'maximaal gevuld bad '
uitleg4d = ' graden celcius.'
print(uitleg0)
error = 'Dat kan niet'
goede_invoer = False
while not goede_invoer:
    try:
        instructie = float(input('Afstand liner tot water in cm (raamkant): '))
        if 7 < instructie < 91.5:
            print('Dank je.')
            goede_invoer = True
        else:
            print('Maximale afstand moet kleiner zijn dan 91.5 cm ')
            print('en groter dan 7 cm')
    except ValueError:
        print(error)
water_niv_nu = (95 - float(instructie) + 3.5)
print ('Het huidig waterniveau is: ' + str(water_niv_nu) + ' cm')
water_niv_max = 91.5
inhoud_max = 1541
goede_invoer2 = False
while not goede_invoer2:
    try:
        temp_nu = float(input('Voer huidige temperatuur in: '))
        if  0 < temp_nu < 40:
            print('Dank je.')
            goede_invoer2 = True
        else:
            print('Vul een getal in tussen 0 en 40')
    except ValueError:
        print(error)
inhoud_nu = (inhoud_max/water_niv_max) * water_niv_nu
inhoud_extra = (inhoud_max - inhoud_nu)
goede_invoer3 = False
while not goede_invoer3:
    try:
        temp_extra = float(input('Temperatuur toegevoegd water: '))
        if  0 < temp_extra <= 100:
            print('Dank je.')
            goede_invoer3 = True
        else:
            print('Vul een getal in tussen de 0 en 100')
    except ValueError:
        print(error)
temp_eind = float(round((inhoud_nu * temp_nu) + (inhoud_extra * temp_extra)) / (inhoud_nu + inhoud_extra))
print(' ')
print(uitleg1 + str(round(inhoud_nu,1)) + ' ' + uitleg1a)
print(uitleg2 + str(round(inhoud_max,1)) + uitleg2a)
print(uitleg3 + str(round(inhoud_extra,1)) + ' ' + uitleg3a)
print(uitleg4 + str(round(temp_extra,1)) + ' ' + uitleg4a)
print(uitleg4b + uitleg4c + str(round(temp_eind,1)) + uitleg4d)
print('')
conclusie = False
while not conclusie:
  try:
    if 20 < temp_eind <= 40:
     print('Dat is een lekker temperatuurtje')
     conclusie = True
    elif 1 < temp_eind <= 20:
      print('Dat is nog steeds wel erg koud')
      conclusie = True 
    else:
      print('Misschien is een koud bad wel net zo makkelijk en gezond.')
      conclusie = True
  except ValueError:
    print(error)  
print(" ")
print('Maar misschien wilt u zelf bepalen\nhoeveel water u toe wilt voegen\nof wat de gewenste temperatuur moet worden.')

eind1 = 'Met '
eind2 = ' liter water, wordt de temperatuur '
eind3 = ' graden celcius.'
eind4 = 'Voor een gewenste temperatuur van '
eind5 = ' graden celcius, '
eind6 = 'heeft u '
eind7 = ' liter water nodig van '
eind8 = ' graden celcius.'

conclusie1 = False
while not conclusie1:
 try:
  keuze = int(input('Maak een keuze:\n1. Voeg vaste hoeveelheid water toe\n2. Bepaal gewenste temperatuur\n'))   
  if keuze == 1:
     conclusie2 = False
     while not conclusie2:
       try:
         keuze1 = float(input('Aantal liters toe te voegen: '))
         if 1 < keuze1 <= inhoud_extra:
           temp_eind2 = ((inhoud_nu*temp_nu) + (keuze1*temp_extra)) / (inhoud_nu + keuze1)
           print(eind1 + str(round(keuze1,1)) + eind2 + str(round(temp_eind2,1)) + eind3)
           conclusie2 = True
         else:
           print('Vul een waarde in tussen 1 en ' + str(round(inhoud_extra,1)) + ' liter')
       except ValueError:
         print(error)
     conclusie1 = True     
  elif keuze == 2:
     conclusie3 = False
     while not conclusie3:
       try:
         keuze2 = float(input('Gewenste temperatuur: '))
         if float(temp_nu) < keuze2 <= float(temp_eind):
           inhoud_extra2 = ((inhoud_nu*temp_nu) - (inhoud_nu*keuze2)) / (keuze2 - temp_extra)
           print(eind4 + str(keuze2) + eind5 + eind6 + str(round(inhoud_extra2,1)) + eind7 + str(round(temp_extra,1)) + eind8)
           conclusie3 = True
         else:
           print('Vul een temperatuur in tussen de ' + str(round(temp_nu,1)) + ' en '+ str(round(temp_eind,1)) + ' graden celcius')
       except ValueError:
           print(error)
     conclusie1 = True        
  else:
     print(error)                  
 except ValueError:
           print(error)      

print('')
print('               _'      )
print('              | |'     )
print('           ___| |___'  )
print('          |___   ___|' )
print('              | |'     )
print('              | |'     )
print('              | |'     )
print('              |_|'     )
print('          JEZUS LEEFT!')
print('')




