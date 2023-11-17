# Движок Flask для сайта
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Ядро API

#import logging

# Админ панелька
import datetime

# Для вычислений
import numpy as np
import sympy as sp

app = Flask(__name__)
CORS(app)
from app import views


@app.route("/admin", methods=["POST"])
def admin():
    selected_server = request.form.get("server")
    # Ваш код обработки выбора сервера здесь

    return f"Выбран сервер: {selected_server}"


@app.route("/api/data", methods=["GET"])
def get_data():
    data = {"message": "Привет, это данные с сервера!"}
    return jsonify(data)


# Метод для вычисления определителя матрицы
def calculate_determinant(matrix):
    return np.linalg.det(matrix)


def stringres(string):
    temp = ""
    i = 0
    while i < len(string):
        if i < len(string) and string[i] == "*" and string[i + 1] == "*":
            temp += "^"
            i += 2
        else:
            temp += string[i]
            i += 1
    # print(temp)
    return temp


def calculate_integral(func, a, b):
    # Задаем символьные переменные
    x, y = sp.symbols("x y")

    # Вводим выражение с клавиатуры
    expr_str = func

    # Парсим выражение
    expr = sp.sympify(expr_str)

    # Интегрируем по x
    integral_result = sp.integrate(expr, (x, a, b))

    # Выводим результат
    # print(f"Результат интегрирования по x: {integral_result}")

    return stringres(str(integral_result))


@app.errorhandler(404)
def page_not_found(e):
    log("Это предупреждение 404", level="warning")
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    log("Это сообщение об ошибке 500", level="error")
    return render_template("500.html"), 500


@app.route("/status")
def status():
    log("Запрос на STATUS", level="info")
    return """<div style='display:flex; width:auto; max-width:460px;border: 2px solid; border-radius: 15px;'>
            <svg style='padding: 10px' width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="16" cy="16" r="16" fill="#00FF33"/>
            </svg>
            <h1 style='padding: 8px; width:auto; display:flex; margin: 0px 0px 0px 20px'>API REQUEST ACTIVE</h1>
        </div>"""


# Роут для приема матрицы и отправки определителя в JSON
@app.route("/calculate_determinant", methods=["POST"])
def calculate_determinant_route():
    log("Запрос на вычисление определителя ", level="info")
    matrix = request.json["matrix"]
    try:
        determinant = calculate_determinant(matrix)
        return jsonify({"result": determinant})
    except:
        return jsonify({"result": "Error"})


@app.route("/calculate_integral", methods=["POST"])
def calculate_integral_route():
    log("Запрос на вычисление интеграла ", level="info")
    function = request.json["function"]
    a = request.json["a"]
    b = request.json["b"]
    try:
        result = calculate_integral(function, a, b)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": str(e)})


def log(message, level):
    now = datetime.datetime.now()
    with open("log.txt", "a") as file:
        file.write(f"{now} {message} {level}" + "\n")


if __name__ == "__main__":
    app.run(debug=False)
