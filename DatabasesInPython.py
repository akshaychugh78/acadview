#Question 1

import pymysql as pm

try:
    con = pm.connect(host='localhost',database='book_info',user='root',password='1122')
    cur=con.cursor()
    
    query='create table Authors(author_id int(5) primary key, first_name varchar(10) not null, middle_name varchar(10), last_name varchar(10) not null)'
    cur.execute(query)
    
    query='create table ZipCodes(zip_code_id int(5) primary key, city varchar(10), state varchar(20), zip_code int(6))'
    cur.execute(query)
    
    query='create table Publishers(publisher_id int(5) primary key, name varchar(10), street_address varchar(20), suite_number int(10), zip_id int(10) not null)'
    cur.execute(query)
    
    query='create table Titles(title_id int(5) primary key, title varchar(15), iSBN int(10) not null , publisher_id int(5) not null, publication_year int(4))'
    cur.execute(query)

    query='create table Book(book_id int(5) primary key, title_id int(5) not null ,location varchar(30),genre varchar(30))'
    cur.execute(query) 

    query='create table AuthorsTitles(author_title_id int(5) primary key, author_id int(5), title_id int(5))'
    cur.execute(query)
    
    print("Tables created")

    con.commit()

except Exception as e:
    print("Error occured!!")
    if con: 
          con.rollback()
          print("Problem: ",e)
         
finally:
    cur.close()
    con.close()




#Q2.Insert values in the tables.

import pymysql as pm

try:
    con = pm.connect(host='localhost',database='book_info',user='root',password='1234')
    cur=con.cursor()
      
    query_mul = "insert into Authors values(%s,%s,%s,%s)"
    data = [(1,'Srinivasa','','Ramanujan'),
            (2,'S','','Hokking'),
            (3,'Tenali','','Raman')]
    cur.executemany(query_mul, data)

    query_mul = "insert into ZipCodes values(%s,%s,%s,%s)"
    data = [(1,'Faridabad','Haryana',121001),
            (2,'Rothak','Haryana',403001),
            (3,'Hisar','Haryana',560070)]
    cur.executemany(query_mul, data)

    query = "insert into Publishers values(1,'ManavRachna','abc',1122,1)"
    cur.execute(query)

    query = "insert into Titles values(1,'The Greatest Show Ever',771,1,2015)"
    cur.execute(query)

    query = "insert into Book values(1,1,'New Delhi','For ALL')"
    cur.execute(query)

    query = "insert into AuthorsTitles values(1,2,1)"
    cur.execute(query)
    
    print("Tables created")

    con.commit()

except Exception as e:
    print("Error occured!!")
    if con: 
          con.rollback()
          print("Problem: ",e)
         
finally:
    cur.close()
    con.close()

#Question 3
    
import pymysql as pm

try:
    con = pm.connect(host='localhost',database='book_info',user='root',password='1111')
    cur=con.cursor() 

    query_select = 'select * from Authors'
    cur.execute(query_select)
    
    data = cur.fetchall()
    for row in data:
        print("author_id: {}, first_name: {}, middle_name: {}, last_name: {} ".format(row[0],row[1],row[2],row[3]))

    #update
    query = "update Authors set first_name='Srinivasa' where author_id= 1 "
    cur.execute(query)

    print('#'*50)
    query_select = 'select * from Authors'
    cur.execute(query_select)
    
    data = cur.fetchall()
    for row in data:
        print("author_id: {}, first_name: {}, middle_name: {}, last_name: {} ".format(row[0],row[1],row[2],row[3])) 

    con.commit()

except Exception as e:
    print("Error occured!!")
    if con: 
          con.rollback()
          print("Problem: ",e)
         
finally:
    cur.close()
    con.close()
