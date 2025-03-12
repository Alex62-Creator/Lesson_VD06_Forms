#Импортируем объект класса Flask
from app import app

#Используем условие для проверки, что скрипт запускается напрямую
if __name__ == "__main__":
    app.run(debug=True)