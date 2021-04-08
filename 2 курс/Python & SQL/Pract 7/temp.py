from datetime import datetime
from sqlalchemy import (select, create_engine, MetaData, Table, Numeric, String, 
                        insert, update, delete)
from sqlalchemy.exc import IntegrityError

metadata = MetaData()

engine=create_engine('sqlite:///Students1.db')
metadata=MetaData()
connection=engine.connect()

exam_marks=Table('exam_marks', metadata, autoload=True, autoload_with=engine)
lecturer=Table('lecturer', metadata, autoload=True, autoload_with=engine)
student=Table('student', metadata, autoload=True, autoload_with=engine)
subj_lect=Table('subj_lect', metadata, autoload=True, autoload_with=engine)
subject=Table('subject', metadata, autoload=True, autoload_with=engine)
university=Table('university', metadata, autoload=True, autoload_with=engine)

metadata.reflect(bind=engine)

from sqlalchemy.sql import func

#Тут все хорошо
ins_exam_marks1 = insert(exam_marks)
ins_exam_marks1 = ins_exam_marks1.values((33, 12, 43, 5, datetime.strptime('2021.03.01','%Y.%m.%d')))

#А тут неочень
ins_exam_marks2 = insert(exam_marks)
ins_exam_marks2 = ins_exam_marks2.values((34, 10, 22, 3, datetime.strptime('2021.03.01','%Y.%m.%d')))


transaction = connection.begin()

rp = connection.execute(ins_exam_marks1)
print('попытка 1')

try:
    rp = connection.execute(ins_exam_marks2)
    
except IntegrityError as error:
    transaction.rollback()
    print(error)
    