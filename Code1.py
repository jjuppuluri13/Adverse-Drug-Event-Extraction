#import csv
import psycopg2

conn = psycopg2.connect("dbname=AE_Positive user=postgres password=Mypostgresql#1a")
cur = conn.cursor()

import string
exclude = set(string.punctuation)
cur.execute("UPDATE pos_table SET sentence = ''.join(ch for ch in sentence if ch not in exclude;")

conn.commit()

#pos_table = csv.reader(open('AE_Pos1.csv'), delimiter = ',', quotechar='"')
#for row in pos_table:
#       cur.execute(
#               "INSERT INTO pos_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
#               row
#           )

#conn.commit()






