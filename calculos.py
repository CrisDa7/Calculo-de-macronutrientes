#formula para calcular el imc
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


#formula para calcular la tmb (tasa metabolica basal)
def calcular_tmb(peso, altura, edad, sexo):
    altura_cm = altura * 100
    if sexo == 'masculino':
        return 10 * peso + 6.25 * altura_cm - 5 * edad + 5
    else:
        return 10 * peso + 6.25 * altura_cm - 5 * edad - 161

#formula para calcular las calorias
def calcular_calorias(tmb, actividad, objetivo):
    calorias = tmb * actividad
    if objetivo == 'bajar':
        calorias -= 500
    elif objetivo == 'subir':
        calorias += 500
    return calorias

#formula para calcular los macronutrientes 
def calcular_macros(calorias, peso):
    proteinas = round(peso * 2.2)  
    grasas = round(peso * 1.2)     
    calorias_prote = proteinas * 4
    calorias_grasa = grasas * 9
    calorias_carb = calorias - calorias_prote - calorias_grasa
    carbos = round(calorias_carb / 4)
    return proteinas, grasas, carbos
