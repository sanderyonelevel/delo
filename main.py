from flask import Flask, request, jsonify, redirect
from flask_cors import CORS  # Добавляем CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/submit": {"origins": "*"}})  # Разрешаем все источники

file_path = 'data.json'  # Путь к файлу, где будут храниться данные


@app.route('/')
def home():
    return redirect("https://unitpay.ru", code=301) 

@app.route('/pay/<token>')
def pay_page(token):
    return render_template('index.html', token=token)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()  # Получаем JSON-данные
    if not data:
        return jsonify({"error": "Нет данных"}), 400  # Ошибка, если данных нет

    # Чтение существующих данных из файла
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        json_data = []  # Если файл не существует, создаем новый список

    # Добавляем новые данные
    json_data.append(data)

    # Записываем обновленные данные обратно в файл
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"Получены данные: {data}")  # Вывод в консоль
    return jsonify({"status": "success", "message": "success", "data": data})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

