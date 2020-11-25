# Проект. Проектирование базы данных

## Оглавление

   * [Тема](#тема)
   * [Выявление и определение сущностей](#выявление-и-определение-сущностей)
   * [Определение атрибутов сущностей и их типов](#определение-атрибутов-сущностей-и-их-типов)
   * [Матрица связей](#матрица-связей)
   * [Логическая модель](#логическая-модель)
   * [Реляционная модель](#реляционная-модель)

## Выбор темы. остановка задачи

## Выявление и определение сущностей

## Определение атрибутов сущностей и их типов

<img src="models/Entities/all.png">

<details>
<summary> domains </summary>

   ```dbml
enum location_domain {
    offline
    online
}

enum player_domain {
    active
    inactive
    standin
    coach
}
   ```
</details>

<details>
<summary> full code </summary>

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
     date_start date [not null]
     date_end date [not null]
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
     id int [pk, increment]
     type location_domain [not null]
     region_id int [null]
     country_id int [null]
     city int [null]
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
     maps_count integer [not null]
     rounds_count integer [not null]
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
     region_id integer [null]
     country_id integer [null]
}

Table PLAYERS {
    id integer [pk, increment]
     nickname varchar(255) [not null]
     type player_domain [not null]
     first_name varchar(255) [null]
     last_name varchar(255) [null]
     birthdate date [null]
     country_id integer [null]
     team_id integer [null]
}

Table ACHIEVEMENTS {
    id integer [pk, increment]
     name varchar(255) [not null]
}

Table COUNTRIES {
     id integer [pk, increment]
     name varchar(255) [not null]
     region_id integer [null]
}

Table REGIONS {
     id integer [pk, increment]
     name varchar(255) [unique, not null]
}

enum location_domain {
     offline
     online
}

enum player_domain {
    active
     inactive
     standin
     coach
}
   ```
</details>

## Матрица связей

|   | Achievement | Article comment | Article | Event | Location | Map | Match comment | Match type | Match | Player | Role | Sponsor | Team | User |
| ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Achievement** |  |  |  |  |  |  |  |  |  | принадлежит |  |  | принадлежит |  |
| **Article comment** |  | ответ на | относится к |  |  |  |  |  |  |  |  |  |  | написан |
| **Article** |  | содержит |  | относится к |  |  |  |  |  |  |  |  |  | написана |
| **Event** |  |  | упоминается в |  | проводится в |  |  |  | включает в себя |  |  | проводится | проводится для |  |
| **Location** |  |  |  | место проведения для |  |  |  |  |  |  |  |  |  |  |
| **Map** |  |  |  |  |  |  |  |  | играется в |  |  |  |  |  |
| **Match comment** |  |  |  |  |  |  | ответ на |  | относится к |  |  |  |  | написан |
| **Match type** |  |  |  |  |  |  |  |  | описывает |  |  |  |  |  |
| **Match** |  |  |  | принадлежит |  | играется на | содержит | проводится в формате |  |  |  |  | участвует |  |
| **Player** | имеет |  |  |  |  |  |  |  |  |  |  |  | состоит в | фаворит для |
| **Role** |  |  |  |  |  |  |  |  |  |  |  |  |  | описывает |
| **Sponsor** |  |  |  | проводит |  |  |  |  |  |  |  |  |  |  |
| **Team** | имеет |  |  | приглашена на |  |  |  |  | участвует в | содержит |  |  |  | фаворит для |
| **User** |  | написал | написал |  |  |  | написал |  |  | выбрал | имеет |  | выбрал |  |

## Логическая модель

## Реляционная модель

TODO
