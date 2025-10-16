import sqlite3
asmit= sqlite3.connect('grade distribution.db') #established connection with database...
#table='CREATE TABLE grade (id integer primary key, number integer, grade TEXT)'
cusor = asmit.cursor()
#cusor.execute(table)
#asmit.commit() 
#grade_system= [
    #(90,"A"),
    #(80,"B"),
   # (70,"C"),
   # (60,"D"),
   # (50,"E")
#] 
#insert= 'INSERT INTO grade(number,grade) VALUES(?,?)'
#cusor.executemany(insert, grade_system)
#asmit.commit()
select= 'SELECT * from grade '
for i in cusor.execute(select):
    print(i)

#cusor.execute('DELETE FROM grade')
#asmit.commit()
