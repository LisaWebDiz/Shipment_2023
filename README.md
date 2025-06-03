### Shipment Project 2023
### Description
Test task for middle python django developer.  
Web приложения поиска грузов.  
Выгрузка конкретных столбцов из списка csv файла локаций в определенные поля базы данных Postgres при загрузке csv файла.  
Создание базы данных грузовиков по умолчанию с рандомными номерами в формате "число от 1000 до 9999 + случайная заглавная буква английского алфавита" в поле "номер" и рандомными локациями в поле "местонахождение".  
Фикстура для загрузки базы данных грузовиков по умолчанию.  
API баз данных: локаций, грузовиков, грузов.  
Поиск груза по ID.  
Вывод списка грузовиков, редактирование грузовика.  
Вывод списка грузов, редактирование, удаление груза.  


### Quick start
```bash
git clone https://github.com/yourusername/shipment_2023.git
cd shipment_2023.git
cp example.env .env

python3 -m venv venv  
source ./venv/bin/activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver

Enjoy!
