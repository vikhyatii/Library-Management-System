print("*****LIBRARY MANAGEMENT SYSTEM*****")
#creating database
import mysql.connector
dbs=mysql.connector.connect(host="localhost",user="root",password="Vikh1234",auth_plugin='mysql_native_password')
cur=dbs.cursor()
cur.execute("create database if not exists lib")
cur.execute("use lib")
#creating required tables
cur.execute("create table if not exists books(bname varchar(30),bcode varchar(20),total int,subject varchar(20))")
cur.execute("create table if not exists issue(stname varchar(30),stid varchar(20),bcode varchar(20),issue varchar(30))")
cur.execute("create table if not exists submit(stname varchar(30),stid varchar(20),bcode varchar(20),submit varchar(30))")
dbs.commit()
while True:
    print("""
1- Add book
2- Issue book
3- Return book
4- Delete book
5- Display all books
""")
    ch=int(input("Enter choice:"))
    if ch==1:
        bn=input("Enter book name:")
        bc=input("Enter book code:")
        total=int(input("Enter total books:"))
        sub=input("Enter subject:")
        cur.execute("insert into books values('"+bn+"','"+bc+"',"+str(total)+",'"+sub+"')")
        dbs.commit()
        print("Book added successfully")
    if ch==2:
        n=input("Enter name of student:")
        ide=input("Enter student id:")
        bcd=input("Enter book code:")
        d=input("Enter issue date:")
        cur.execute("insert into issue values('"+n+"','"+ide+"','"+bcd+"','"+d+"')")
        cur.execute('update books set total=total-1 where bcode="'+str(bcd)+'"')
        dbs.commit()
        print("Book issued to:",n)
    if ch==3:
        n=input("Enter name of student:")
        ide=input("Enter student id:")
        bcd=input("Enter book code:")
        d=input("Enter return date:")
        cur.execute("insert into issue values('"+n+"','"+ide+"','"+bcd+"','"+d+"')")
        cur.execute('update books set total=total+1 where bcode="'+str(bcd)+'"')
        dbs.commit()
        print("Book submitted from:",n)
    if ch==4:
        cod=input('enter book code to be deleted from record:')
        cur.execute('delete from books where bcode="'+str(cod)+'"')
        dbs.commit()
        print('RECORD SUCCESSFULLY DELETED')
    if ch==5:
        cur.execute("select * from books")
        for i in cur:
            print(i)
        dbs.commit()





    
        
        

    

    
    



