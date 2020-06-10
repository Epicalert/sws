import MySQLdb
import sys

import surveys

if len(sys.argv) < 2:
    print("You must specify a survey!")
    quit()

survey = surveys.parse_survey(sys.argv[1])
db = MySQLdb.connect("localhost","daevsan","peepeepoopoo","sws")
c = db.cursor()

sql_query = "CREATE TABLE %s (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT" % sys.argv[1]

#SQL datatypes for each form type
types = {
        "radio":"VARCHAR(32)",
        "text":"VARCHAR(512)",
        "number":"INT",
        "time":"VARCHAR(5)"
        }
        

for item in survey:
    if item[0][0] != "_":
        sql_query += ",%s %s" % (item[0], types[item[1]])

sql_query += ");"

print("Executing query %s" % sql_query)
c.execute(sql_query)
