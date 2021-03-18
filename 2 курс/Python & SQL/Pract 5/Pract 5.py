from sqlalchemy import select, create_engine, MetaData, Table, cast, String, Integer
from sqlalchemy.sql import func

import warnings
warnings.filterwarnings('ignore')

engine = create_engine('sqlite:///C:\\Users\\anast\\Documents\\GitHub\\FA\\2 курс\\Python & SQL\\Pract 5\\Students.db')
metadata=MetaData()
connection=engine.connect()

exam_marks=Table('exam_marks', metadata, autoload=True, autoload_with=engine)
lecturer=Table('lecturer', metadata, autoload=True, autoload_with=engine)
student=Table('student', metadata, autoload=True, autoload_with=engine)
subj_lect =Table('subj_lect', metadata, autoload=True, autoload_with=engine)
subject=Table('subject', metadata, autoload=True, autoload_with=engine)
university=Table('university', metadata, autoload=True, autoload_with=engine)


#Задание 1

s = select([
    cast(student.c.student_id, String(20)) + ';' +
    cast(student.c.surname, String(20)) + ';' +
    cast(student.c.name, String(20)) + ';' +
    cast(student.c.stipend, String(20)) + ';' +
    cast(student.c.city, String(20)) + ';' +
    cast(func.strftime('%d/%m/%Y', student.c.birthday),  String(20)) + ';' +
    cast(student.c.univ_id, String(20)) + '.'
    ])

rp = connection.execute(s)
results = rp.fetchall()

results = [item[0].upper() for item in results if item[0] is not None]
print('Задание 1 \n', results, '\n')


#Задание 2

s = select([
    cast(func.substr(student.c.name, 1, 1), String(20)) + '.' +
    cast(student.c.surname, String(20)) + '; место жительства-' +
    cast(student.c.city, String(20)) + '; родился - ' +
    cast(func.strftime('%d.%m.%Y.', student.c.birthday),  String(20))
    ])

rp = connection.execute(s)
results = rp.fetchall()

results = [item[0][0:item[0].find('; место жительства-')].upper() + '; место жительства-' + item[0][item[0].find('; место жительства-')+len('; место жительства-'):item[0].find('; родился - ')].upper() + item[0][item[0].find('; родился - '):] for item in results if item[0] is not None]
print('Задание 2 \n', results, '\n')


#Задание 3

s = select([
    cast(func.substr(student.c.name, 1, 1), String(20)) + '.' +
    cast(student.c.surname, String(20)) + '; место жительства-' +
    cast(student.c.city, String(20)) + '; родился: ' +
    cast(func.strftime('%d-%m-%Y', student.c.birthday),  String(20))
    ])

rp = connection.execute(s)
results = rp.fetchall()

results = [item[0].lower() for item in results if item[0] is not None]
print('Задание 3 \n', results, '\n')


#Задание 4

s = select([
    cast(student.c.name, String(20)) + ' ' +
    cast(student.c.surname, String(20)) + ' родился в ' +
    cast(func.strftime('%Y', student.c.birthday),  String(20)) + ' году.'
    ])

rp = connection.execute(s)
print('Задание 4 \n', rp.fetchall(), '\n')


#Задание 5

s = select([
    student.c.surname,
    student.c.name,
    student.c.stipend*100
    ])

rp = connection.execute(s)
print('Задание 5 \n', rp.fetchall(), '\n')


#Задание 6
s = select([
    cast(student.c.name, String(20)) + ' ' +
    cast(student.c.surname, String(20)) + ' родился в ' +
    cast(func.strftime('%Y', student.c.birthday),  String(20)) + ' году.'
    ]).where(student.c.kurs.in_((1,2,4)))

rp = connection.execute(s)
results = rp.fetchall()

results = [item[0][0:item[0].find(' родился в ')].upper() + item[0][item[0].find(' родился в '):] for item in results if item[0] is not None]
print('Задание 6 \n', results, '\n')


#Задание 7

s = select(['Код-' +
    cast(university.c.univ_id, String(20)) + '; ВГУ-г.' +
    cast(university.c.city, String(20)) + '; Рейтинг=' +
    cast(university.c.rating, String(20)) + '.'
    ])

