from sqlalchemy import *
import pandas as pd
from datetime import *

engine = create_engine('sqlite:///C:\\Users\\anast\\Documents\\GitHub\\FA\\2 курс\\Python & SQL\\Pract 3\\smth.db')

metadata = MetaData()

#Список организаций, обслуживающихся в банке
Organizations = Table('Organizations', metadata,
                      Column('ID', Integer(), primary_key=True),
                      Column('Name', String(255), nullable=False, unique=True),
                      Column('Owner', String(50), nullable=False),
                      Column('Registration_certificate', Integer(), nullable=False, unique=True),
                      Column('Phone_number', Integer(), nullable=False),
                      Column('Address', String(255), nullable=False),
                      extend_existing=True
                     )

#Список клиентов банка, клиент может быть записан 2 раза, как представитель организации (Type=True), либо как физ. лицо (Type=False)
Clients = Table('Clients', metadata,
                Column('ID', Integer(), primary_key=True),
                Column('Surname', String(50), nullable=False),
                Column('Name', String(50), nullable=False),
                Column('Middle_name', String(50)),
                Column('Passport', Integer(), nullable=False, unique=True),
                Column('Phone_number', Integer(), nullable=False, unique=True),
                Column('Address', String(255), nullable=False),
                Column('Type', Boolean(), nullable=False), #Тип клиента, юр. ли лицо
                Column('Organisation code', Integer(), ForeignKey('Organizations.ID')), #Если юр. лицо, то какую организацию представляет
                extend_existing=True
               )

#Счета в банке
Bank_accounts = Table('Bank_accounts', metadata,
                      Column('ID', Integer(), primary_key=True), #Если счетов не много, то ID будет удобнее длинного номера
                      Column('Number', Integer(), nullable=False, unique=True),
                      Column('Client_ID', Integer(), ForeignKey('Clients.ID')), #Ссылка на клиента
                      Column('Balance', Integer(), nullable=False),
                      Column('Open_date', DateTime(), nullable=False),
                      Column('Close_date', DateTime()),
                      extend_existing=True
                     )

#Справочник операций банка
Operations_list = Table('Operations_list', metadata,
                        Column('ID', Integer(), primary_key=True),
                        Column('Name', String(50), nullable=False),
                        Column('Note', String(255)),
                        extend_existing=True
                       )

#Справочник городов
Cities = Table('Cities', metadata,
               Column('ID', Integer(), primary_key=True),
               Column('Name', String(50), nullable=False),
               extend_existing=True
              )

#Справочник филлиалов
Departments = Table('Departments', metadata,
                    Column('ID', Integer(), primary_key=True),
                    Column('Department_head', String(50)),
                    Column('City', String(50), ForeignKey('Cities.ID')),
                    extend_existing=True
                   )

#Работники организации
Employees = Table('Employees', metadata,
                  Column('ID', Integer(), primary_key=True),
                  Column('Bank_account_ID', Integer(), nullable=False),
                  Column('Post', String(50), nullable=False), #Должность
                  Column('Surname', String(50), nullable=False),
                  Column('Name', String(50), nullable=False),
                  Column('Middle_name', String(50)),
                  Column('Passport', Integer(), nullable=False, unique=True),
                  Column('Phone_number', Integer(), nullable=False, unique=True),
                  Column('Address', String(255), nullable=False),
                  Column('Department_ID', Integer(), ForeignKey('Departments.ID')), #Cсылка на филиал
                  extend_existing=True
                 )

#Журнал операций
Account_transactions = Table('Account_transactions', metadata,
                             Column('ID', Integer(), primary_key=True),
                             Column('Account_ID', Integer(), ForeignKey('Bank_accounts.ID')), #Ссылка на плательщика
                             Column('Operation_ID', Integer(), ForeignKey('Operations_list.ID')), #Ссылка на код операции
                             Column('Recipient_ID', Integer(), ForeignKey('Bank_accounts.ID')), #Ссылка на получателя
                             Column('Amount_of_money', Integer()),
                             Column('Served_by', Integer(), ForeignKey('Employees.ID'), nullable=True), #Ссылка на работника, если он проводил операцию
                             extend_existing=True
                            )

metadata.create_all(engine)


our_tables = {'Organizations': Organizations, 
              'Clients': Clients, 
              'Bank_accounts': Bank_accounts, 
              'Operations_list': Bank_accounts, 
              'Cities': Cities, 
              'Departments': Departments, 
              'Employees': Employees, 
              'Account_transactions': Account_transactions}
list_for_tables = []
'''
Table('Organizations', metadata,
                      Column('ID', Integer(), primary_key=True),
                      Column('Name', String(255), nullable=False, unique=True),
                      Column('Owner', String(50), nullable=False),
                      Column('Registration_certificate', Integer(), nullable=False, unique=True),
                      Column('Phone_number', Integer(), nullable=False),
                      Column('Address', String(255), nullable=False),
                      extend_existing=True
                     )
'''
#Заполняем таблицу организаций


list_for_tables.extend(
        [{
        'ID' : 1,
        'Name' : 'ООО Field',
        'Owner' : 'Соловьев В. А.',
        'Registration_certificate' : 737031981456270,
        'Phone_number' : 84952730218,
        'Address' : 'Москва',
        },
{
        'ID' : 2,
        'Name' : 'ООО MEOW',
        'Owner' : 'Котов К. К.',
        'Registration_certificate' : 584478327029084,
        'Phone_number' : 84993721057,
        'Address' : 'Санкт-Петербург',
        }]
)
ins = Organizations.insert()
connection=engine.connect()
#result=connection.execute(ins, list_for_tables)

list_for_tables = []

inp = 'meow'
#while inp != 'EXIT':
inp = input('Введите имя таблицы для заполнения: ')
#while inp != 'END':
ins = our_tables[inp].insert()
print(our_tables[inp].params)

'''
list_for_tables = [{
'ID' : 3,
'Name' : 'ООО MEOW',
'Owner' : 'Котов К. К.',
'Registration_certificate' : 584478027029084,
'Phone_number' : 84993721000,
'Address' : 'Санкт-Петербург',
}]
result=connection.execute(ins, list_for_tables)
'''