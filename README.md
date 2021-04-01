Тестовое задание для Фабрики решений
====================================
-----------------------------------
### Деплой приложения
Сначала нужно клонировать репозиторий с GitHub
```git
git clone https://github.com/AbndreyMichaylov/test
```
Затем нужно открыть папку проекта, активировать среду, после активации перейти в папку проекта и запустить его локально
```bash
cd env/scripts
activate
cd ..
cd ..
cd test2
manage.py runserver
```
Локальный адрес выглядит так
```
http://127.0.0.1:8000/
```
----------------------------
### Админ панель
Адрес админ панели выглядит так
```
http://127.0.0.1:8000/admin
```
Логин и пароль от админ панели
```
login : andrey
password : andrey
```
Админ панель выглядит следующим образом

![image](https://user-images.githubusercontent.com/48345409/113225076-74a9ce80-9295-11eb-8f9a-0031d9eafe57.png)

Схема базы данных

![cheema](https://user-images.githubusercontent.com/48345409/113225901-80969000-9297-11eb-9ff5-2bd06d8f88be.png)

Возможности админ панели:
1. Добавление/изменение/удаление любых данных.
----------------------------
### Работа с системой
В система изначально присутсвует 2 пользователя, kirill, dmitriy, их данные представленны ниже:
```
kirill
login : kirill
password : EVQJdsEJyvzM
dmitriy
login : dmitriy
password : OQG61{6V1ice
```
Взаимодействие с api проходит по следующему алгоритму:
1. Получение токена
2. Получение списка опросов
3. Прохождение опроса
4. Получение списка пройденных опросов

### 1. Получение токена
Что бы получить токен нужно отправить POST запрос следующему адресу:
```
http://127.0.0.1:8000/api/v1/auth/token/login
```
В теле запроса передать следующий json(пример будет на пользователе dmitriy):
```json
{
  "password" : "OQG61{6V1ice",
  "username" : "dmitriy"
}
```
В ответ придет следующий json:
```json
{
    "auth_token": "ef09348ec16055328fcb5db70cb84079f03d6585"
}
```
`!!!Данный токен требуется сохранить и отправлять в заголовке каждого запроса!!!`, формат передачи показан ниже:
```json
"Authorization" : "Token ef09348ec16055328fcb5db70cb84079f03d6585"
```
### 2. Получение списка опросов
Для получения опросов нужно отправить GET запрос по следующему адресу:
```
http://127.0.0.1:8000/api/v1/survey/all
```
В ответ придет следующий json:
```json
[
    {
        "id": 11,
        "questions": [
            "Как вас зовут?",
            "Как ваши дела?",
            "Сколько вам лет?"
        ],
        "name": "Общий опросик",
        "date_start": "2021-03-31T20:45:16Z",
        "date_end": null,
        "desc": "Опрос"
    },
    {
        "id": 41,
        "questions": [
            "Куда поедете летом?"
        ],
        "name": "Куда вы поедете летом?",
        "date_start": "2021-03-31T22:38:27Z",
        "date_end": null,
        "desc": "Опрос про море"
    }
]
```
Из полученного json требуется запомнить id опроса и сами вопросы.
### 3. Прохождение опроса
Для прохождения опроса нужно отправить POST запрос по следующему адресу:
```
http://127.0.0.1:8000/api/v1/survey/start/
```
В теле передать следующий json, где answer - это ответы(строка), а survey - опрос(идентификатор опроса полученный выше, целое число)
```json
{
  "answer" : "На море",
  "survey" : 41
}
```
Если опрос с указанным идентификатором существует, в ответ придет следующее сообщение и ответы сохраняться:
```json
{"ok":"\"ok\""}
```
### 4.Получение списка пройденных опросов
Для получения списка пройденных опросов требуется отправить GET запрос следующему адресу:
```
http://127.0.0.1:8000/api/v1/surveys/ended/all
```
В ответ придет конструкция имеющая следующий вид:
```json
{
    "surveys": [
        {
            "id": 1,
            "survey": 39,
            "answer": "Dima"
        },
        {
            "id": 2,
            "survey": 40,
            "answer": "Dima"
        },
        {
            "id": 3,
            "survey": 42,
            "answer": "На море"
        }
    ]
}
```
----------------------------
### Резюмирование проделанного задания
#### Были достигнуты следующий цели:
1. авторизация в системе (регистрация не нужна)
2. добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
3. добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)
4. получение списка активных опросов
5. прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
6. получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Однако некоторые моменты были все таки не решены, они представленны ниже:
1. Изменение типа вопроса ни к чем не приводит. По началу я не понимал как это сделать, но под самый конец я придумал способ это реализовать при помощи NoSQL бд по типу MongoDB, скорее всего пришлось бы делать все почти с самого нуля, к тому же я уже просрочил сдачу т.к. сам говорил что сдам в этот же день, потому я оставил данный вариант от реализации.
----------------------------------
#### Детали работы
При открытии таблиц Surveys и StartedSurveys будет примерно такая картина:

![image](https://user-images.githubusercontent.com/48345409/113227047-51355280-929a-11eb-98ed-fefd1a8c39a2.png)

А именно опросы именуются как "название | bool", все дело в том чтона прохождение каждого, даже одного и того же опроса создается копия опроса с полем copy равным False, данная системма была встроенна по той причине что человек может ответить на вопрос разными вариантами, и тогда придется изменять уже существующий ответ, плюс из за связей придобалении ответа, статус опроса изменяется на "Пройден", а это означает что этот же опрос придет другому человеку с тем же статусом, это неправильное поведение и оно было решено таким, не самым правильным и эффективным образом. Затем я добввил промежуточную таблицу EndedSurveys что бы все пройденные опросы записывались туда, однако то происходит не так как я ожидал и в итоге таблица копируется в Survey, для этого я добавил фильтр в админ панель, в котором можно убрать все записи что были скопированы, а в api при запросе всех опросов приходит ответ только с опросами False в свойстве copied, таким образом для просмотра всех "базовых" опросов в админ панели нужно отфильтровать записи по полю copied в false.
Справа Filter -> By Копировано -> No

![image](https://user-images.githubusercontent.com/48345409/113227561-9efe8a80-929b-11eb-9101-b11e570a454f.png)

------------------------------------------------
`Большое спасибо вам за задание, 
оно показалось мне очень интересным!`
=================================================================
