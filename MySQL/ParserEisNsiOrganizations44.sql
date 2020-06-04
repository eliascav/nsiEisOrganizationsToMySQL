CREATE TABLE IF NOT EXISTS `nsi_eis_organizations_44` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор (внутр)',
  `eis_regNumber` varchar(36) NOT NULL DEFAULT '' COMMENT 'Идентификатор позиции в информационном пакете ',
  `eis_consRegistryNum` varchar(20) NOT NULL DEFAULT '' COMMENT 'Код по Сводному Реестру ',
  `nameShort` varchar(500) NOT NULL DEFAULT '' COMMENT 'Сокращенное наименование ',
  `nameFull` varchar(1000) NOT NULL DEFAULT '' COMMENT 'Полное наименование ',
  `region` int(11) NOT NULL COMMENT 'Регион',
  `kladrCode` varchar(50) NOT NULL DEFAULT '' COMMENT 'Код КЛАДР',
  `countryFullName` varchar(300) NOT NULL DEFAULT '' COMMENT 'Наименование страны',
  `inn` varchar(12) NOT NULL DEFAULT '' COMMENT 'ИНН ',
  `kpp` varchar(9) NOT NULL DEFAULT '' COMMENT 'КПП ',
  `registrationDate` datetime NOT NULL COMMENT 'Дата поставновки на учет в налоговом органе',
  `ogrn` varchar(13) NOT NULL DEFAULT '' COMMENT 'ОГРН ',
  `okfs` varchar(2) NOT NULL DEFAULT '' COMMENT 'Код ОКФС',
  `name_okfs` varchar(300) NOT NULL DEFAULT '' COMMENT 'Наименование ОКФС',
  `okopf` varchar(5) NOT NULL DEFAULT '' COMMENT 'Код ОКОПФ ',
  `name_okopf` varchar(500) NOT NULL DEFAULT '' COMMENT 'Правовая форма организации',
  `okato` varchar(11) NOT NULL DEFAULT '' COMMENT 'Код ОКАТО',
  `oktmo` varchar(11) NOT NULL DEFAULT '' COMMENT 'Код ОКТМО',
  `okpo` varchar(10) NOT NULL DEFAULT '' COMMENT 'Код ОКПО ',
  `OKVED` varchar(10) NOT NULL DEFAULT '' COMMENT 'Код ОКВЕД',
  `iku` varchar(20) NOT NULL DEFAULT '' COMMENT 'ИКУ',
  `dateSt_iku` datetime NOT NULL COMMENT 'Дата присвоения ИКУ',
  `legalAddress` varchar(2000) NOT NULL DEFAULT '' COMMENT ' Почтовый адрес ',
  `postalAddress` varchar(2000) NOT NULL DEFAULT '' COMMENT ' Почтовый адрес ',
  `org_type` varchar(20) NOT NULL DEFAULT '' COMMENT 'Тип организации ',
  `timeZone` varchar(50) NOT NULL DEFAULT '' COMMENT 'Часовой пояс ',
  `bankAddress` varchar(2000) NOT NULL DEFAULT '' COMMENT 'Адрес банка',
  `bankName` varchar(300) NOT NULL DEFAULT '' COMMENT 'Наименование банка',
  `bik` varchar(9) NOT NULL DEFAULT '' COMMENT 'БИК',
  `corrAccount` varchar(20) NOT NULL DEFAULT '' COMMENT 'Кор/счет',
  `paymentAccount` varchar(20) NOT NULL DEFAULT '' COMMENT 'Р/счет',
  `personalAccount` varchar(20) NOT NULL DEFAULT '' COMMENT 'Л/счет',
  `contactFIO` varchar(600) NOT NULL DEFAULT '' COMMENT 'ФИО контактного лица',
  `orgPhone` varchar(20) NOT NULL DEFAULT '' COMMENT 'Телефон ',
  `orgFax` varchar(20) NOT NULL DEFAULT '' COMMENT 'Факс ',
  `orgEmail` varchar(50) NOT NULL DEFAULT '' COMMENT 'E-mail ',
  `orgWebsite` varchar(300) NOT NULL DEFAULT '' COMMENT 'URL  источника',
  PRIMARY KEY (`id`),
  KEY `eis_regNumber` (`eis_regNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Справочник организации с сайта ЕИС по 44, 504, 615, 94 ФЗ';
