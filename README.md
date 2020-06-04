# nsiEisOrganizationsToMySQL
Сбор данных из справочников организации с ftp открытой части ЕИС (https://zakupki.gov.ru/) по 44 и 223 ФЗ и запись полученных данных в таблицы MySQL, с автоматическим поиском региона организации.
### Алгоритм работы
Скрипт на python подключается к открытой части сайта ЕИС, FTP сайта https://zakupki.gov.ru/, собирает архивы из каталогов
- для 44 ФЗ  /fcs_nsi/nsiOrganization/
- для 223 ФЗ /out/nsi/nsiOrganization/

разбирает содержимое, и добавляет, или обновляет записи в таблицах MySQL. Помимо простого сбора и обновления данных, имеется возможность автоматического определения региона организации, по кодам фактического адреса КЛАДР, ОКАТО, и ОКТМО, в случае, если эти данные имеются в xml.
### Как пользоваться
Для того, чтобы воспользоваться скриптом в режиме "как есть", необходимо иметь базу данных MySQL, создать таблицы для хранения организаций по 44 и 223 ФЗ(код создания таблицы находится в каталоге MySQL и продублирован ниже). В настройках скрипта (файлы: parserSettings.py) в каталогах 
- src/ParserEisNsiOrganizations44/appmodules/
- src/ParserEisNsiOrganizations223/appmodules/

указать настройки соединения с базой данных MySQL:
```sh
  # Настройки подключения в БД
  dbHost = "your_host"
  dbUser = "your_user"
  dbPass = "your_password"
  dbBase = "your_database"
  dbPort = 3306
  dbTable = "nsi_eis_organizations_223"
  dbtbKey = "eis_guid"
# Логирование в приложении  
```
Скрипт поддерживает запуск с различными параметрами: -all, -update. Первый загружает все что есть на ftp, второй только обновления (архивы в папке daily для 223 ФЗ и архивы с отметкой _inc_ для 44 ФЗ)

### Таблица MySQL для организаций с источника 44 ФЗ
```sh
  CREATE TABLE `nsi_eis_organizations_44` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор (внутр)',
    `eis_regNumber` VARCHAR(36) NOT NULL DEFAULT '' COMMENT 'Идентификатор позиции в информационном пакете ' COLLATE 'utf8_general_ci',
    `eis_consRegistryNum` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Код по Сводному Реестру ' COLLATE 'utf8_general_ci',
    `nameShort` VARCHAR(500) NOT NULL DEFAULT '' COMMENT 'Сокращенное наименование ' COLLATE 'utf8_general_ci',
    `nameFull` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT 'Полное наименование ' COLLATE 'utf8_general_ci',
    `region` INT(11) NOT NULL COMMENT 'Регион',
    `kladrCode` VARCHAR(50) NOT NULL DEFAULT '' COMMENT 'Код КЛАДР' COLLATE 'utf8_general_ci',
    `countryFullName` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'Наименование страны' COLLATE 'utf8_general_ci',
    `inn` VARCHAR(12) NOT NULL DEFAULT '' COMMENT 'ИНН ' COLLATE 'utf8_general_ci',
    `kpp` VARCHAR(9) NOT NULL DEFAULT '' COMMENT 'КПП ' COLLATE 'utf8_general_ci',
    `registrationDate` DATETIME NOT NULL COMMENT 'Дата поставновки на учет в налоговом органе',
    `ogrn` VARCHAR(13) NOT NULL DEFAULT '' COMMENT 'ОГРН ' COLLATE 'utf8_general_ci',
    `okfs` VARCHAR(2) NOT NULL DEFAULT '' COMMENT 'Код ОКФС' COLLATE 'utf8_general_ci',
    `name_okfs` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'Наименование ОКФС' COLLATE 'utf8_general_ci',
    `okopf` VARCHAR(5) NOT NULL DEFAULT '' COMMENT 'Код ОКОПФ ' COLLATE 'utf8_general_ci',
    `name_okopf` VARCHAR(500) NOT NULL DEFAULT '' COMMENT 'Правовая форма организации' COLLATE 'utf8_general_ci',
    `okato` VARCHAR(11) NOT NULL DEFAULT '' COMMENT 'Код ОКАТО' COLLATE 'utf8_general_ci',
    `oktmo` VARCHAR(11) NOT NULL DEFAULT '' COMMENT 'Код ОКТМО' COLLATE 'utf8_general_ci',
    `okpo` VARCHAR(10) NOT NULL DEFAULT '' COMMENT 'Код ОКПО ' COLLATE 'utf8_general_ci',
    `OKVED` VARCHAR(10) NOT NULL DEFAULT '' COMMENT 'Код ОКВЕД' COLLATE 'utf8_general_ci',
    `iku` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'ИКУ' COLLATE 'utf8_general_ci',
    `dateSt_iku` DATETIME NOT NULL COMMENT 'Дата присвоения ИКУ',
    `legalAddress` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT ' Почтовый адрес ' COLLATE 'utf8_general_ci',
    `postalAddress` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT ' Почтовый адрес ' COLLATE 'utf8_general_ci',
    `org_type` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Тип организации ' COLLATE 'utf8_general_ci',
    `timeZone` VARCHAR(50) NOT NULL DEFAULT '' COMMENT 'Часовой пояс ' COLLATE 'utf8_general_ci',
    `bankAddress` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT 'Адрес банка' COLLATE 'utf8_general_ci',
    `bankName` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'Наименование банка' COLLATE 'utf8_general_ci',
    `bik` VARCHAR(9) NOT NULL DEFAULT '' COMMENT 'БИК' COLLATE 'utf8_general_ci',
    `corrAccount` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Кор/счет' COLLATE 'utf8_general_ci',
    `paymentAccount` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Р/счет' COLLATE 'utf8_general_ci',
    `personalAccount` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Л/счет' COLLATE 'utf8_general_ci',
    `contactFIO` VARCHAR(600) NOT NULL DEFAULT '' COMMENT 'ФИО контактного лица' COLLATE 'utf8_general_ci',
    `orgPhone` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Телефон ' COLLATE 'utf8_general_ci',
    `orgFax` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Факс ' COLLATE 'utf8_general_ci',
    `orgEmail` VARCHAR(50) NOT NULL DEFAULT '' COMMENT 'E-mail ' COLLATE 'utf8_general_ci',
    `orgWebsite` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'URL  источника' COLLATE 'utf8_general_ci',
    PRIMARY KEY (`id`) USING BTREE,
    INDEX `eis_regNumber` (`eis_regNumber`) USING BTREE
  )
  COMMENT='Справочник организации с сайта ЕИС по 44, 504, 615, 94 ФЗ'
  COLLATE='utf8_general_ci'
  ENGINE=InnoDB
  AUTO_INCREMENT=0;
```
### Таблица MySQL для организаций с источника 223 ФЗ
```sh
  CREATE TABLE `nsi_eis_organizations_223` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор (внутр)',
    `eis_guid` VARCHAR(36) NOT NULL DEFAULT '' COMMENT 'Идентификатор позиции в информационном пакете ' COLLATE 'utf8_general_ci',
    `eis_code` VARCHAR(20) NOT NULL DEFAULT '' COMMENT 'Индивидуальный код организации ' COLLATE 'utf8_general_ci',
    `eis_updateDate` DATETIME NOT NULL COMMENT 'Дата и время изменения данных об организации в ЕСИА',
    `nameFull` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT 'Наименование ' COLLATE 'utf8_general_ci',
    `nameShort` VARCHAR(500) NOT NULL DEFAULT '' COMMENT 'Сокращенное наименование ' COLLATE 'utf8_general_ci',
    `region` INT(11) NOT NULL COMMENT 'Регион',
    `inn` VARCHAR(12) NOT NULL DEFAULT '' COMMENT 'ИНН ' COLLATE 'utf8_general_ci',
    `kpp` VARCHAR(9) NOT NULL DEFAULT '' COMMENT 'КПП ' COLLATE 'utf8_general_ci',
    `ogrn` VARCHAR(13) NOT NULL DEFAULT '' COMMENT 'ОГРН ' COLLATE 'utf8_general_ci',
    `okfs` VARCHAR(2) NOT NULL DEFAULT '' COMMENT 'Код ОКФС' COLLATE 'utf8_general_ci',
    `okopf` VARCHAR(5) NOT NULL DEFAULT '' COMMENT 'Код ОКОПФ ' COLLATE 'utf8_general_ci',
    `okato` VARCHAR(11) NOT NULL DEFAULT '' COMMENT 'Код ОКАТО' COLLATE 'utf8_general_ci',
    `oktmo` VARCHAR(11) NOT NULL DEFAULT '' COMMENT 'Код ОКТМО' COLLATE 'utf8_general_ci',
    `okpo` VARCHAR(10) NOT NULL DEFAULT '' COMMENT 'Код ОКПО ' COLLATE 'utf8_general_ci',
    `legalAddress` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT 'Юридический адрес' COLLATE 'utf8_general_ci',
    `postalAddress` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT ' Почтовый адрес ' COLLATE 'utf8_general_ci',
    `type` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT 'Тип организации ' COLLATE 'utf8_general_ci',
    `timeZone` VARCHAR(50) NOT NULL COMMENT 'Cмещение относительно UTC' COLLATE 'utf8_general_ci',
    `contactFIO` VARCHAR(600) NOT NULL DEFAULT '' COMMENT 'ФИО контактного лица' COLLATE 'utf8_general_ci',
    `contactEmail` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'Email контактного лица' COLLATE 'utf8_general_ci',
    `orgPhone` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'Телефон ' COLLATE 'utf8_general_ci',
    `orgFax` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'Факс ' COLLATE 'utf8_general_ci',
    `orgEmail` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'Email ' COLLATE 'utf8_general_ci',
    `orgWebsite` VARCHAR(300) NOT NULL DEFAULT '' COMMENT 'URL  веб-сайта' COLLATE 'utf8_general_ci',
    PRIMARY KEY (`id`) USING BTREE,
    INDEX `eis_guid` (`eis_guid`) USING BTREE,
    INDEX `eis_code` (`eis_code`) USING BTREE,
    INDEX `eis_updateDate` (`eis_updateDate`) USING BTREE,
    INDEX `region` (`region`) USING BTREE,
    INDEX `inn` (`inn`) USING BTREE,
    INDEX `kpp` (`kpp`) USING BTREE,
    INDEX `oktmo` (`oktmo`) USING BTREE,
    INDEX `okato` (`okato`) USING BTREE
  )
  COMMENT='Справочник организации с сайта ЕИС по 223 ФЗ'
  COLLATE='utf8_general_ci'
  ENGINE=InnoDB
  AUTO_INCREMENT=0;
```
### Таблица регионы (для связи и поиска по кодам КЛАДР, ОКАТО, и ОКТМО) 
```sh
   CREATE TABLE `region` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор',
    `okrug_id` INT(11) NOT NULL COMMENT 'Идентификатор Округа',
    `name` TEXT(65535) NOT NULL COMMENT 'Наименование Региона' COLLATE 'utf8_general_ci',
    `path` VARCHAR(255) NOT NULL COMMENT 'Переменная ftp' COLLATE 'utf8_general_ci',
    `conf` VARCHAR(11) NOT NULL COLLATE 'utf8_general_ci',
    `path223` VARCHAR(100) NOT NULL COMMENT 'Переменная ftp 223' COLLATE 'utf8_general_ci',
    `time_zone` VARCHAR(10) NULL DEFAULT NULL COMMENT 'Временная зона' COLLATE 'utf8_general_ci',
    `kladr_code` VARCHAR(50) NULL DEFAULT NULL COMMENT 'Код региона КЛАДР' COLLATE 'utf8_general_ci',
    `okato_code` VARCHAR(4) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
    `oktmo_code` VARCHAR(4) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
    PRIMARY KEY (`id`) USING BTREE
  )
  COMMENT='Справочник Регионы'
  COLLATE='utf8_general_ci'
  ENGINE=MyISAM
  AUTO_INCREMENT=0;
```
Данные в таблицу можно загрузить из файла /MySQL/regions_data.sql
