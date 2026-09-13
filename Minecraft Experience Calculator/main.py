# app.py
from flask import Flask, render_template, request

app = Flask(__name__)


MOB_XP = {
    "Обычный моб (зомби, скелет)": 5,
    "Крипер": 5,
    "Корова": 1,
    "Свинья": 1,
    "Взрослый житель": 3,
    "Голем": 15,
    "Дракон Края": 12000,
    "Визер": 500,
    "Убийство игрока": 500,
    "Плавка руды": 1,
    "Торговля с жителем": 3,
    "Рыбалка": 1
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            current_level = int(request.form['current_level'])
            target_level = int(request.form['target_level'])

            diff = target_level - current_level
            result = diff * 1000 if diff > 0 else 0
        except ValueError:
            result = "Введите корректные числа"

    return render_template('index.html', result=result, mob_xp=MOB_XP)

if __name__ == '__main__':
    app.run(debug=True)
