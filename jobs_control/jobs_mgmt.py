import pymysql, flask_server
from db_model.mysql import conn_mysqldb

# cursor = conn_mysqldb.cursor()

# table name : my_jobs
# id(primary key)auto_increment, company, title, location, link

# sql_table = """
#     create table my_jobs (
# 	  id int unsigned not null auto_increment,
#     company varchar(50) not null,
#     title varchar(50) not null,
#     location varchar(50) not null,
#     link varchar(200) not null,
#     primary key(id)
#     );
# """
