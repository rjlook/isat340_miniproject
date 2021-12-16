import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "insert into members values (?,?,?,?,?,?)"
data = ((1, "Robert", "Look", 20, "lookrl@dukes.jmu.edu", "I am an ISAT student at James Madison University. I was born in San Jose, California. I like to fish, hunt, and hangout with friends."),
(2, "Lyle", "Rodgers", 21, "rodge2ld@dukes.jmu.edu", "I am an ISAT student at James Madison University. I am currently a junior that is concentrating in industrial and maufacturing systems. I enjoy being outdoors and hanging with friends and family."))
cursor.executemany(sql, data)

conn.commit()
conn.close()