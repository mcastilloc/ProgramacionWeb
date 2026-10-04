from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            nombre = request.form["nombre"].strip()
            edad = int(request.form["edad"])
            cantidad = int(request.form["cantidad"])

            if not nombre or edad < 0 or cantidad < 1:
                raise ValueError

            total_sin_descuento = cantidad * PRECIO_TARRO

            if 18 <= edad <= 30:
                descuento = 15
            elif edad > 30:
                descuento = 25
            else:
                descuento = 0

            total_pagar = total_sin_descuento * (1 - descuento / 100)
            total_descuento = total_sin_descuento - total_pagar

            resultado = {
                "nombre": nombre,
                "total_sin_descuento": total_sin_descuento,
                "total_descuento": total_descuento,
                "total_pagar": total_pagar
            }

        except ValueError:
            error = "Ingresa datos válidos. La cantidad debe ser mayor que cero."

    return render_template(
        "ejercicio1.html",
        resultado=resultado,
        error=error
    )


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    correcto = None

    if request.method == "POST":
        usuario = request.form["usuario"].strip()
        contrasena = request.form["contrasena"]

        usuarios = {
            "juan": {"contrasena": "admin", "rol": "administrador"},
            "pepe": {"contrasena": "user", "rol": "usuario"}
        }

        if usuario in usuarios and usuarios[usuario]["contrasena"] == contrasena:
            mensaje = f"Bienvenido {usuarios[usuario]['rol']} {usuario}"
            correcto = True
        else:
            mensaje = "Usuario o contraseña incorrectos"
            correcto = False

    return render_template(
        "ejercicio2.html",
        mensaje=mensaje,
        correcto=correcto
    )


if __name__ == "__main__":
    app.run(debug=True)