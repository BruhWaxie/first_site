from flask import Flask, render_template


app = Flask(__name__)  # Створюємо веб–додаток Flask


@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    return render_template("index.html")  # html-сторінка, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження