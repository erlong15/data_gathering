# Тестовый проект по курсу BIG DATA

вызов *gather* скачивает заданное число курсов с coursera 
и сохраняет следующую информацию в файле scrapped_data.json
в виде 1 json =  1 строка
```json
{"start_date": "Starts Nov 06", 
"title": "Introduction to Virtual Reality", 
"insttructor": "   Dr Sylvia Xueni Pan,  Lecturer, Department of Computing    Dr Marco Gillies, Senior Lecturer", 
"commitment": " 4 weeks of study, 3-5 hours/week", 
"language": "English", "rating": "4.8 stars", 
"uri": "https://www.coursera.org/learn/introduction-virtual-reality"}
```
вызов *tranform* конвертирует scrapped_data.json в data.csv

вызов *stats* выдает статистистические параметры по языкам используемым в курсах


# Как запустить
```bash
python -m gathering -h
INFO:__main__:Work started
usage: gathering.py [-h] [-c COUNT] action

data collector

positional arguments:
  action                required action (gather, transform, stats)

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        How much courses do you want to scrape (default: 100)
```

# Дополнительные источники данных, которые могут быть использованы
1. букмекерские сайты (bwin.com, betway.com, unibet.com) - анализ коэффициентов на спортивные события
2. hh.ru - съем информации по поиску работы
3. auto.ru -  данные о продаже автомобилей
4. avito.ru - объявления о покупке/продаже
5. отельные сайты (booking.com, tripadvisor.com, expedia.com) - данные о бронировании, отзывы
6. билетные сайты (scyscanner.ru, aviasales.ru) - поиск дешевых билетов
7. новостные сайты (lenta.ru, meduza.ru, rbc.ru) - анализ новостных вбросов
8. биржевые данные - рассчет торговых стратегий
9. сайт недвижимости cian.ru, reality.yandex.ru
10. соцсети (vc.ru, fb, twitter) - отслеживание любой активности
11. upwork.com - мониторинг заказов на фриланс
12. обучающие сайты (coursera, geeekbrains) - анализ заинтересовнности 
13. habrhabr.ru -  мониторинг трендов в IT
14. imdb.com - анализ кинорынка
15. погодные сайты - анализ и мониторинг погоды в мире
16. github.com - анализ новых проектов в ИТ
17. https://apidata.mos.ru/ - много полезного для анализа
18. криптовалюты - база биткоина например
19. http://ar.gov.ru/inform_otkritost_05_otkritii_dannie_po_foiv/index.html
20. librusec - задачка на определение жанров книг

