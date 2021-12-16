import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into member_login values (?,?,?)"
data = ((1, "vato", "grandpapi"), (2, "lyguy", "cheeseball"))
cursor.executemany(sql,data)
conn.commit()
conn.close()

