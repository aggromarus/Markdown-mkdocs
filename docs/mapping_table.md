# Маппинг данных

## BaseBankAccountDto
| Поле               | Тип данных  | Описание                                                  |
|--------------------|-------------|-----------------------------------------------------------|
| id | integer | Идентификатор банковского счета                           |
| status | string | Статус банковского счета                                  |
| bankId | integer | Идентификатор банка                                       |
| currencyId | integer | <a name='bankaccount-currencyid'><a/>Идентификатор валюты |
| type | string | Вид счета                                                 |
| accountNumber | string | Номер счета                                               |
| budgetAccount | string | Лицевой счет                                              |
| correspondent | string | Корреспондент                                             |
| purpose | string | Назначение                                                |
| exchequerId | integer | Идентификатор УФК/Департамента                            |
| primaryBankAccountFlg | boolean | Основной банковский счет                                  |
| _permissions | object | (смотрите вложенные поля ниже)                            |
| type | string |                                                           |
| create | boolean |                                                           |
| view | boolean |                                                           |
| edit | boolean |                                                           |
| delete | boolean |                                                           |
| methods | array |                                                           |
| childPermissions | array |                                                           |

## Permission
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| type | string |  |
| create | boolean |  |
| view | boolean |  |
| edit | boolean |  |
| delete | boolean |  |
| methods | array |  |
| childPermissions | array |  |

## BankAccountDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор банковского счета |
| status | string | Статус банковского счета |
| bankId | integer | Идентификатор банка |
| currencyId | integer | Идентификатор валюты |
| type | string | Вид счета |
| accountNumber | string | Номер счета |
| budgetAccount | string | Лицевой счет |
| correspondent | string | Корреспондент |
| purpose | string | Назначение |
| exchequerId | integer | Идентификатор УФК/Департамента |
| primaryBankAccountFlg | boolean | Основной банковский счет |
| dateActivate | string | Дата активации счета |
| dateDeactivate | string | Дата деактивации счета |
| _permissions | object | (смотрите вложенные поля ниже) |
| type | string |  |
| create | boolean |  |
| view | boolean |  |
| edit | boolean |  |
| delete | boolean |  |
| methods | array |  |
| childPermissions | array |  |

## CreateBankAccountDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор банковского счета |
| status | string | Статус банковского счета |
| bankId | integer | Идентификатор банка |
| currencyId | integer | Идентификатор валюты |
| type | string | Вид счета |
| accountNumber | string | Номер счета |
| budgetAccount | string | Лицевой счет |
| correspondent | string | Корреспондент |
| purpose | string | Назначение |
| exchequerId | integer | Идентификатор УФК/Департамента |
| primaryBankAccountFlg | boolean | Основной банковский счет |
| dateOpen | string | Дата открытия |
| dateClose | string | Дата закрытия |
| _permissions | object | (смотрите вложенные поля ниже) |
| type | string |  |
| create | boolean |  |
| view | boolean |  |
| edit | boolean |  |
| delete | boolean |  |
| methods | array |  |
| childPermissions | array |  |

## OnlyIdDto
| Поле               | Тип данных  | Описание                            |
|--------------------|-------------|-------------------------------------|
| id | integer | Идентификатор созданной сущности |


## - Номер контракта: {{ Contract.fields.ContractDto.properties.contractName.docName }}