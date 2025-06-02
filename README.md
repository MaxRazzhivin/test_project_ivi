# Ivi.tv
![main page screenshot](resources/main%20screen%20page.png)

## Description:
В этом репозитории:
- Демо-проект с <b>автотестами</b> на <b>Python</b>.
- Настроен запуск тестов "одной кнопкой" с любого компьютера со стабильным интернетом. Установка ПО не требуется.
- Визуальный отчет о прохождении тестов. Отчет может сформировать любой сотрудник: оценить тестовое покрытие и/или передать разработчикам информацию о проблеме.
- После выполнения каждого теста записывается видео и скриншот экрана.
- Уведомление о результатах тестов в <b>Telegram</b> группу.
- Запуск мобильных автотестов на Андроид через Appium (локальный запуск через установленное приложение на девайсе из play market)

## Stack:
<code><img src="resources/StackIcons/python.svg" width="40" height="40" alt="Python"  title="Python" /></code>
<code><img src="resources/StackIcons/pycharm.png" width="40" height="40" alt="PyCharm" title="PyCharm"></code>
<code><img src="resources/StackIcons/pytest.png" width="40" height="40"  alt="PyTest" title="PyTest"></code>
<code><img src="resources/StackIcons/selene.png" width="40" height="40"  alt="Selene" title="Selene"></code>
<code><img src="resources/StackIcons/Allure.svg" width="40" height="40"  alt="Allure" title="Allure"></code>
<code><img src="resources/StackIcons/selenoid.png" width="40" height="40"  alt="Selenoid " title="Selenoid"></code>
<code><img src="resources/StackIcons/Jenkins.svg" width="40" height="40"  alt="Jenkins " title="Jenkins"></code>
<code><img src="resources/StackIcons/appium.png" width="40" height="40"  alt="Appium " title="Appium"></code>
<code><img src="resources/StackIcons/allure_testops.png" width="40" height="40"  alt="Testops " title="Testops"></code>
<code><img src="resources/StackIcons/Telegram.svg" width="50" height="40" alt="Telegram"  title="Telegram"></code>
<br>
- Язык: `Python`
- Для написания UI-тестов используется фреймворк `Selene`, современная «обёртка» вокруг `Selenium WebDriver`
- Библиотека модульного тестирования: `PyTest`
- `Jenkins` выполняет удаленный запуск тестов в графическом интерфейсе. Установки дополнительных приложений на компьютер пользователя не требуется.
- `Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)
- Фреймворк`Allure Report` собирает графический отчет о прохождении тестов
- После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант Allure Report
- Мобильные тесты выполняются только локально - т.к. нет в общем доступе установочного .apk (иначе можно сделать и через браузерную ферму Browserstack)
- При локальном запуске отчет в телеграм не отправляется, но возможно посмотреть аллюр отчет через команду allure serve {путь до папки allure-reports}

## Tests:
- [x] Отображается главная страница и основные разделы сайта (мой иви, фильмы, сериалы, мультфильмы)
- [x] Основные разделы кликабельны и по ним можно перейти
- [x] Проверка авторазации на сайте
- [x] Поиск фильма на сайте и переход в его карточку
- [x] Добавление фильма в избранное (список - "буду смотреть") и проверка в личном кабинете

## Mobile Tests:
- [x] Отображается главная страница и основные разделы сайта (мой иви, поиск, поток, избранное, войти)
- [x] Проверка функции поиска и результата поиска, переход на карточку фильма
- [x] Проверка авторизации в приложении - введение логина/пароля и проверка результата в личном кабинете

----


### Удаленный запуск тестов (<b>Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/qa.guru_18_14/">Job</a></b>)
<details>
   <summary>Краткая инструкция</summary>

###### А: 

<i>Незарегистрированным</i> пользователем открыть готовый, ранее сформированный отчет (желтая иконка, стрелка №2 на скриншоте)
<p>Результат: откроется страница с отчетом Allure Report</p>

###### Б: 
<i>Зарегистрированным</i> пользователем: 
1. Перейти на страницу сборки проекта
2. Выбрать "Build now" в графическом интерфейсе.
3. Запустить выполнение тестов кнопкой "Build"
4. Убедиться, что в блоке "Builds" появилась новая запись.
5. Дождаться окончания активного процесса (~2-3 мин)
6. Кликнуть по значку или тексту Allure Report либо Allure Testops
<p>Результат: откроется страница с отчетом Allure Report</p>

> <p>Срок хранения сборки на сервере ~60 дней. Ссылка на Job может оказаться недоступной после 28.07.2025</p>

<p>Образец:</p>

<br>![Jenkins](resources/jenkins-screen.png)

</details>

----

## Локальный запуск автотестов - если Jenkins не работает:

### Для запуска web/UI автотестов скачать репозиторий и выполнить в терминале:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/web/.
```

### Получение отчёта после завершения теста:
```bash
allure serve tests/web/allure-results
```


### Для локального запуска mobile автотестов выполнить процедуру:

- [x] Установить appium - brew install appium
- [x] Подсоединить телефон или подключить эмулятор телефона
- [x] Проверить через команду adb devices (для Андроида), что система видит наш девайс
- [x] Запустить Аппиум сервер - в терминале команда "appium"

### Далее выполнить:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/android/.
```

### Получение отчёта:
```bash
allure serve tests/android/allure-results

```

----



## Allure: пример отчета
<details>
   <summary>Скриншоты</summary>

###### Главный экран (Overview)
![Screen Allure1](resources/allure-main-screen.png)
###### Страница со списком тестов (Graph)
![Screen Allure2](resources/allure-graphs.png)
###### Пример описания теста
![Screen Allure3](resources/allure-test-suites.png)

</details>

## Видео тестов
Видеозапись каждого web-теста генерируется с помощью `Selenoid`, после успешного запуска контейнера c тестами в `Docker`.

----


![Video test](resources/video-report.gif)


### Gif прохождения mobile автотестов на Android
![autotest_gif](resources/Firsttest-ezgif.com-crop.gif)
![autotest_gif](resources/Secondtest-ezgif.com-crop.gif)
![autotest_gif](resources/3rdtest-ezgif.com-crop.gif)

### Gif прохождения mobile автотестов на iOS
![autotest_gif](resources/test_main_screen.gif)
![autotest_gif](resources/test_search_text.gif)
![autotest_gif](resources/test-authorize_user.gif)


## Отчет в Telegram (падает в случае прохождения через CI/CD Jenkins)
После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.
Чтобы видеть его увидеть, вступите (временно) в канал `https://t.me/allure_reports_max`


![Telegram](resources/messg_telegram.png)

## Полная статистика хранится в Allure TestOps

> [Ссылка на проект в AllureTestOps](https://allure.autotests.cloud/project/4695/dashboards)

#### Дашборд с общими показателями тестовых прогонов

![This is an image](resources/testops%20main%20screen.png)

#### История запуска тестовых наборов

![This is an image](resources/testops%20test%20runs.png)

#### Тест кейсы

![This is an image](resources/testops-test-suits.png)

#### Тестовые артефакты

![This is an image](resources/test_artefacts.png)

----

### Интеграция с Jira

> [Ссылка на проект в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1430)

![This is an image](resources/jira%20screen.png)
