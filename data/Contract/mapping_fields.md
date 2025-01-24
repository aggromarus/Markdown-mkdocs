# Маппинг данных

## TariffContractDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| tariffId | integer | Идентификатор тарифной программы |
| dateStart | string | Дата начала |
| dateEnd | string | Дата окончания |
| dateDeactive | string | Дата отключения |

## TariffContractDetailsDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| tariffId | integer | Идентификатор тарифной программы |
| dateStart | string | Дата начала |
| dateEnd | string | Дата окончания |
| dateDeactive | string | Дата отключения |
| id | integer | Идентификатор записи связи тарифной программы и договора |

## SRProductRestrictorCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| type | string | Тип ограничения |

## SRProductRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор |
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| type | string | Тип ограничения |

## LocalTime
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |

## SRGoodsRestrictorCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| restrictorMeasure | string | Установка лимита в. |
| currencyId | string | Валюта. Заполняется, если restrictorMeasure = Валюта, иначе пусто |
| measure | string | Единицы. Условие заполнения, = Литр/ШТ, если restrictorMeasure = Единицы, иначе пусто |
| sumMax | number | Сумма Max |
| durationType | string | Тип длительности |
| duration | integer | Длительность |
| operationMaxCount | integer | Количество операций Max |
| restrictorDayType | string | Рабочие/Выходные дни |
| weekDay | object | (смотрите вложенные поля ниже) |
| monday | boolean |  |
| tuesday | boolean |  |
| wednesday | boolean |  |
| thursday | boolean |  |
| friday | boolean |  |
| saturday | boolean |  |
| sunday | boolean |  |
| timeSince | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |
| timeTo | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |

## WeekDay
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| monday | boolean |  |
| tuesday | boolean |  |
| wednesday | boolean |  |
| thursday | boolean |  |
| friday | boolean |  |
| saturday | boolean |  |
| sunday | boolean |  |

## SRGoodsRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| restrictorMeasure | string | Установка лимита в. |
| currencyId | string | Валюта. Заполняется, если restrictorMeasure = Валюта, иначе пусто |
| measure | string | Единицы. Условие заполнения, = Литр/ШТ, если restrictorMeasure = Единицы, иначе пусто |
| sumMax | number | Сумма Max |
| durationType | string | Тип длительности |
| duration | integer | Длительность |
| operationMaxCount | integer | Количество операций Max |
| restrictorDayType | string | Рабочие/Выходные дни |
| weekDay | object | (смотрите вложенные поля ниже) |
| monday | boolean |  |
| tuesday | boolean |  |
| wednesday | boolean |  |
| thursday | boolean |  |
| friday | boolean |  |
| saturday | boolean |  |
| sunday | boolean |  |
| timeSince | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |
| timeTo | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |
| id | integer | Идентификатор |

## SRGeoRestrictorCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string | Тип ограничения |
| countryId | string | Страна |
| regionId | integer | Регион |
| gasStationId | integer | АЗС |
| partnerId | integer | Партнер АЗС |

## SRGeoRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор |
| type | string | Тип ограничения |
| countryId | string | Страна |
| regionId | integer | Регионы |
| gasStationId | integer | АЗС |
| partnerId | integer | Партнер АЗС |

## ServiceRequestFuelDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| fuelCardNumber | string | Номер карты |
| w4FuelCardStatus | string | Статус топливной карты получаемой из w4 |
| w4CardIssueDate | string | Дата выпуска карты получаемой из w4 |

## ServiceRequestUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| channel | string | Канал, по которому поступило обращение |
| type | string | Тип обращения |
| theme | string | Тема обращения |
| bindingType | string | Тип привязки |
| cardCount | integer | Число карт |
| bottomBorder | string | Нижняя граница диапазона |
| topBorder | string | Верхняя граница диапазона |
| receiveType | string | Тип получения карт |
| deliveryOfficeId | integer | ID оффиса для самовывоза |
| srCardIssueDate | string | Дата выдачи карт |
| date | string | Дата обращения клиента |
| openDate | string | Начало работы |
| endDate | string | Окончание работы |
| responsibleManagerId | integer | ID Ответственного по обращению |
| personBuyerId | integer | ID КЛ покупателя по обращению |
| personVendorId | integer | ID КЛ продавца\поставщика по обращению |
| comment | string | Комментарий |
| createdBy | integer | ID пользователя, создавшего обращение |
| status | string | Статус обращения |
| transferStatus | string | Статус передачи в w4 |
| transferError | string | Ошибка при передачи в w4 |
| fuelCards | array | Список топливных карт обращения |

## ServiceRequestDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор обращения |
| contractId | integer | Идентификатор договора |
| clientId | integer | Идентификатор контрагента |
| date | string | Дата обращения |
| number | string | Номер обращения |
| bsnUnitId | integer | Организация |
| responsibleManagerId | integer | Ответственный по обращению |
| channel | string | Канал |
| type | string | Тип обращения |
| theme | string | Тема обращения |
| comment | string | Комментарий |
| openDate | string | Время создания обращения |
| endDate | string | Время закрытия обращения |
| status | string | Статус обращения |
| personBuyerId | integer | ID КЛ покупателя по обращению |
| personVendorId | integer | ID КЛ продавца\поставщика по обращению |
| bindingType | string | Тип привязки |
| cardCount | integer | Число карт |
| bottomBorder | string | Нижняя граница диапазона |
| topBorder | string | Верхняя граница диапазона |
| receiveType | string | Способ получения карт |
| deliveryOfficeId | integer | Офис |
| srCardIssueDate | string | Дата выдачи карт |
| commissionType | string | Тип комиссии за ТК |
| availableBalance | number | Доступный остаток |
| totalCostCard | number | Общая стоимость карт |
| transferStatus | string | Статус передачи карт в процессинг |
| transferError | string | Ошибка передачи в процессинг |
| fuelCards | array | Топливные карты |
| createdBy | integer | Идентификатор пользователя, создавшего обращение |
| created | string | Дата создания обращения |

## ServiceRequestFullFuelDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| fuelCardNumber | string | Номер карты |
| w4FuelCardStatus | string | Статус топливной карты получаемой из w4 |
| w4CardIssueDate | string | Дата выпуска карты получаемой из w4 |
| id | integer |  |
| fuelCardId | integer |  |

## ProductRestrictorUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string | Тип ограничения |
| status | string | Статус |
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |
| w4Status | string | Статус передачи в W4 |
| w4Error | string | Ошибка передачи в W4 |

## ProductRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string | Тип ограничения |
| status | string | Статус |
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |
| w4Status | string | Статус передачи в W4 |
| w4Error | string | Ошибка передачи в W4 |
| id | integer | Идентификатор продуктового ограничителя |

## GoodsRestrictorUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| status | string | Статус |
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| restrictorMeasure | string | Установка лимита в. |
| measure | string | Единицы. Условие заполнения, = Литр/ШТ, если restrictorMeasure = Единицы, иначе пусто |
| currencyId | string | Валюта. Заполняется, если restrictorMeasure = Валюта, иначе пусто |
| sumMax | number | Сумма Max |
| usedValue | number | Израсходованная сумма |
| durationType | string | Тип длительности |
| duration | integer | Длительность |
| operationMaxCount | integer | Количество операций Max |
| operationUsedCount | integer | Количество проведенных операций |
| restrictorDayType | string | Рабочие/Выходные дни |
| weekDay | object | (смотрите вложенные поля ниже) |
| monday | boolean |  |
| tuesday | boolean |  |
| wednesday | boolean |  |
| thursday | boolean |  |
| friday | boolean |  |
| saturday | boolean |  |
| sunday | boolean |  |
| timeSince | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |
| timeTo | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |

## GoodsRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| status | string | Статус |
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| restrictorMeasure | string | Установка лимита в. |
| measure | string | Единицы. Условие заполнения, = Литр/ШТ, если restrictorMeasure = Единицы, иначе пусто |
| currencyId | string | Валюта. Заполняется, если restrictorMeasure = Валюта, иначе пусто |
| sumMax | number | Сумма Max |
| usedValue | number | Израсходованная сумма |
| durationType | string | Тип длительности |
| duration | integer | Длительность |
| operationMaxCount | integer | Количество операций Max |
| operationUsedCount | integer | Количество проведенных операций |
| restrictorDayType | string | Рабочие/Выходные дни |
| weekDay | object | (смотрите вложенные поля ниже) |
| monday | boolean |  |
| tuesday | boolean |  |
| wednesday | boolean |  |
| thursday | boolean |  |
| friday | boolean |  |
| saturday | boolean |  |
| sunday | boolean |  |
| timeSince | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |
| timeTo | object | (смотрите вложенные поля ниже) |
| hour | integer |  |
| minute | integer |  |
| second | integer |  |
| nano | integer |  |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |
| id | integer | Идентификатор товарного ограничителя |

## GeoRestrictorUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string | Тип ограничения |
| status | string | Статус |
| countryId | string | Страна |
| regionId | integer | Идентификатор региона |
| gasStationId | integer | Идентификатор АЗС |
| partnerId | integer | Идентификатор партнера АЗС |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |
| w4Status | string | Статус передачи в W4 |
| w4Error | string | Ошибка передачи в W4 |

## GeoRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string | Тип ограничения |
| status | string | Статус |
| countryId | string | Страна |
| regionId | integer | Идентификатор региона |
| gasStationId | integer | Идентификатор АЗС |
| partnerId | integer | Идентификатор партнера АЗС |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |
| w4Status | string | Статус передачи в W4 |
| w4Error | string | Ошибка передачи в W4 |
| id | integer | Идентификатор географического ограничителя |

## TeamMemberUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| roleTeamMember | string | Роль |
| primarySince | string | Дата установления статуса основной |
| primaryMember | boolean | Признак основной |
| primaryAsku | boolean | Признак основной АСКУ |

## TeamMemberInfoDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор участника команды договора |
| positionId | integer | Идентификатор позиции |
| roleTeamMember | string | Роль |
| primaryMember | boolean | Основной |
| primaryAsku | boolean | Основной АСКУ |
| primarySince | string | Основной |
| followDivisionId | integer | Идентификатор офиса продаж |
| followOrganizationId | integer | Идентификатор отделения ГПН |
| firstName | string | Имя |
| lastName | string | Фамилия |
| middleName | string | Отчество |
| mobilePhone | string | Мобильный телефон |
| workPhone | string | Рабочий телефон |
| email | string | Email |

## SignatoriesDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| personBuyerId | integer | Идентификатор покупателя |
| personVendorId | integer | Идентификатор поставщика |

## OrgMemberUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| roleParticipant | string | Роль |
| clientId | integer | Идентификатор КА |

## OrgMemberInfoDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор участника договора |
| roleParticipant | string | Роль |
| shortName | string | Краткое наименование КА |
| clientId | integer | Идентификатор КА |
| opf | string | Справочник ОПФ |
| inn | string | ИНН |
| kpp | string | КПП |
| ogrn | string | ОГРН/ОГРНИП |
| status | string | Статус |

## FuelCardUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| fuelCardStatus | string | Статус топливной карты |
| transferFlag | boolean | Карта перенесена |
| cardType | string | Тип топливной карты |
| productType | string | Тип продукта |
| cardCommissionStatus | string | Статус списания комиссии за ТК |
| cardCarrierType | string | Тип носителя |
| changeStatusReason | string | Причина блокировки\разблокировки |
| comments | string | Примечания менеджера |
| availableBalance | number | Доступный остаток |
| maxPinAttempts | integer | MAX счетчик неверного ввода PIN |
| pinAttemptsCount | integer | Текущее количество неверных попыток |
| pinResetCount | integer | Количество сбросов PIN |
| pinResetDate | string | Дата последнего сброса счетчика неверного ввода PIN |
| roadServiceFlag | boolean | Услуга «Оплата дорожных сборов» |
| autodorServiceFlag | boolean | Услуга «Автодор» |
| madeMpcFlag | boolean | Выпущен МПК |
| w4Status | string | Статус передачи в W4, справочник ЛОВ |
| w4Error | string | Ошибка передачи в W4 |

## FuelCardDetailDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор |
| finAccountId | integer | Идентификатор фин. аккаута |
| cardNumber | string | Номер топливной карты |
| idW4 | string | Идентификатор карты, присвоенный процессингом после привязки |
| fuelCardStatus | string | Статус топливной карты |
| transferFlag | boolean | Карта перенесена |
| cardType | string | Тип топливной карты |
| productType | string | Тип продукта |
| cardCommissionStatus | string | Статус списания комиссии за ТК |
| cardCarrierType | string | Тип носителя |
| changeStatusReason | string | Причина блокировки\разблокировки |
| contractAcceptorId | string | Договор с которого перенесли ТК |
| contractRecipientId | string | Договор на который перенесли ТК |
| cardTransferDate | string | Дата переноса ТК |
| comments | string | Примечания менеджера |
| lastActivityDate | string | Дата последнего использования |
| cardIssueDate | string | Дата выпуска ТК |
| cardExpireDate | string | Срок действия ТК |
| availableBalance | number | Доступный остаток |
| maxPinAttempts | integer | MAX счетчик неверного ввода PIN |
| pinAttemptsCount | integer | Текущее количество неверных попыток |
| pinResetCount | integer | Количество сбросов PIN |
| pinResetDate | string | Дата последнего сброса счетчика неверного ввода PIN |
| roadServiceFlag | boolean | Услуга «Оплата дорожных сборов» |
| autodorServiceFlag | boolean | Услуга «Автодор» |
| madeMpcFlag | boolean | Выпущен МПК |
| w4Status | string | Статус передачи в W4, справочник ЛОВ |
| w4Error | string | Ошибка передачи в W4 |
| contractId | integer | Идентификатор контракта |
| serviceRequestId | integer | Идентификатор обращения |

## DriverUpdateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| personId | integer | Идентификатор водителя |
| primaryFlag | boolean | Флаг основной водитель |

## DriverDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор связки водитель - топливная карта |
| personId | integer | Идентификатор водителя |
| person | object | (смотрите вложенные поля ниже) |
| firstName | string | Имя |
| lastName | string | Фамилия |
| middleName | string | Отчество |
| email | string | Email |
| phone | string | Телефон |
| primaryFlag | boolean | Флаг основного водителя |

## PersonDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| firstName | string | Имя |
| lastName | string | Фамилия |
| middleName | string | Отчество |
| email | string | Email |
| phone | string | Телефон |

## ContractDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| contractType | string | Тип договора |
| contractName | string | Наименование договора от даты заключения |
| saleStage | string | Этап продаж |
| conclusionDate | string | Дата заключения договора |
| effectiveDate | string | Дата вступления в силу договора |
| closureDate | string | Дата закрытия |
| endDate | string | Дата окончания договора |
| edoId | integer | Идентификатор ЭДО |
| edoProvider | string | ЭДО провайдер |
| segment | string | Сегмент договора |
| additionalServiceContract | string | Договор на доп. услугу |
| discountScheme | string | Схема расчета скидки |
| paymentTerms | string | Условие оплаты |
| invoicingScheme | string | Схема оплаты |
| contractPricing | string | Цена в |
| contractPaying | string | Оплата в |
| autoRenewal | boolean | Автоматическая пролонгация договора |
| notes | string | примечание |
| commissionType | string | Тип комиссии за ТК |
| expectedTurnoverPmonth | number | Предполагаемый оборот в месяц |
| lossReason | string | Причина проигрыша |
| labeledProductList | string | Маркированная продукция |
| statusApproval | string | Статус согласования договора |
| notePrintForm | string | Примечание для печатных форм участников договора |
| includeHolding | boolean | Входит в холдинг |
| paymentBillDateScheme | string | Выставление счетов на оплату |
| consentNewsletter | boolean | Согласие на информационную рассылку |
| nonTypicalContract | boolean | Нетиповой договор |
| refuelByLk | boolean | Онлайн заправка из ЛК |
| payByPhoneNumber | boolean | Оплата по номеру телефона |
| waitingAgreement | boolean | Ожидание согласования |
| declineOfferContract | boolean | Отказ от договора-оферты |
| consentAd | boolean | Согласие на рекламную рассылку |
| blockUnblockReason | string | Причина блокировки/разблокировки договора |
| closureReason | string | Причина расторжения/закрытия договора |
| infoThresholdL | number | Информационный порог (литры) |
| infoThresholdRub | number | Информационный порог (рубли) |
| balanceNotice | number | Информирование менеджера, баланс |
| daysForPay | integer | Количество дней на оплату |
| billingDays | string | Дни выставления счетов |
| w4Id | integer | Идентификатор в Way4 |

## ContractDetailInfoDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| contractType | string | Тип договора |
| contractName | string | Наименование договора от даты заключения |
| saleStage | string | Этап продаж |
| conclusionDate | string | Дата заключения договора |
| effectiveDate | string | Дата вступления в силу договора |
| closureDate | string | Дата закрытия |
| endDate | string | Дата окончания договора |
| edoId | integer | Идентификатор ЭДО |
| edoProvider | string | ЭДО провайдер |
| segment | string | Сегмент договора |
| additionalServiceContract | string | Договор на доп. услугу |
| discountScheme | string | Схема расчета скидки |
| paymentTerms | string | Условие оплаты |
| invoicingScheme | string | Схема оплаты |
| contractPricing | string | Цена в |
| contractPaying | string | Оплата в |
| autoRenewal | boolean | Автоматическая пролонгация договора |
| notes | string | примечание |
| commissionType | string | Тип комиссии за ТК |
| expectedTurnoverPmonth | number | Предполагаемый оборот в месяц |
| lossReason | string | Причина проигрыша |
| labeledProductList | string | Маркированная продукция |
| statusApproval | string | Статус согласования договора |
| notePrintForm | string | Примечание для печатных форм участников договора |
| includeHolding | boolean | Входит в холдинг |
| paymentBillDateScheme | string | Выставление счетов на оплату |
| consentNewsletter | boolean | Согласие на информационную рассылку |
| nonTypicalContract | boolean | Нетиповой договор |
| refuelByLk | boolean | Онлайн заправка из ЛК |
| payByPhoneNumber | boolean | Оплата по номеру телефона |
| waitingAgreement | boolean | Ожидание согласования |
| declineOfferContract | boolean | Отказ от договора-оферты |
| consentAd | boolean | Согласие на рекламную рассылку |
| blockUnblockReason | string | Причина блокировки/разблокировки договора |
| closureReason | string | Причина расторжения/закрытия договора |
| infoThresholdL | number | Информационный порог (литры) |
| infoThresholdRub | number | Информационный порог (рубли) |
| balanceNotice | number | Информирование менеджера, баланс |
| daysForPay | integer | Количество дней на оплату |
| billingDays | string | Дни выставления счетов |
| w4Id | integer | Идентификатор в Way4 |
| id | integer | ID Договора |
| clientId | integer | ID Покупателя |
| shortName | string | Короткое имя КА |
| inn | string | ИНН КА |
| contractNumber | string | Номер договора |
| uniquePayId | string | Уникальный идентификатор платежа |
| segmentUpdDate | string | Дата обновления сегмента |
| personBuyerId | integer | ID КЛ покупателя |
| personVendorId | integer | ID КЛ поставщика |
| promoName | string | Наименование промоакции |
| invitedByReferer | string | Краткое наименование реферера, который привлек КА |
| referrersContract | string | Номер договора реферера, в рамках которого привлечен КА |
| orgConsignee | integer | ID грузополучателя |
| finAccount | object | (смотрите вложенные поля ниже) |
| id | integer | Идентификатор записи финансовой информации |
| contractId | integer | Идентификатор договора |
| w4StatusContract | string | Статус договора |
| accountNumber | string | Номер лицевого счета |
| accountStatus | string | Статус лицевого счета |
| balance | number | Собственные средства с учетом заблокированной суммы |
| currentBalance | number | Собственные средства |
| minBalance | number | Значение неснижаемого остатка |
| availableBalance | number | Доступный остаток |
| totalBalance | number | Общий баланс контракта, включая балансы дочерних контрактов |
| currentVolume | number | Объем потребления в текущем месяце (в литрах) |
| previousVolume | number | Объем потребления в предыдущем месяце (в литрах) |
| chargesCurrentMonth | number | Расход в текущем месяце |
| releaseCardNum | integer | Число карт контракта |
| activeCardNum | integer | Число активных карт контракта |
| lastPayment | number | Сумма последнего платежа |
| lastPaymentDate | string | Дата последнего платежа |
| blocked | number | Сумма собственных заблокированных средств |
| totalBlocked | number | Общая сумма заблокированных средств, включая заблокированные средства дочерних контрактов |
| contractTeamMembers | array |  |
| fuelCards | array |  |
| orgMembers | array |  |
| primaryFollowDivision | string | Названия основного офиса продаж, где сопровождает договор |
| primaryFollowOrganization | string | Название основного отделения, где сопровождается договор |
| followOrganizations | array | Сопровождается в отделении. Организации, где сопровождается договор |
| followDivisions | array | Сопровождается в офисе продаж. Подразделения, где сопровождается договор |
| created | string | Дата создания договора |
| lastUpd | string | Дата последнего обновления договора |

## FinAccountDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор записи финансовой информации |
| contractId | integer | Идентификатор договора |
| w4StatusContract | string | Статус договора |
| accountNumber | string | Номер лицевого счета |
| accountStatus | string | Статус лицевого счета |
| balance | number | Собственные средства с учетом заблокированной суммы |
| currentBalance | number | Собственные средства |
| minBalance | number | Значение неснижаемого остатка |
| availableBalance | number | Доступный остаток |
| totalBalance | number | Общий баланс контракта, включая балансы дочерних контрактов |
| currentVolume | number | Объем потребления в текущем месяце (в литрах) |
| previousVolume | number | Объем потребления в предыдущем месяце (в литрах) |
| chargesCurrentMonth | number | Расход в текущем месяце |
| releaseCardNum | integer | Число карт контракта |
| activeCardNum | integer | Число активных карт контракта |
| lastPayment | number | Сумма последнего платежа |
| lastPaymentDate | string | Дата последнего платежа |
| blocked | number | Сумма собственных заблокированных средств |
| totalBlocked | number | Общая сумма заблокированных средств, включая заблокированные средства дочерних контрактов |

## FollowDivisionDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| followDivisionId | integer | Сопровождается в офисе продаж. Идентификатор подразделения ГПН, где будет сопровождаться договор |
| primaryFlg | boolean | Флаг - основное подразделение |

## FollowOrganizationDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| followOrganizationId | integer | Сопровождается в отделении. Идентификатор организации ГПН, где сопровождается договор |
| primaryFlg | boolean | Флаг - основное подразделение |

## OrgMemberDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| clientId | integer | Идентификатор КА |
| roleParticipant | string | Роль |

## ContractInfoDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор контракта |
| clientId | integer | ID Покупателя |
| contractType | string | Тип договора |
| contractNumber | string | Номер договора. Формируется системой |
| contractName | string | Наименование договора от даты заключения |
| saleStage | string | Этап продаж |
| conclusionDate | string | Дата заключения договора |
| effectiveDate | string | Дата вступления в силу договора |
| closureDate | string | Дата закрытия |
| endDate | string | Дата окончания договора |
| orgMembers | array | Организационные члены |

## ServiceRequestCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| channel | string | Канал, по которому поступило обращение |
| type | string | Тип обращения |
| theme | string | Тема обращения |
| bindingType | string | Тип привязки |
| cardCount | integer | Число карт |
| bottomBorder | string | Нижняя граница диапазона |
| topBorder | string | Верхняя граница диапазона |
| receiveType | string | Тип получения карт |
| deliveryOfficeId | integer | ID оффиса для самовывоза |
| srCardIssueDate | string | Дата выдачи карт |
| date | string | Дата обращения клиента |
| openDate | string | Начало работы |
| endDate | string | Окончание работы |
| responsibleManagerId | integer | ID Ответственного по обращению |
| personBuyerId | integer | ID КЛ покупателя по обращению |
| personVendorId | integer | ID КЛ продавца\поставщика по обращению |
| comment | string | Комментарий |
| createdBy | integer | ID пользователя, создавшего обращение |
| fuelCards | array | Список топливных карт обращения |

## ServiceRequestFuelCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| fuelCardNumber | string | Номер карты |

## ProductRestrictorCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string | Тип ограничения |
| status | string | Статус |
| productTypeCode | string | Код типа товара |
| productGroupCode | string | Код группы товара |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |

## GeoRestrictorCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string | Тип ограничения |
| status | string | Статус |
| countryId | string | Страна |
| regionId | integer | Идентификатор региона |
| gasStationId | integer | Идентификатор АЗС |
| partnerId | integer | Идентификатор партнера АЗС |
| lastUpdRestrictor | string | Дата последнего изменения лимита |
| lastUpdRestrictorBy | integer | Источник изменения |

## ContractCreateDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| positionId | integer | ID штатки текущего пользователя |
| clientId | integer | ID клиента |
| followOrganizations | array | Сопровождается в отделении. Организации, где сопровождается договор |
| followDivisions | array | Сопровождается в офисе продаж. Подразделения, где сопровождается договор |

## PageTransferFundsDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## PageableObject
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |

## SortObject
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| direction | string |  |
| nullHandling | string |  |
| ascending | boolean |  |
| property | string |  |
| ignoreCase | boolean |  |

## TransferFundsDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| user | string | Пользователь |
| transferType | string | Тип перевода |
| transferAmount | integer | Сумма перевода |
| created | string | Дата перевода |

## TransactionDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer |  |
| direct | string |  |
| operationDate | string |  |
| currency | string |  |
| outletName | string |  |
| sumWithDiscount | number |  |
| paymentTypeId | integer |  |
| serviceFee | number |  |

## TransactionDetailDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer |  |
| productName | string |  |
| quantityGoods | integer |  |
| measure | string |  |
| productCost | number |  |
| costBeforeDiscount | number |  |
| sumDiscount | number |  |
| serviceFee | number |  |

## TransactionFullDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer |  |
| direct | string |  |
| operationDate | string |  |
| currency | string |  |
| outletName | string |  |
| sumWithDiscount | number |  |
| paymentTypeId | integer |  |
| serviceFee | number |  |
| transactionsDetail | array |  |

## WayTransactionDetailInfoRequest
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| ID | integer | ID транзакции |

## Response
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| body | object |  |
| error | object |  |

## WayTransactionsByContractRequest
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| Card | integer | ID договора/карты |
| TransactionCount | integer | Кол-во транзакций |

## TariffContractDetailsFullDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор записи связи таринфной программы и договора |
| tariffId | integer | Идентификатор тарифной программы |
| tariffCode | string | Код тарифной программы |
| tariffName | string | Название тарифной программы |
| tariffDescription | string | Описание тарифной программы |
| tariffType | string | Тип тарифной программы |
| dateStart | string | Дата начала |
| dateEnd | string | Дата окончания |
| dateDeactive | string | Дата отключения |

## PageSRProductRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## PageSRGoodsRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## PageSRGeoRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## PageServiceRequestSearchGetDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## ServiceRequestSearchGetDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer |  |
| number | string |  |
| created | string |  |
| createdBy | integer |  |
| channel | string |  |
| type | string |  |
| theme | string |  |
| status | string |  |
| personBuyerId | integer |  |
| personVendorId | integer |  |

## WayRestrictionsDTO
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| ContractSearchMethod | string |  |
| ContractScope | string |  |
| ContractIdentifier | string |  |
| ContractRelation | string |  |
| CardGroupCode | string |  |
| CardSequenceNumber | string |  |
| ExpirationDate | string |  |

## PageProductRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## PageGoodsRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## PageGeoRestrictorDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## ParticipantsTeamMembersDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| teamMembers | array | Команда договора |

## ParticipantsOrgMembersDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| orgMember | array | Участники договора |
| personBuyerId | integer | Идентификатор покупателя |
| personVendorId | integer | Идентификатор поставщика |

## FuelCardDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор записи топливной карты |
| cardNumber | string | Номер карты |
| idW4 | string | Идентификатор карты, присвоенный процессингом после привязки |
| productType | string | Тип продукта |
| cardStatus | string | Статус топливной карты |
| lastUseDate | string | Дата последнего использования |
| created | string | Дата создания |
| madeMpcFlag | boolean | Выпущен МПК |
| primaryDriver | object | (смотрите вложенные поля ниже) |
| firstName | string | Имя |
| lastName | string | Фамилия |
| middleName | string | Отчество |
| email | string | Email |
| phone | string | Телефон |
| cardIssueDate | string | Дата выпуска ТК |
| w4Status | string | Статус w4 |
| w4Error | string | Текст ошибки w4 |
| cardGroup | string | Группу карт |
| contractNumber | string | Номер договора |
| clientId | integer | Иденитфикатор контрагента |
| clientShortName | string | Наименование контрагента |
| contractAcceptorId | string | Договор с которого перенесли ТК |
| contractRecipientId | string | Договор на который перенесли ТК |
| cardCarrierType | string | Тип носителя ТК |
| contractId | integer | Идентификатор договора |
| serviceRequestId | integer | Идентификатор обращения |

## PageFuelCardDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## PageDriverDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |

## ContractBaseDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор договора |
| contractNumber | string | № договора |
| contractName | string | Наименование договора |
| contractType | string | Тип договора |
| saleStage | string | Этап продаж договора |
| statusApproval | string | Статус |
| paymentTerms | string | Условия оплаты |
| invoicingScheme | string | Схема оплаты |
| clientId | integer | Идентификатор КА |
| shortName | string | Краткое наименование КА |
| inn | string | ИНН Контрагента |
| waitingAgreement | boolean | Ожидает согласования |
| discountScheme | string | Схема расчета скидки |
| closureDate | string | Дата закрытия договора |
| conclusionDate | string | Дата заключения договора |
| effectiveDate | string | Дата вступления в силу договора |
| endDate | string | Дата окончания договора |
| askuStatus | string | Статус синхронизации с АСКУ |
| askuError | string | Текст ошибки синхронизации с АСКУ |
| w4Status | string | Статус синхронизации с процессингом |
| w4Error | string | Текст ошибки синхронизации с процессингом |
| primaryFollowDivision | string | Основной офис сопровождения |
| primaryFollowOrganization | string | Основное отделение сопровождения |
| edoFlag | boolean | ЭДО |

## PageContractBaseDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| totalElements | integer |  |
| totalPages | integer |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort | array |  |
| numberOfElements | integer |  |
| pageable | object | (смотрите вложенные поля ниже) |
| offset | integer |  |
| sort | array |  |
| unpaged | boolean |  |
| paged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |
| first | boolean |  |
| last | boolean |  |
| empty | boolean |  |
