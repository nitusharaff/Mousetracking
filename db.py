import MySQLdb
con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root",db="interview")
con.autocommit(True)
cur = con.cursor()

# Use all the SQL you like
#cur.execute("CREATE TABLE question( ques_id varchar(100),ques_type varchar(100),ques varchar(150))")

d= cur.execute( "INSERT INTO subject(name,matric,intw_num,intw_date,logfile) VALUES('abc','n15000044',1,'2017-04-13 09:59:05.051000','n15000044.txt');")
if(d==True):
    print "success"