from appmodules import parserSettings as cfg
import xmltodict
import traceback


def prepareDataModelFromFile(xmlFile, dataModel):
    exportData = list()
    with open(xmlFile) as dataFile:
        try:
            firstString = dataFile.read()
            dataFromFile = xmltodict.parse(firstString)
            xmlOrganizations = dataFromFile['ns2:nsiOrganization']['ns2:body']['ns2:item']
        except Exception as ex:
            cfg.appLogger.write("При разборе файла {} произошла ошибка: {}".format(xmlFile, str(ex)))
            return list()
        for xmlOrganization in xmlOrganizations:
            try:
                dataItem = getDataItemByDataModel(xmlOrganization, dataModel)
            except Exception as ex:
                cfg.appLogger.write("При парсинге: {} {} ошибка: {}".format(
                    xmlOrganization.get('oos:fullName'), xmlFile, str(ex)))
                cfg.appLogger.write("{}".format(traceback.format_exc()))
            exportData.append(dict(dataItem))
        return exportData


def getDataItemByDataModel(xmlOrganization, dataModel):
    xmlOrgData = xmlOrganization['ns2:nsiOrganizationData']  # Оставляю прявое обращение, необходимо явное исключение
    dataModel["eis_guid"] = str(xmlOrgData.get('ns2:guid'))
    dataModel["eis_code"] = str(xmlOrgData.get('ns2:code'))
    dataModel["eis_updateDate"] = str(xmlOrgData.get('ns2:changeESIADateTime'))
    # Данные из пакета mainInfo
    if xmlOrgData.get('ns2:mainInfo') is not None:
        xmlOrgDataMain = xmlOrgData.get('ns2:mainInfo')
        dataModel["nameFull"] = str(xmlOrgDataMain.get('fullName'))
        dataModel["nameShort"] = str(xmlOrgDataMain.get('shortName'))
        dataModel["inn"] = str(xmlOrgDataMain.get('inn'))
        dataModel["kpp"] = str(xmlOrgDataMain.get('kpp'))
        dataModel["ogrn"] = str(xmlOrgDataMain.get('ogrn'))
        dataModel["legalAddress"] = str(xmlOrgDataMain.get('legalAddress'))
        dataModel["postalAddress"] = str(xmlOrgDataMain.get('postalAddress'))
    # Данные из пакета classification
    if xmlOrgData.get('ns2:classification') is not None:
        xmlOrgDataClass = xmlOrgData['ns2:classification']
        dataModel["okfs"] = str(xmlOrgDataClass.get('ns2:okfs'))
        dataModel["okopf"] = str(xmlOrgDataClass.get('ns2:okopf'))
        dataModel["okato"] = str(xmlOrgDataClass.get('ns2:okato'))
        dataModel["oktmo"] = str(xmlOrgDataClass.get('ns2:oktmo'))
        dataModel["okpo"] = str(xmlOrgDataClass.get('ns2:okpo'))
        if xmlOrgDataClass.get('ns2:fz223types') is not None:
            if type(xmlOrgDataClass.get('ns2:fz223types').get('ns2:fz223type')) == list:
                dataModel["type"] = str(xmlOrgDataClass['ns2:fz223types'].get('ns2:fz223type')[0].get('ns2:name'))
            else:
                dataModel["type"] = str(xmlOrgDataClass['ns2:fz223types'].get('ns2:fz223type').get('ns2:name'))
        if xmlOrgDataClass.get('ns2:additionalInfo') is not None:
            if type(xmlOrgData.get('ns2:additionalInfo').get('ns2:timeZone')) == list:
                dataModel["timeZone"] = str(
                    xmlOrgData.get('ns2:additionalInfo').get('ns2:timeZone')[0].get('ns2:offset'))
            else:
                dataModel["timeZone"] = str(
                    xmlOrgData.get('ns2:additionalInfo').get('ns2:timeZone').get('ns2:offset'))
    # Данные из пакета contactInfo
    if xmlOrgData.get('ns2:contactInfo') is not None:
        xmlOrgDataContact = xmlOrgData['ns2:contactInfo']
        dataModel["contactFIO"] = "{} {} {}".format(
            xmlOrgDataContact.get('ns2:contactLastName'),
            xmlOrgDataContact.get('ns2:contactFirstName'),
            xmlOrgDataContact.get('ns2:contactMiddleName'))
        dataModel["contactEmail"] = str(xmlOrgData.get('ns2:email'))
        dataModel["orgPhone"] = str(xmlOrgData.get('ns2:phone'))
        dataModel["orgFax"] = str(xmlOrgData.get('ns2:fax'))
        dataModel["orgEmail"] = str(xmlOrgData.get('ns2:email'))
        dataModel["orgWebsite"] = str(xmlOrgData.get('ns2:website'))
    # Поиск и подстановка региона по данным заказчика
    dataModel["region"] = getRegionFromOkatoCode(dataModel["okato"])
    if dataModel["region"] == 0:
        dataModel["region"] = getRegionFromOktmoCode(dataModel["oktmo"])
    return dataModel


def getRegionFromOkatoCode(okatoCode):
    for region in cfg.dbRegions:
        if len(region.get('okato_code')) == 3:
            if region.get('okato_code')[0:3] == okatoCode[0:3]:
                return region.get('id')
        else:
            if region.get('okato_code')[0:2] == okatoCode[0:2]:
                return region.get('id')
    return 0


def getRegionFromOktmoCode(oktmoCode):
    for region in cfg.dbRegions:
        if len(region.get('oktmo_code')) == 3:
            if region.get('oktmo_code')[0:3] == oktmoCode[0:3]:
                return region.get('id')
        else:
            if region.get('oktmo_code')[0:2] == oktmoCode[0:2]:
                return region.get('id')
    return 0
