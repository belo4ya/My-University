# Проект. Проектирование базы данных

## Оглавление

   * [Выбор темы. Постановка задачи](#выбор-темы-постановка-задачи)
   * [Выявление и определение сущностей](#выявление-и-определение-сущностей)
   * [Определение атрибутов сущностей и их типов](#определение-атрибутов-сущностей-и-их-типов)
   * [Матрица связей](#матрица-связей)
   * [Логическая модель](#логическая-модель)
   * [Реляционная модель](#реляционная-модель)

## Выбор темы. Постановка задачи

Разработка модели данных для системы управления базы данных новостного сайта и форума [**hltv.org**](https://www.hltv.org/).

База данных должна способствовать реализации следующего функционала:

- Пользователи с особым **статусом** могут создавать **статьи** и публиковать **новости**. Другой статус разрешает пользователям публиковать короткие highlight-ролики. Также есть администраторы и модераторы форума, которые могут редактировать контент, удалять его или скрывать, блокировать пользователей и удалять комментарии.
- Каждый **авторизованный пользователь** имеет **уникальный nickname**; в настройках профиля может указать **страну**, выбрать **любимого игрока** **или** (но не одновременно) **любимую команду**, которые будут отображаться рядом с его nickname'ом.
- Любые авторизованные пользователи могут **комментировать** **новости**, **статьи** и **предстоящие матчи**, а также **отвечать** на комментарии других пользователей.
- На сайте представлена информация о грядущих **турнирах**, а именно: **название** турнира; **даты** начала и конца проведения турнира; **организатор** турнира, **призовой фонд** (может выражаться как в денежном эквиваленте так и приглашением на следующую стадию турнира); **место проведения** - в зависимости от **формата** турнира (offline или online) местом может быть либо **страна и город**, либо просто название **региона**; **количество команд**-участников, при этом некоторые команды могут быть не определены.
- На сайте представлена информация о предстоящих матчах, а именно: **дата и время начала** встречи; **две команды**, при этом они могут быть ещё не определены; **формат** матча (bo1, bo2, ...); ближе к началу матча становятся известны названия **карт**, на которых пройдет встреча; ссылка на доступную **трансляцию**. Каждый **матч проходит в рамках** какого-либо **турнира**.
- На сайте представлена информация о **командах** и **игроках**.
- В команде может числиться **любое количество игроков**, но участвовать в матче могут только пятеро. Игроки могут иметь разные **статусы**, такие как игрок-замена, неактивный игрок, иногда в матчах игрока может заменить тренер команды.
- За победы на турнирах и другие заслуги команды и игроки могут получать **достижения** (команды также получают очки). При этом достижение полученное командой, закрепляется и за командой, и за игроком.

## Выявление и определение сущностей

Исходя из условия задачи я выделил следующие сущности:

- **user** - зарегистрированный/авторизованный пользователь сайта.
- **role** - статус пользователя, определяющий его возможности.
- **article** - опубликованная статья или новость.
- **article comment** - комментарий оставленный к статье или ответ на этот комментарий.
- **event** - информация о предстоящем турнире.
- **sponsor** - информация об организаторе турнира.
- **location** - место проведения турнира в зависимости от его типа.
- **match** - информация о предстоящем матче.
- **match type** - информация о формате проведения турнира, кол-ве карт и раундов.
- **map** - информация о картах официального маппула.
- **score** - информация о счете игры на конкретной карте.
- **match comment** - комментарий оставленный к матчу или ответ на этот комментарий.
- **team** - информация о киберспортивной комманде.
- **player** - информация об игроке.
- **player team** - информация о дате пребывания игрока в конкретной комманде.
- **player status** - информация о статусе игрока в конкретный момент времени.
- **achievement** - достижение, которое может получить комманды или игрок.
- **country** - вспомогательная таблица с названиями стран и иконками их флагов.
- **region** - вспомогательная таблица с названиями регионов.

## Определение атрибутов сущностей и их типов

<img src="models/Entities/all.png" height="600">

<details>
<summary> domains </summary>

   ```dbml
enum location_d {
    offline
    online
}

enum player_status_d {
    active
    inactive
    standin
    coach
}
   ```
</details>

<details>
<summary> dbml </summary>

   ```dbml
Table USERS {
    id integer [pk, increment]
    username varchar(255) [unique, not null]
    password varchar(255) [not null]
    email varchar(255) [not null]
    birthdate date [null]
    country_id integer [null]
    role_id integer [not null]
    player_id integer [null, note: 'favorite player']
    team_id integer [null, note: 'or favorite team']
}

Table ROLES {
    id integer [pk, increment]
    name varchar(255) [unique, not null]
}

Table ARTICLES {
    id integer [pk, increment]
    title varchar(255) [not null]
    content text(10000) [not null]
    date date [not null]
    author_id integer [not null]
    event_id integer [null]
}

Table ARTICLE_COMMENTS {
    id integer [pk, increment]
    text varchar(500) [not null]
    date date [not null]
    article_id integer [not null]
    user_id integer [not null]
    parent_id integer [null]
}

Table MATCH_COMMENTS {
    id integer [pk, increment]
    text varchar(500) [not null]
    date date [not null]
    match_id integer [not null]
    user_id integer [not null]
    parent_id integer [null]
}

Table EVENTS {
    id integer [pk, increment]
    name varchar(255) [not null]
    start_date date [not null]
    end_date date [not null]
    prize_pool varchar(255) [not null]
    total_teams integer [not null]
    logo varchar(255) [null]
    location_id integer [not null]
    sponsor_id integer [not null]
}

Table SPONSORS {
    id integer [pk, increment]
    name varchar(255) [not null]
    link varchar(255) [null]
}

Table LOCATIONS {
    id integer [pk, increment]
    type location_d [not null]
    region_id integer [null]
    country_id integer [null]
    city varchar(255) [null]
}

Table MATCHES {
    id integer [pk, increment]
    date date [not null]
    watch varchar(255) [null]
    description varchar(500) [null]
    format_id integer [not null]
    event_id integer [not null]
    team_id1 integer [null]
    team_id2 integer [null]
}

Table MATCH_TYPES {
    id integer [pk, increment]
    maps_cnt integer [not null]
    rounds_cnt integer [not null]
}

Table SCORES {
    match_id integer [pk]
    map_id integer [pk]
    first_hf integer [null]
    second_hf integer [null]
    overtime integer [null]
}

Table MAPS {
    id integer [pk, increment]
    name varchar(255) [unique, not null]
    image varchar(255) [not null]
}

Table TEAMS {
    id integer [pk, increment]
    name varchar(255) [not null]
    logo varchar(255) [null]
    points integer [not null]
    peak integer [not null]
}

Table PLAYERS {
    id integer [pk, increment]
    nickname varchar(255) [not null]
    photo varchar(255) [null]
    first_name varchar(255) [null]
    last_name varchar(255) [null]
    birthdate date [null]
    country_id integer [null]
}

Table PLAYERS_TEAMS {
    player_id integer [pk]
    team_id integer [pk]
    start_date date [not null]
    end_date date [null]
}

Table PLAYERS_STATUSES {
    player_id integer [pk]
    date date [pk]
    status player_status_d [not null]
}

Table ACHIEVEMENTS {
    id integer [pk, increment]
    name varchar(255) [unique, not null]
}

Table COUNTRIES {
    id integer [pk, increment]
    name varchar(255) [not null]
    region_id integer [null]
    icon varchar(255) [not null]
}

Table REGIONS {
    id integer [pk, increment]
    name varchar(255) [unique, not null]
    icon varchar(255) [not null]
}

enum location_d {
    offline
    online
}

enum player_status_d {
    active
    inactive
    standin
    coach
}
   ```
</details>

## Матрица связей

|   | Achievement | Article comment | Article | Country | Event | Location | Map | Match comment | Match type | Match | Player status | Player team | Player | Region | Role | Score | Sponsor | Team | User |
| ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Achievement** |  |  |  |  |  |  |  |  |  |  |  |  | принадлежит |  |  |  |  | принадлежит |  |
| **Article comment** |  | ответ на | относится к |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | написан |
| **Article** |  | содержит |  |  | относится к |  |  |  |  |  |  |  |  |  |  |  |  |  |  | написана |
| **Country** |  |  |  |  |  | характеризует |  |  |  |  |  |  | характеризует | входит в |  |  |  |  | характеризует |
| **Event** | 1 | 2 | упоминается в | 4 | 5 | проводится в | 7 | 8 | 9 | включает в себя | 11 | 12 | 13 | 14 | 15 | 16 | проводится | проводится для | 19 |
| **Location** | 1 | 2 | 3 | характеризуется | место проведения для | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | характеризуется | 15 | 16 | 17 | 18 | 19 |
| **Map** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | характеризуется | 17 | 18 | 19 |
| **Match comment** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ответ на | 9 | относится к | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | написан |
| **Match type** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | характеризует | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| **Match** | 1 | 2 | 3 | 4 | принадлежит | 6 | играется на | содержит | характеризуется | 10 | 11 | 12 | 13 | 14 | 15 | характеризуется | 17 | проводится между | 19 |
| **Player status** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | характеризует | 14 | 15 | 16 | 17 | 18 | 19 |
| **Player team** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | характеризует | характеризует | 14 | 15 | 16 | 17 | 18 | 19 |
| **Player** | имеет | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | характеризуется | характеризуется | 13 | 14 | 15 | 16 | 17 | состоит в | фаворит для |
| **Region** | 1 | 2 | 3 | содержит | 5 | характеризует | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| **Role** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | характеризует |
| **Score** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| **Sponsor** | 1 | 2 | 3 | 4 | проводит | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| **Team** | имеет | 2 | 3 | 4 | участвует в | 6 | 7 | 8 | 9 | участвует в | 11 | характеризуется | содержит | 14 | 15 | характеризуется | 17 | 18 | фаворит для |
| **User** | 1 | написал | написал | 4 | 5 | 6 | 7 | написал | 9 | 10 | 11 | 12 | выбрал | 14 | характеризуется | 16 | 17 | выбрал | 19 |

## Логическая модель

<img src="models/Logical/Logical.png" height="600">

## Реляционная модель

TODO
