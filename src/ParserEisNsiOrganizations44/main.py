from appmodules import parserSettings as cfg
from appmodules import parser as nsiParser
import sys


def main():
    if len(sys.argv) == 1:
        print("Не выбран режим работы парсера: -all; -update. \n"
              " -all - загрузка всего справочника, \n"
              " -update - загрузка только файлов *inc*.")
        return
    else:
        if sys.argv[1] == "-all" or sys.argv[1] == "-update":
            cfg.parserParam = sys.argv[1]
        else:
            print("Не правильно указан режим работы парсера ({}): -all; -update. \n"
                  " -all - загрузка всего справочника, \n"
                  " -update - загрузка только файлов *inc*.".format(sys.argv[1]))
            return
    cfg.appLogger.write("Начало сбора данных для парсинга.")
    nsiParser.prepareDataSources()
    cfg.appLogger.write("Информация для парсинга была собрана.")
    nsiParser.parseDataAndExportToDb()
    cfg.appLogger.write("Было добавлено {} организаций.".format(cfg.parserAdd))
    cfg.appLogger.write("Было обновлено {} организаций.".format(cfg.parserUpd))
    nsiParser.clearTmpFolder()
    cfg.appLogger.write("Каталог временных файлов был очищен.")


main()
