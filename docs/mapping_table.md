| Поле UI | API field                    | BD field | Тип     | Описание                                                     |
|---------|------------------------------|----------|---------|--------------------------------------------------------------|
|         | {{ "id" }}                   |          | integer |                                                              |
|         | {{ "finAccountId" }}         |          | integer | Идентификатор фин. аккаута                                   |
|         | {{ "cardNumber" }}           |          | string  | {{ "cardNumber.description" }}                               |
|         | {{ "idW4" }}                 |          | string  | Идентификатор карты, присвоенный процессингом после привязки |
|         | {{ "fuelCardStatus" }}       |          | string  | Статус топливной карты                                       |
|         | {{ "transferFlag" }}         |          | boolean | Карта перенесена                                             |
|         | {{ "cardType" }}             |          | string  | Тип топливной карты                                          |
|         | {{ "productType" }}          |          | string  | Тип продукта                                                 |
|         | {{ "cardCommissionStatus" }} |          | string  | Статус списания комиссии за ТК                               |
|         | {{ "cardCarrierType" }}      |          | string  | Тип носителя                                                 |
|         | {{ "changeStatusReason" }}   |          | string  | Причина блокировки\разблокировки                             |
|         | {{ "contractAcceptorId" }}   |          | string  | Договор с которого перенесли ТК                              |
|         | {{ "contractRecipientId" }}  |          | string  | Договор на который перенесли ТК                              |
|         | {{ "cardTransferDate" }}     |          | string  | Дата переноса ТК                                             |
|         | {{ "comments" }}             |          | string  | Примечания менеджера                                         |
|         | {{ "lastActivityDate" }}     |          | string  | Дата последнего использования                                |
|         | {{ "cardIssueDate" }}        |          | string  | Дата выпуска ТК                                              |
|         | {{ "cardExpireDate" }}       |          | string  | Срок действия ТК                                             |
|         | {{ "availableBalance" }}     |          | number  | Доступный остаток                                            |
|         | {{ "maxPinAttempts" }}       |          | integer | MAX счетчик неверного ввода PIN                              |
|         | {{ "pinAttemptsCount" }}     |          | integer | Текущее количество неверных попыток                          |
|         | {{ "pinResetCount" }}        |          | integer | Количество сбросов PIN                                       |
|         | {{ "pinResetDate" }}         |          | string  | Дата последнего сброса счетчика неверного ввода PIN          |
|         | {{ "roadServiceFlag" }}      |          | boolean | Услуга «Оплата дорожных сборов»                              |
|         | {{ "autodorServiceFlag" }}   |          | boolean | Услуга «Автодор»                                             |
|         | {{ "madeMpcFlag" }}          |          | boolean | Выпущен МПК                                                  |
|         | {{ "w4Status" }}             |          | string  | Статус передачи в W4, справочник ЛОВ                         |
|         | {{ "w4Error" }}              |          | string  | Ошибка передачи в W4                                         |
|         | {{ "contractId" }}           |          | integer | {{ "contractId.description" }}                               |
|         | {{ "serviceRequestId" }}     |          | integer | Идентификатор обращения                                      |
|         | {{ "personId" }}             |          | integer | Идентификатор водителя                                       |
|         | {{ "firstName" }}            |          | string  | Имя                                                          |
|         | {{ "lastName" }}             |          | string  | Фамилия                                                      |
|         | {{ "middleName" }}           |          | string  | Отчество                                                     |
|         | {{ "email" }}                |          | string  | Email                                                        |
|         | {{ "phone" }}                |          | string  | Данные пользователя                                          |
|         | {{ "primaryFlag" }}          |          | boolean | Флаг основного водителя                                      |
|         | direct                       |          | string  |                                                              |
|         | operationDate                |          | string  |                                                              |
|         | currency                     |          | string  |                                                              |
|         | outletName                   |          | string  |                                                              |
|         | sumWithDiscount              |          | number  |                                                              |
|         | paymentTypeId                |          | integer |                                                              |
|         | serviceFee                   |          | number  |                                                              |
|         | ID                           |          | integer | ID транзакции                                                |
|         | Card                         |          | integer | ID договора/карты                                            |
|         | TransactionCount             |          | integer | Кол-во транзакций                                            |
|         | productName                  |          | string  |                                                              |
|         | quantityGoods                |          | integer |                                                              |
|         | measure                      |          | string  |                                                              |
|         | productCost                  |          | number  |                                                              |
|         | costBeforeDiscount           |          | number  |                                                              |
|         | sumDiscount                  |          | number  |                                                              |
|         | user                         |          | string  | Пользователь                                                 |
|         | transferType                 |          | string  | Тип перевода                                                 |
|         | transferAmount               |          | integer | Сумма перевода                                               |
|         | created                      |          | string  | Дата перевода                                                |


| Поле                 | Описание                          |
|----------------------|----------------------------------|
{% for key, value in FuelCard.fields.items() -%}
| {{ key }}           | {{ value.description if value.description else "—" }} |
{% endfor %}