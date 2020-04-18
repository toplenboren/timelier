# timelier
Сервер, который врёт время по UDP.

Задача с курса «Протоколы интернета» с мат-меха

# Сервер: /timeserver

## Конфигурация:
```
cd ./timeserver
./configuration.yml
```

Изменить значение «Дельты» на которое врет таймсервер можно в файле configuration.yml в папке timeserver

## Запуск:

Для первого запуска:

```
cd ./timeserver
pip install -r requirements.txt # Установка pyyaml — модуля для работы с .yml-файлами
```

```
cd ./timeserver
python main.py # Теперь сервер слушает UDP на 127.0.0.1:123
```

Для остановки сервера — закройте терминал

Формат общения с сервером: Восьмибайтовое UDP-сообщение, например `givetime`
 
# Клиент: /timeclient

## Запуск:

```
cd ./timeclient 
python main.py # Сразу же отправит сообщение givetime на 127.0.0.1:123 и выведет результат 
``` 