rp = connection.execute(s)
print('Задание 7 \n', rp.fetchall(), '\n')


#Задание 8

s = select(['Код-' +
    cast(university.c.univ_id, String(20)) + '; ВГУ-г.' +
    cast(university.c.city, String(20)) + '; Рейтинг=' +
    cast(func.round(university.c.rating, -2), String(20)) + '.'
    ])

rp = connection.execute(s)
results = rp.fetchall()

results = [item[0][0:item[0].find('; Рейтинг=')+len('; Рейтинг=')] + str(round(float(item[0][item[0].find('; Рейтинг=')+len('; Рейтинг='):len(item[0])-1]), -2)) + '.' for item in results if item[0] is not None]
print('Задание 8 \n', results, '\n')


#Задание 9

s = select([
    func.count(exam_marks.c.student_id)
    ]).where(exam_marks.c.subj_id == 20 and exam_marks.c.mark > 2)

rp = connection.execute(s)
print('Задание 9 \n', rp.fetchall(), '\n')


#Задание 10

s = select([
    func.count(func.distinct(exam_marks.c.subj_id))
    ])

rp = connection.execute(s)
print('Задание 10 \n', rp.fetchall(), '\n')


#Задание 11

s = select([
    exam_marks.c.student_id,
    func.min(exam_marks.c.mark)
    ]).group_by(exam_marks.c.student_id)

rp = connection.execute(s)
print('Задание 11 \n', rp.fetchall(), '\n')


#Задание 12

s = select([
    exam_marks.c.student_id,
    func.max(exam_marks.c.mark)
    ]).group_by(exam_marks.c.student_id)

rp = connection.execute(s)
print('Задание 12 \n', rp.fetchall(), '\n')


#Задание 13

s = select([
    student.c.surname
    ]).where(student.c.surname.like('И%')).order_by(student.c.surname).limit(1)

rp = connection.execute(s)
print('Задание 13 \n', rp.fetchall(), '\n')


#Задание 14

s = select([
    subject.c.subj_name,
    func.max(subject.c.semester)
    ]).group_by(subject.c.subj_name)

rp = connection.execute(s)
print('Задание 14 \n', rp.fetchall(), '\n')


#Задание 15

s = select([
    func.strftime('%d.%m.%Y', exam_marks.c.exam_date),
    func.count(exam_marks.c.student_id)
    ]).group_by(exam_marks.c.exam_date)

rp = connection.execute(s)
print('Задание 15 \n', rp.fetchall(), '\n')


#Задание 16

joined_tables = student.join(exam_marks, student.c.student_id==exam_marks.c.student_id)
s = select([
    exam_marks.c.subj_id,
    student.c.kurs,
    func.avg(exam_marks.c.mark),
    ]).select_from(joined_tables).group_by(exam_marks.c.subj_id, student.c.kurs)

rp = connection.execute(s)
print('Задание 16 \n', rp.fetchall(), '\n')


#Задание 17

s = select([
    exam_marks.c.student_id,
    func.avg(exam_marks.c.mark)
    ]).group_by(exam_marks.c.student_id)

rp = connection.execute(s)
print('Задание 17 \n', rp.fetchall(), '\n')


#Задание 18

s = select([
    exam_marks.c.exam_id,
    func.avg(exam_marks.c.mark)
    ]).group_by(exam_marks.c.exam_id)

rp = connection.execute(s)
print('Задание 18 \n', rp.fetchall(), '\n')


#Задание 19

s = select([
    exam_marks.c.exam_id,
    func.count(exam_marks.c.student_id)
    ]).where(exam_marks.c.mark > 2).group_by(exam_marks.c.exam_id)

rp = connection.execute(s)
print('Задание 19 \n', rp.fetchall(), '\n')

#Задание 20

s = select([
    cast(((subject.c.semester + 1)/ 2 ), Integer).label("kurs"),
    func.count().label("Кол-во предметов")
    ]).group_by("kurs")

rp = connection.execute(s)
print('Задание 20 \n', rp.fetchall(), '\n')
