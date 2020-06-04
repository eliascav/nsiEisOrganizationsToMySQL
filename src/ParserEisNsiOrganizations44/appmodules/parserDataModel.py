from appmodules import parserDataModelProvider as parserDMP
from appmodules import parserSettings as cfg
from appmodules import parserDatabase as db


class parserDataModel:
    data = list()
    dataModel = {
        "eis_regNumber": "",
        "eis_consRegistryNum": "",
        "nameFull": "",
        "nameShort": "",
        "region": 0,
        "kladrCode": "",
        "countryFullName": "",
        "inn": "",
        "kpp": "",
        "registrationDate": "",
        "ogrn": "",
        "okfs": "",
        "name_okfs": "",
        "okopf": "",
        "name_okopf": "",
        "okato": "",
        "oktmo": "",
        "okpo": "",
        "OKVED": "",
        "iku": "",
        "dateSt_iku": "",
        "legalAddress": "",
        "postalAddress": "",
        "org_type": "",
        "timeZone": "",
        "bankAddress": "",
        "bankName": "",
        "bik": "",
        "corrAccount": "",
        "paymentAccount": "",
        "personalAccount": "",
        "contactFIO": "",
        "orgPhone": "",
        "orgFax": "",
        "orgEmail": "",
        "orgWebsite": ""
    }

    def __init__(self, xmlFile):
        self.data = parserDMP.prepareDataModelFromFile(xmlFile, self.dataModel)

    def exportToDataBase(self):
        con = db.database().connector()
        for dataItem in self.data:
            exportItemToDataBase(dataItem, con)


def exportItemToDataBase(dataItem, con):
    # проверка на существование
    itemExist = dbItemExist(dataItem[cfg.dbtbKey], con)
    if itemExist:  # Формирование запроса
        upDataItem = dict(dataItem)
        del upDataItem[cfg.dbtbKey]  # Удаляем колонку идекса
        dbValHolder = " = %s, ".join(upDataItem.keys())
        dbValHolder += " = %s"
        query = "UPDATE `{}` SET {} WHERE `{}` = '{}';".format(
            cfg.dbTable,
            dbValHolder,
            cfg.dbtbKey,
            dataItem[cfg.dbtbKey])
        with con:
            cur = con.cursor()
            cur.execute(query, prepareValues(list(upDataItem.values())))
    else:
        dbTables = ", ".join(dataItem.keys())
        dbValHolder = "%s," * len(dataItem.keys())
        dbValHolder = dbValHolder[0:-1]
        query = "INSERT INTO `{}` ({}) VALUES ({});".format(cfg.dbTable, dbTables, dbValHolder)
        with con:
            cur = con.cursor()
            cur.execute(query, prepareValues(list(dataItem.values())))
    if itemExist:
        cfg.parserUpd += 1
    else:
        cfg.parserAdd += 1


def dbItemExist(dbtbKey, con):
    query = "SELECT `tb`.`id` FROM {} as tb WHERE tb.{} = %s".format(cfg.dbTable, cfg.dbtbKey)
    with con:
        cur = con.cursor()
        cur.execute(query, (str(dbtbKey)))
        dbResponse = cur.fetchall()
    if len(dbResponse) == 0:
        return False
    else:
        return True


def prepareValues(ValuesList):
    for i in range(len(ValuesList)):
        if ValuesList[i] == "None":
            ValuesList[i] = ""
    return ValuesList
