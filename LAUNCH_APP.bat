:: создание виртуальной среды
set VENV_NAME=venv
python -m venv %VENV_NAME%

:: активация виртуальной среды
CALL .venv/Scripts/activate

:: установка внешних зависимостей
pip install -r requirements.txt

:: запуск приложения
set %APP_PATH=./app/app.py
flask --app %APP_PATH% run --host=0.0.0.0

