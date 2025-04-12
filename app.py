from flask import Flask, render_template, request
from calculos import calcular_imc, calcular_tmb, calcular_calorias, calcular_macros

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/resultados', methods=['POST'])
def resultados():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    sexo = request.form['sexo']
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    actividad = float(request.form['actividad'])
    objetivo = request.form['objetivo']

    imc = round(calcular_imc(peso, altura), 2)
    tmb = round(calcular_tmb(peso, altura, edad, sexo), 2)
    calorias = round(calcular_calorias(tmb, actividad, objetivo), 2)
    prote, grasa, carbo = calcular_macros(calorias, peso)

    return render_template('resultados.html', nombre=nombre, imc=imc, tmb=tmb, calorias=calorias,
                           prote=prote, grasa=grasa, carbo=carbo)

if __name__ == '__main__':
    app.run(debug=True)
