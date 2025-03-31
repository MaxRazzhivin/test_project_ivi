# Ivi.tv
![main page screenshot](images/main%20screen.png)

## Description:
В этом репозитории:
- Демо-проект с <b>автотестами</b> на <b>Python</b>.
- Настроен запуск тестов "одной кнопкой" с любого компьютера со стабильным интернетом. Установка ПО не требуется.
- Визуальный отчет о прохождении тестов. Отчет может сформировать любой сотрудник: оценить тестовое покрытие и/или передать разработчикам информацию о проблеме.
- После выполнения каждого теста записывается видео и скриншот экрана.
- Уведомление о результатах тестов в <b>Telegram</b> группу.

## Stack:
<code><img src="images/StackIcons/python.svg" width="40" height="40" alt="Python"  title="Python" /></code>
<code><img src="images/StackIcons/pycharm.png" width="40" height="40" alt="PyCharm" title="PyCharm"></code>
<code><img src="images/StackIcons/pytest.png" width="40" height="40"  alt="PyTest" title="PyTest"></code>
<code><img src="images/StackIcons/selene.png" width="40" height="40"  alt="Selene" title="Selene"></code>
<code><img src="images/StackIcons/Allure.svg" width="40" height="40"  alt="Allure" title="Allure"></code>
<code><img src="images/StackIcons/selenoid.png" width="40" height="40"  alt="Selenoid " title="Selenoid"></code>
<code><img src="images/StackIcons/Jenkins.svg" width="40" height="40"  alt="Jenkins " title="Jenkins"></code>
<code><img src="images/StackIcons/Telegram.svg" width="50" height="40" alt="Telegram"  title="Telegram"></code>
<br>
- Язык: `Python`
- Для написания UI-тестов используется фреймворк `Selene`, современная «обёртка» вокруг `Selenium WebDriver`
- Библиотека модульного тестирования: `PyTest`
- `Jenkins` выполняет удаленный запуск тестов в графическом интерфейсе. Установки дополнительных приложений на компьютер пользователя не требуется.
- `Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)
- Фреймворк`Allure Report` собирает графический отчет о прохождении тестов
- После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант Allure Report

## Tests:
- [x] Отображается главная страница и основные разделы сайта (мой иви, фильмы, сериалы, мультфильмы)
- [x] Основные разделы кликабельны и по ним можно перейти
- [x] Проверка авторазации на сайте
- [x] Поиск фильма на сайте и переход в его карточку
- [x] Добавление фильма в избранное (список - "буду смотреть") и проверка в личном кабинете

### Удаленный запуск тестов (<b>Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/qa.guru_18_14/">Job</a></b>)
<details>
   <summary>Краткая инструкция</summary>

###### А: 

<i>Незарегистрированным</i> пользователем открыть готовый, ранее сформированный отчет (желтая иконка, стрелка №2 на скриншоте)
<p>Результат: откроется страница с отчетом Allure Report</p>

###### Б: 
<i>Зарегистрированным</i> пользователем: 
1. Перейти на страницу сборки проекта
2. Выбрать желаемые "Build with Parameters" в графическом интерфейсе или оставить как есть.
3. Запустить выполнение тестов кнопкой "Build"
4. Убедиться, что в блоке "Builds" появилась новая запись.
5. Дождаться окончания активного процесса (~2-3 мин)
6. Кликнуть по значку или тексту Allure Report
<p>Результат: откроется страница с отчетом Allure Report</p>

> <p>Срок хранения сборки на сервере ~60 дней. Ссылка на Job может оказаться недоступной после 28.05.2025</p>

<p>Образец:</p>

<br>![Jenkins](images/jenkins-screen.png)

</details>

## Allure: пример отчета
<details>
   <summary>Скриншоты</summary>

###### Главный экран (Owerwiev)
![Screen Allure1](images/allure-main-screen.png)
###### Страница со списком тестов (Graph)
![Screen Allure2](images/allure-graphs.png)
###### Пример описания теста
![Screen Allure3](images/allure-test-suites.png)

</details>

## Видео тестов
Видеозапись каждого теста генерируется с помощью `Selenoid`, после успешного запуска контейнера c тестами в `Docker`. 
<details>
<summary>Видеозапись</summary>
<p>Образец:</p>


![Video test](images/video%20report.mp4)
</details>

## Отчет в Telegram
После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.
Чтобы видеть его увидеть, вступите (временно) в группу `MaxNovo reports allure`


![Telegram](images/message-example.png)