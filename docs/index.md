# Здесь могла бы быть ваша реклама

For full documentation visit [mkdocs.org](https://www.mkdocs.org).


    Это тестовый стенд, который поднят для проверки возможностей Mkdocs



## Проверка отображения заголовка №2
[Переход на страницу диаграмм](Group-1/diagram-sequence.md)

[И еще одна ссылка](Group-1/diagramm_classes.md)

```puml
@startuml

!theme plain
top to bottom direction
skinparam linetype ortho

class flyway_schema_history {
   installed_rank: integer
   version: varchar(50)
   description: varchar(200)
   type: varchar(20)
   script: varchar(1000)
   checksum: integer
   installed_by: varchar(100)
   installed_on: timestamp
   execution_time: integer
   success: boolean
}
class t_consignee_card {
   id: bigint
   fuel_card_id: bigint
   consignee_id: bigint
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}
class t_fc_geo_restrictor {
   id: bigint
   fuel_card_id: bigint
   type: varchar(30)
   status: varchar(30)
   country_id: varchar(100)
   region_id: bigint
   gas_station_id: bigint
   partner_id: bigint
   last_upd_restrictor: date
   last_upd_restrictor_by: bigint
   siebel_id: varchar(15)
   w4_status: varchar(30)
   w4_error: varchar(255)
   w4_id: varchar(18)
   w4_last_upd: timestamp
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}
class t_fc_goods_restrictor {
   id: bigint
   fuel_card_id: bigint
   status: varchar(30)
   product_type_code: varchar(75)
   product_group_code: varchar(100)
   restrictor_measure: varchar(30)
   currency_id: varchar(30)
   measure: varchar(30)
   sum_max: numeric(12,2)
   duration_type: varchar(30)
   duration: smallint
   operation_max_count: smallint
   operation_used_count: smallint
   restrictor_day_type: varchar(30)
   week_day: jsonb
   time_since: time
   time_to: time
   used_value: numeric(12,2)
   balance_amount: numeric(12,2)
   last_upd_restrictor: date
   last_upd_restrictor_by: bigint
   siebel_id: varchar(15)
   w4_id: varchar(18)
   w4_last_upd: timestamp
   w4_status: varchar(30)
   w4_error: varchar(255)
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}
class t_fc_product_restrictor {
   id: bigint
   fuel_card_id: bigint
   type: varchar(30)
   status: varchar(30)
   product_type_code: varchar(75)
   product_group_code: varchar(100)
   last_upd_restrictor: date
   last_upd_restrictor_by: bigint
   siebel_id: varchar(15)
   w4_id: varchar(18)
   w4_last_upd: timestamp
   w4_status: varchar(30)
   w4_error: varchar(255)
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}
class t_fuel_card {
   id: bigint
   fin_account_id: bigint
   id_w4: varchar(100)
   card_number: varchar(16)
   card_type: varchar(50)
   card_issue_date: date
   card_commission_status: varchar(30)
   card_carrier_type: varchar(30)
   change_status_reason: varchar(30)
   transfer_flag: boolean
   contract_acceptor_id: varchar(30)
   contract_recipient_id: varchar(30)
   card_transfer_date: date
   product_type: varchar(30)
   comments: varchar(255)
   fuel_card_status: varchar(35)
   last_activity_date: date
   card_expire_date: date
   available_balance: numeric(12,2)
   max_pin_attempts: smallint
   pin_attempts_count: smallint
   pin_reset_count: smallint
   pin_reset_date: date
   road_service_flag: boolean
   autodor_service_flag: boolean
   made_mpc_flag: boolean
   w4_status: varchar(250)
   w4_error: varchar(255)
   primary_driver: varchar(150)
   siebel_id: varchar(15)
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}
class t_transaction {
   id: bigint
   fuel_card_id: bigint
   direct: varchar(50)
   operation_date: date
   currency: varchar(30)
   outlet_name: varchar(255)
   sum_with_discount: numeric(12,2)
   payment_type_id: bigint
   service_fee: numeric(12,2)
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}
class t_transaction_detail {
   id: bigint
   transaction_id: bigint
   product_name: varchar(200)
   quantity_goods: smallint
   measure: varchar(30)
   product_cost: numeric(12,2)
   cost_before_discount: numeric(12,2)
   sum_discount: numeric(12,2)
   service_fee: numeric(12,2)
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}
class t_transfer_funds {
   id: bigint
   fuel_card_id: bigint
   user_id: bigint
   transfer_type: varchar(30)
   transfer_amount: numeric(12,2)
   user_fio: varchar(255)
   created: timestamp
   created_by: bigint
   last_upd: timestamp
   last_upd_by: bigint
}

@enduml
```
