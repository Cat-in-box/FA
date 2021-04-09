import warnings
warnings.filterwarnings("ignore")

from sqlalchemy import MetaData, Table, create_engine, select
metadata = MetaData()
engine = create_engine('sqlite:///BD_Primer_SQLite.db')

connection = engine.connect()

metadata.reflect(bind=engine)
lst1 = list(metadata.tables.keys())

tables = []
for table in metadata.tables.keys():
    tables.append(metadata.tables[table])

exam_marks, lectures, student, subj_lect, subject, university = tables

s = select([student])
print('1\n', engine.execute(s).fetchall())

s = select([student]).where(student.c.CITY == "Орел")
print('2\n', engine.execute(s).fetchall())

s=select([student]).where(student.c.CITY == (select([university.c.CITY]).where(university.c.CITY==student.c.CITY)))
print('3\n', engine.execute(s).fetchall())


from sqlalchemy import ForeignKeyConstraint

student.append_constraint(
    ForeignKeyConstraint(['UNIV_ID'], ['university.UNIV_ID'])
)

s = select([student]).select_from(university.join(student))
s = s.where(student.c.CITY == university.c.CITY)

print('4.1\n', engine.execute(s).fetchall())

join_expr = student.join(university)
s = select([join_expr]).where(student.c.CITY == university.c.CITY)

print('4.2\n', engine.execute(s).fetchall())


exam_marks.append_constraint(
    ForeignKeyConstraint(['STUDENT_ID'], ['student.STUDENT_ID'])
)
exam_marks.append_constraint(
    ForeignKeyConstraint(['SUBJ_ID'], ['subject.SUBJ_ID'])
)

"Вариант через функцию"
def FK(table, table1, column):
    table.append_constraint(
        ForeignKeyConstraint([column.upper()], [str(table1)+'.'+column.upper()])
)

s = select([subject.c.SUBJ_NAME, student.c.SURNAME, exam_marks.c.MARK]).select_from(student.join(exam_marks).join(subject))
s = s.where(exam_marks.c.MARK == 5)

print('5.1\n', engine.execute(s).fetchall())

join_expr = student.join(exam_marks).join(subject)
s = select([join_expr]).where(exam_marks.c.MARK == 5)

print('5.2\n', engine.execute(s).fetchall())