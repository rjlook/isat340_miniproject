import sqlite3
conn = sqlite3.connect("celebrities.db") 
cursor = conn.cursor()
sql = "insert into celebs values(?,?,?,?,?,?,?)"
data = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg", "An American actress and filmmaker. She has won many Academy Awards and three Golden Globe Awards."),
(2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg", "An American Actress and film producer. He has won multiple awards incuding a British Academy Film Award and two Global Globe Awards to name a few."),
(3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg", "She is a Princess in many Disney films. Her skin was as white as snow, her lips as red as the rose, and her hair was as black as ebony wood."),
(4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg", "He is a Jedi Knight and was seduced by the dark side of the Force. He began a Sith Lord and led the Empire's eradiction of the Jedi Order."),
(5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg", "She is an American singer-songwriter. She sings many popular country and pop music songs."),
(6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg", "She is an American singer, songwriter, and actress. She rose her fame as the lead singer of Destiny's Child, one of the best girl groups of all time."),
(7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg", "She is an American singer, actress, and producer. She began her acting career on the children's TV series Barney & Friends."),
(8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg", "He is an American professional Basketball player for the Golden State Warriors. He plays point guard position, and is widely known as one of the best."))
cursor.executemany(sql, data)
conn.commit()
conn.close()
