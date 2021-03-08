insert into REGIONS (NAME, ICON) values ('Europe', 'images/icons/regions/europe.png');
insert into REGIONS (NAME, ICON) values ('China', 'images/icons/regions/china.png');
insert into REGIONS (NAME, ICON) values ('Southeast Asia', 'images/icons/regions/southeast_asia.png');
insert into REGIONS (NAME, ICON) values ('CIS', 'images/icons/regions/cis.png');
insert into REGIONS (NAME, ICON) values ('North America', 'images/icons/regions/north_america.png');
insert into REGIONS (NAME, ICON) values ('South America', 'images/icons/regions/south_america.png');

insert into COUNTRIES (REGION_ID, NAME, ICON) values (1, 'Denmark', 'images/icons/countries/denmark.png');
insert into COUNTRIES (REGION_ID, NAME, ICON) values (1, 'Russia', 'images/icons/countries/russia.png');
insert into COUNTRIES (REGION_ID, NAME, ICON) values (1, 'Ukraine', 'images/icons/countries/ukraine.png');
insert into COUNTRIES (REGION_ID, NAME, ICON) values (1, 'France', 'images/icons/countries/france.png');
insert into COUNTRIES (REGION_ID, NAME, ICON) values (1, 'Germany', 'images/icons/countries/germany.png');
insert into COUNTRIES (REGION_ID, NAME, ICON) values (5, 'United States', 'images/icons/countries/united_states.png');
insert into COUNTRIES (REGION_ID, NAME, ICON) values (6, 'Brazil', 'images/icons/countries/brazil.png');
insert into COUNTRIES (REGION_ID, NAME, ICON) values (5, 'Canada', 'images/icons/countries/canada.png');

insert into PLAYER_STATUSES (NAME) values ('major player');
insert into PLAYER_STATUSES (NAME) values ('spare player');
insert into PLAYER_STATUSES (NAME) values ('replacement player');
insert into PLAYER_STATUSES (NAME) values ('inactive player');
insert into PLAYER_STATUSES (NAME) values ('coach');

insert into ROLES (NAME) values ('user');
insert into ROLES (NAME) values ('author');
insert into ROLES (NAME) values ('clip-maker');
insert into ROLES (NAME) values ('moderator');
insert into ROLES (NAME) values ('admin');

insert into MAPS (NAME, ICON) values ('Dust2', 'images/icons/maps/dust2.png');
insert into MAPS (NAME, ICON) values ('Mirage', 'images/icons/maps/mirage.png');
insert into MAPS (NAME, ICON) values ('Inferno', 'images/icons/maps/inferno.png');
insert into MAPS (NAME, ICON) values ('Nuke', 'images/icons/maps/nuke.png');
insert into MAPS (NAME, ICON) values ('Train', 'images/icons/maps/train.png');
insert into MAPS (NAME, ICON) values ('Overpass', 'images/icons/maps/overpass.png');
insert into MAPS (NAME, ICON) values ('Vertigo', 'images/icons/maps/vertigo.png');

insert into MATCH_TYPES (NUMBER_MAPS, NUMBER_ROUNDS) values (1, 16);
insert into MATCH_TYPES (NUMBER_MAPS, NUMBER_ROUNDS) values (2, 16);
insert into MATCH_TYPES (NUMBER_MAPS, NUMBER_ROUNDS) values (3, 16);
insert into MATCH_TYPES (NUMBER_MAPS, NUMBER_ROUNDS) values (5, 16);

insert into SPONSORS (NAME, LINK) values ('ESL', 'https://www.links.urls/esl');
insert into SPONSORS (NAME, LINK) values ('BLAST', 'https://www.links.urls/blast');
insert into SPONSORS (NAME, LINK) values ('DreamHack', 'https://www.links.urls/dream_hack');

insert into LOCATIONS (NAME, REGION_ID) values ('online', 1);
insert into LOCATIONS (NAME, REGION_ID) values ('online', 5);

insert into TEAMS (NAME, POINTS, PEAK, ICON) values ('Astralis', 904, 1, 'images/icons/astralis.png');
insert into TEAMS (NAME, POINTS, PEAK, ICON) values ('Natus Vincere', 849, 1, 'images/icons/na_vi.png');
insert into TEAMS (NAME, POINTS, PEAK, ICON) values ('Vitality', 565, 1, 'images/icons/vitality.png');
insert into TEAMS (NAME, POINTS, PEAK, ICON) values ('BIG', 536, 2, 'images/icons/big.png');
insert into TEAMS (NAME, POINTS, PEAK, ICON) values ('Liquid', 446, 1, 'images/icons/liquid.png');


insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('Xyp9x', 'Andreas', 'Hojsleth', 'images/photos/players/xyp9x.jpg', 1);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('dupreeh', 'Peter', 'Rasmussen', 'images/photos/players/dupreeh.jpg', 1);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('gla1ve', 'Lukas', 'Rossander', 'images/photos/players/gla1ve.jpg', 1);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('device', 'Nicolai', 'Reedtz', 'images/photos/players/device.jpg', 1);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('Magisk', 'Emil', 'Reif', 'images/photos/players/magisk.jpg', 1);

insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('FalleN', 'Gabriel', 'Toledo', 'images/photos/players/fallen.jpg', 7);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('NAF', 'Keith', 'Markovic', 'images/photos/players/naf.jpg', 8);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('EliGE', 'Jonathan', 'Jablonowski', 'images/photos/players/elige.jpg', 6);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('Stewie2K', 'Jake', 'Yip', 'images/photos/players/stewie2k.jpg', 6);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('Grim', 'Michael', 'Wince', 'images/photos/players/grim.jpg', 6);

insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('flamie', 'Egor', 'Vasilyev', 'images/photos/players/flamie.jpg', 2);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('s1mple', 'Aleksandr', 'Kostyliev', 'images/photos/players/s1mple.jpg', 3);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('electronic', 'Denis', 'Sharipov', 'images/photos/players/electronic.jpg', 2);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('Boombl4', 'Kirill', 'Mikhailov', 'images/photos/players/boombl4.jpg', 2);
insert into PLAYERS
    (NICKNAME, FIRST_NAME, LAST_NAME, PHOTO, COUNTRY_ID)
    values ('Perfecto', 'Ilya', 'Zalutskiy', 'images/photos/players/perfecto.jpg', 2);

insert into USERS (USERNAME, PASSWORD, EMAIL, ROLE_ID, PLAYER_ID) values ('admin', 'admin', 'admin@gmail.com', 5, 7);
insert into USERS (USERNAME, PASSWORD, EMAIL, ROLE_ID, TEAM_ID) values ('author', 'author', 'author@gmail.com', 2, 3);
insert into USERS (USERNAME, PASSWORD, EMAIL, ROLE_ID, PLAYER_ID) values ('user', 'user', 'user@gmail.com', 1, 1);

insert into EVENTS
    (NAME, SPONSOR_ID, START_DATE, END_DATE, LOCATION_ID, PRIZE_POOL, NUMBER_TEAMS)
    values ('ESL Pro League Season 13', 1, TO_DATE('08.03.2021', 'DD.MM.YYYY'),
            TO_DATE('11.04.2021', 'DD.MM.YYYY'), 2, '750000', 24);
