#Импрортируем необходимые библиотеки
from flask import render_template, request, redirect, url_for

#Импортируем объект класса Flask
from app import app

#Инициализируем пустой список users для хранения карточек
users = []
print("Start")

#Создаем маршрут: используем @app.route("/", methods=["GET", "POST"]) для определения главного маршрута с методами GET и POST
@app.route('/', methods=['GET', 'POST'])
def form():
    #Используем метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
        #Функция request.form извлекает значение из соответствующих полей
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        #Создаём условие для проверки наличия данных в полях
        if name and city and hobby and age:
            users.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
        #Используем для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('form'))
    #Возвращаем отрендеренный шаблон с переданными данными анкеты
    return render_template('form.html', users=users)



