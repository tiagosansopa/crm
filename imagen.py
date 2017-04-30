
import psycopg2
conn_string = "host='localhost' dbname='imagen' user='uim' password='jkl'"
conn = psycopg2.connect(conn_string)
mypic=open('c:/Users/Pablo/Pictures/sun.jpg','rb').read()
cursor = conn.cursor()
cursor.execute("INSERT INTO phonebook(lastname,c2image) VALUES (%s,%s);", ('MyPICTURENAME', psycopg2.Binary(mypic)))
conn.commit()
cursor = conn.cursor()
cursor.execute("SELECT (c2image) FROM phonebook WHERE lastname='MyPICTURENAME';")
print ("HI")
mypic2 = cursor.fetchone()
print(str(mypic2[0]))
open('c:/Users/Pablo/Desktop/UVG/4to. 1er Semestre/Base de Datos/Proyecto 2/copyofsun.jpg', 'wb').write(str(mypic2[0]))
cursor.close()
conn.close()