from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    if not (10 <= nota1 <= 70) or not (10 <= nota2 <= 70) or not (10 <= nota3 <= 70):
        return "Error: Las notas deben estar entre 10 y 70"

    if not (0 <= asistencia <= 100):
        return "Error: La asistencia debe estar entre 0 y 100"

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    return render_template('resultado.html',
                           ejercicio=1,
                           promedio=round(promedio, 1),
                           asistencia=asistencia,
                           estado=estado)


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    nombre1 = request.form['nombre1'].strip()
    nombre2 = request.form['nombre2'].strip()
    nombre3 = request.form['nombre3'].strip()

    if not nombre1 or not nombre2 or not nombre3:
        return "Error: Todos los nombres deben ser completados"

    nombres = [
        {'nombre': nombre1, 'longitud': len(nombre1)},
        {'nombre': nombre2, 'longitud': len(nombre2)},
        {'nombre': nombre3, 'longitud': len(nombre3)}
    ]

    nombre_mas_largo = max(nombres, key=lambda x: x['longitud'])

    return render_template('resultado.html',
                           ejercicio=2,
                           nombre_mas_largo=nombre_mas_largo['nombre'],
                           longitud=nombre_mas_largo['longitud'],
                           todos_nombres=nombres)


if __name__ == '__main__':
    app.run(debug=True)