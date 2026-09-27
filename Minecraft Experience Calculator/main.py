from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

MOB_XP = {
    "Зомби": 5,
    "Скелет": 5,
    "Крипер": 5,
    "Корова": 1,
    "Свинья": 1,
    "Житель": 3,
    "Железный голем": 15,
    "Дракон Края": 12000,
    "Визер": 500,
    "Убийство игрока": 500,
    "Плавка руды": 1,
    "Торговля с жителем": 3,
    "Рыбалка": 1
}

@app.route("/minecraft-bg.jpg")
def background():
    return send_from_directory(".", "minecraft-bg.jpg")

@app.route("/night-bg.png")
def night_background():
    return send_from_directory(".", "night-bg.png")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            current_level = int(request.form["current_level"])
            target_level = int(request.form["target_level"])
            difference = target_level - current_level
            result = difference * 1000 if difference > 0 else 0
        except ValueError:
            result = "Ошибка"

    return render_template("index.html", result=result, mob_xp=MOB_XP)

if __name__ == "__main__":
    app.run(debug=True)
