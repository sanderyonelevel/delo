from flask import Flask, request, jsonify
from flask_cors import CORS  # Добавляем CORS

app = Flask(__name__)
CORS(app, resources={r"/submit": {"origins": "*"}})  # Разрешаем все источники

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()  # Получаем JSON-данные
    if not data:
        return jsonify({"error": "Нет данных"}), 400  # Ошибка, если данных нет

    print(f"Получены данные: {data}")  # Вывод в консоль
    return jsonify({"status": "success", "message": "success", "data": data})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
