import numpy as np
#list of available cars in R and C garage and their prices
cars = {
        "toyota corolla":100000,
        "toyota camry":80000,
        "honda civic":90000,
        "honda accord":75000,
        "honda crv":100000,
        "toyota rav4":120000,
        "ford focus":70000,
        "bugatti chhiron":800000,
        "bugatti veyron":750000,
        "lamborghini aventador":650000,
        "mercedes benz c-class":350000,
        "mercedes benz GLE":400000,
        "mercedes benz s-class":450000,
        "mercedes benz GLC":350000,
        "mercedes benz AMG":500000,
        "bmw x5":200000,
        "audi A3":130000,
        "audi Q5":150000,
        "audi Q8":150000,
        "hyundai elantra":80000,
        "tesla":400000,
        "hyundai tucson ":200000,
        "range rover":350000,
        "rolls royce":1000000,
        "lexux":400000,
        "hyundai sonata":75000,
        "hyundai santafe":100000,
        "porschhe":120000,
        "chevrolet":100000,
        "jaguar":120000,
        "bently":450000,
        "dodge":200000,
        "highlander":300000,
        "landcruiser":350000,
        "prado":400000,
        "renault":350000,
        }

dialogue =input("Welcome, which car are you looking to purchase? :")
#check if car name is in the list of cars in R and C garage
if dialogue in cars:
          print('Yes, we have '  +  dialogue.upper() + ' available.')
          price = cars[dialogue]
          print(dialogue.upper() + ' goes for GHc.' + str(price))
else:
          print("Sorry, we don't have" + dialogue + ' available. Would you be interested in any of the following though? :')
          a = cars.keys()
          print(a)
          
          
          
         #6945721