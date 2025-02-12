# Список сервисов тут будет, как очередной пример

    Немного описания

> И выделенного текста

## Параграф 1

Здесь мы пробуем использовать переменные из объектов, созданных нами заранее, через yml файлы. 


    Можно еще попробовать сослаться на другую переменную {{ data.Contract.var.parameters.shortName.description }}
    
Можно еще попробовать сослаться на другую переменную {{ data.Contract.var.parameters.shortName}}

> Использование параметров из явных переменных маппера **{{ contract.fields.TariffContractDto.properties.dateEnd.description }}** под капотом выглядит так:

    Использование параметров из явных переменных маппера 
    contract.fields.TariffContractDto.properties.dateEnd.description
    (путь к атрибуту переменной оборачивается в {}
