from appmodules import parserSettings as cfg
import xmltodict
import traceback


def prepareDataModelFromFile(xmlFile, dataModel):
    exportData = list()
    with open(xmlFile) as dataFile:
        try:
            firstString = dataFile.read()
            dataFromFile = xmltodict.parse(firstString)
            xmlOrganizations = dataFromFile["export"]["nsiOrganizationList"]["nsiOrganization"]
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
    dataModel["eis_regNumber"] = str(xmlOrganization.get('oos:regNumber'))
    dataModel["eis_consRegistryNum"] = str(xmlOrganization.get('oos:consRegistryNum'))
    dataModel["nameFull"] = str(xmlOrganization.get('oos:fullName'))
    dataModel["nameShort"] = str(xmlOrganization.get('oos:shortName'))
    if xmlOrganization.get('oos:factualAddress') is not None:
        if xmlOrganization.get('oos:factualAddress').get('oos:region') is not None:
            dataModel["region"] = int(getRegionFromKladrCode(
                xmlOrganization.get('oos:factualAddress').get('oos:region').get('oos:kladrCode')))
            dataModel["kladrCode"] = str(xmlOrganization.get('oos:factualAddress').get('oos:region').get('oos:kladrCode'))
    dataModel["countryFullName"] = str(xmlOrganization.get('oos:factualAddress').get('oos:country').get(
        'oos:countryFullName'))
    dataModel["inn"] = str(xmlOrganization.get('oos:INN'))
    dataModel["kpp"] = str(xmlOrganization.get('oos:KPP'))
    dataModel["registrationDate"] = str(xmlOrganization.get('oos:registrationDate'))
    dataModel["ogrn"] = str(xmlOrganization.get('oos:OGRN'))
    if xmlOrganization.get('oos:OKFS') is not None:
        dataModel["okfs"] = str(xmlOrganization.get('oos:OKFS').get('oos:code'))
        dataModel["name_okfs"] = str(xmlOrganization.get('oos:OKFS').get('oos:name'))
    if xmlOrganization.get('oos:OKOPF') is not None:
        dataModel["okopf"] = str(xmlOrganization.get('oos:OKOPF').get('oos:code'))
        dataModel["name_okopf"] = str(xmlOrganization.get('oos:OKOPF').get('oos:fullName'))
    if xmlOrganization.get('oos:factualAddress') is not None:
        if xmlOrganization.get('oos:factualAddress').get('oos:OKATO') is not None:
            dataModel["okato"] = str(xmlOrganization.get('oos:factualAddress').get('oos:OKATO'))
            if dataModel["region"] == 0:
                dataModel["region"] = int(getRegionFromOkatoCode(xmlOrganization.get('oos:factualAddress').get('oos:OKATO')))
    if xmlOrganization.get('oos:OKTMO') is not None:
        dataModel["oktmo"] = str(xmlOrganization.get('oos:OKTMO').get('oos:code'))
    dataModel["okpo"] = str(xmlOrganization.get('oos:OKPO'))
    dataModel["OKVED"] = str(xmlOrganization.get('oos:OKVED'))
    if xmlOrganization.get('oos:IKUInfo') is not None:
        if type(xmlOrganization.get('oos:IKUInfo')) == list:
            dataModel["iku"] = str(xmlOrganization.get('oos:IKUInfo')[0].get('oos:IKU'))
            dataModel["dateSt_iku"] = str(xmlOrganization.get('oos:IKUInfo')[0].get('oos:dateStIKU'))
        else:
            dataModel["iku"] = str(xmlOrganization.get('oos:IKUInfo').get('oos:IKU'))
            dataModel["dateSt_iku"] = str(xmlOrganization.get('oos:IKUInfo').get('oos:dateStIKU'))
    # dataModel["legalAddress"] = xmlOrganization['oos:regNumber']
    dataModel["postalAddress"] = str(xmlOrganization.get('oos:postalAddress'))
    dataModel["org_type"] = str(xmlOrganization.get('oos:organizationType').get('oos:name'))
    dataModel["timeZone"] = str(xmlOrganization.get('oos:timeZoneUtcOffset'))
    if xmlOrganization.get('oos:accounts') is not None:
        if type(xmlOrganization.get('oos:accounts').get('oos:account')) == list:
            dataModel["bankAddress"] = str(xmlOrganization.get('oos:accounts').get('oos:account')[0].get('oos:bankAddress'))
            dataModel["bankName"] = str(xmlOrganization.get('oos:accounts').get('oos:account')[0].get('oos:bankName'))
            dataModel["bik"] = str(xmlOrganization.get('oos:accounts').get('oos:account')[0].get('oos:bik'))
            dataModel["corrAccount"] = str(xmlOrganization.get('oos:accounts').get('oos:account')[0].get('oos:corrAccount'))
            dataModel["paymentAccount"] = str(xmlOrganization.get('oos:accounts').get('oos:account')[0].get('oos'
                                                                                                        ':paymentAccount'))
            dataModel["personalAccount"] = str(xmlOrganization.get('oos:accounts').get('oos:account')[0].get('oos'
                                                                                                         ':personalAccount'))
        else:
            dataModel["bankAddress"] = str(xmlOrganization.get('oos:accounts').get('oos:account').get('oos:bankAddress'))
            dataModel["bankName"] = str(xmlOrganization.get('oos:accounts').get('oos:account').get('oos:bankName'))
            dataModel["bik"] = str(xmlOrganization.get('oos:accounts').get('oos:account').get('oos:bik'))
            dataModel["corrAccount"] = str(xmlOrganization.get('oos:accounts').get('oos:account').get('oos:corrAccount'))
            dataModel["paymentAccount"] = str(xmlOrganization.get('oos:accounts').get('oos:account').get('oos'
                                                                                                     ':paymentAccount'))
            dataModel["personalAccount"] = str(xmlOrganization.get('oos:accounts').get('oos:account').get('oos'
                                                                                                      ':personalAccount'))
    if xmlOrganization.get('oos:contactPerson') is not None:
        dataModel["contactFIO"] = "{} {} {}".format(
            xmlOrganization.get('oos:contactPerson').get('oos:lastName'),
            xmlOrganization.get('oos:contactPerson').get('oos:firstName'),
            xmlOrganization.get('oos:contactPerson').get('oos:middleName')
        )
    dataModel["orgPhone"] = str(xmlOrganization.get('oos:phone'))
    dataModel["orgFax"] = str(xmlOrganization.get('oos:fax'))
    dataModel["orgEmail"] = str(xmlOrganization.get('oos:email'))
    dataModel["orgWebsite"] = str(xmlOrganization.get('oos:url'))

    return dataModel


def getRegionFromKladrCode(kladrCode):
    for region in cfg.dbRegions:
        if len(kladrCode) < 13:
            if region.get('kladr_code')[0:len(kladrCode)] == kladrCode:
                return region.get('id')
        else:
            if region.get('kladr_code') == kladrCode:
                return region.get('id')
    return 0


def getRegionFromOkatoCode(okatoCode):
    for region in cfg.dbRegions:
        if region.get('okato_code')[0:2] == okatoCode[0:2]:
            return region.get('id')
    return 0
