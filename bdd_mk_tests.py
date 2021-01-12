# класс для разбора подпрограмм для создания циклограмм
# циклограмма согласно данному шаблону
# ["Name", [[Address, Subaddress, Wr/R, [Data], Data leng, Start time, Finish time, Interval, Delay], [...], [...]]]
#    |          |          |        |      |         |          |           |          |         |
#    |          |          |        |      |         |          |           |          |         -- Задержка отправки
#    |          |          |        |      |         |          |           |          --- Интервал отправки
#    |          |          |        |      |         |          |           - Время остановки посылок
#    |          |          |        |      |         |          --- Время старта отправки от запуска программы
#    |          |          |        |      |         --- Длина данных для приема/отправки
#    |          |          |        |      ------------- Данные для отправки (при приеме не имеет значения)
#    |          |          |        -------------------- Отправка - "0", Прием - "1"
#    |          |          ----------------------------- Подадрес
#    |          ---------------------------------------- Адрес ОУ
#    --------------------------------------------------- Имя циклограммы

# опрос всего:

all_test = ["Опрос БДД с МК", [
            # Чтение информационного кадра БДД
            [13, 1, 1, [], 32, 5, 3600, 1, 0.0],
            ]]