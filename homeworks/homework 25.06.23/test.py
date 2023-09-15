import mysql.connector


con = mysql.connector.connect(
    host='localhost',
    user='Abuka',
    password='Takanashi_13',
    database='animals'
    )
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM cat")

    rows = cur.fetchall()

print(rows)