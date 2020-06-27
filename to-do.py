# Imports

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

# Database Creation
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, )
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Main Program
while True:
    print('''1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit''')
    menu = int(input())
    if menu == 0:
        print('Bye!')
        break
    if menu == 1:
        today = datetime.today()
        print('Today', today.strftime('%d'), today.strftime('%b'), ':')
        query = session.query(Table).filter(Table.deadline == today).all()
        if not query:
            print('Nothing to do!')
            continue
        print(query)
        continue
    if menu ==2:
        now = datetime.today()
        year = int(now.strftime("%Y"))
        month = int(now.strftime("%m"))
        day = int(now.strftime("%d")) - 1
        for i in range (1,8):
            if month in {1, 3, 5, 7, 8, 10, 12}:
                if day + 1 > 31:
                    month = month + 1
                    day = day + 1 - 31
                else:
                    day = day + 1
            else:
                if day + 1 > 30:
                    month = month + 1
                    day = day + 1 - 30
                else:
                    day = day + 1
            range = date(year, month, day)
            query = session.query(Table).filter(Table.deadline == range).all()
            print()
            print(range.strftime('%A'), range.strftime('%d'), range.strftime('%b'), ':')
            if not query:
                print('Nothing to do!')
                continue
            print(query)
        print()
        continue
    if menu == 3:
        rows = session.query(Table).all()
        for i in rows:
            print(i.deadline)
            print(i.task)
    if menu == 4:
        print()
        print('Missed tasks:')
        num = 0
        rows = session.query(Table).filter(Table.deadline < datetime.today()).all()
        if not rows:
            print('Nothing is missed!')
        for row in rows:
            da = (row.deadline).strftime('%d')
            mo = (row.deadline).strftime('%b')
            print(num+1, ')', row, da, mo)
            num = num + 1
        print()
    if menu == 5:
        a = input('Enter task')
        b = input('Enter deadline')
        c, d, e  = day = map(int, b.split('-'))
        dater = date(c, d, e)
        new_row = Table(task=a, deadline = dater)
        session.add(new_row)
        session.commit()
        print('The task has been added!')
        continue
    if menu == 6:
        num = 0
        print('Chose the number of the task you want to delete:')
        rows = session.query(Table).all()
        for row in rows:
            da = (row.deadline).strftime('%d')
            mo = (row.deadline).strftime('%b')
            print(num + 1, '.', row, da, mo)
            num = num + 1
        choice = int(input())
        srow = rows[choice+1]
        session.delete(srow)
        session.commit()
        print('The task has been deleted!')

