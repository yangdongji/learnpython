import hashlib
import unicodedata
import mysql.connector
from mysql.connector import errorcode


class MySQLDB:
    username = '数据库用户名'
    password = '数据库密码'
    database = '数据库名'
    host = 'localhost'  # 数据库主机地址
    connection = ''
    isconnect = True
    placeholder = '%s'

    def __init__(self):
        if self.isconnect:
            MySQLDB.connect(self)
            MySQLDB.initdb(self)

    def escape(self, string):
        return '`%s`' % string

    def connect(self):
        config = {
            'user': self.username,
            'password': self.password,
            'host': self.host
        }

        if self.database != None:
            config['database'] = self.database

        try:
            cnx = mysql.connector.connect(**config)
            self.connection = cnx
            return True
        except mysql.connector.Error as err:
            if (err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
                print "The credentials you provided are not correct."
            elif (err.errno == errorcode.ER_BAD_DB_ERROR):
                print "The database you provided does not exist."
            else:
                print "Something went wrong: ", err
            return False

    def initdb(self):
        if self.connection == '':
            print "Please connect first"
            return False
        cursor = self.connection.cursor()

        # 创建表的定义
        sql = 'CREATE TABLE IF NOT EXISTS \
        table_name ( \
        id VARCHAR(64) PRIMARY KEY, \
        url TEXT, \
        title TEXT, \
        type TEXT, \
        thumb TEXT, \
        count INTEGER, \
        images TEXT, \
        tags TEXT, \
        post_time DATETIME \
        ) ENGINE=INNODB DEFAULT CHARSET=UTF8'
        try:
            cursor.execute(sql)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print ("An error occured: {}".format(err))
            return False

    def cleardb(self):
        if self.connection == '':
            print "Please connect first"
            return False
        cursor = self.connection.cursor()
        sql = 'DROP TABLE IF EXISTS table_name'
        try:
            cursor.execute(sql)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print ("An error occured: {}".format(err))
            return False

    def insert(self, **values):
        if self.connection == '':
            print "Please connect first"
            return False
        cursor = self.connection.cursor()
        # 插入数据
        sql = "insert into table_name (id, url, title, type, thumb, count, temperature, images, tags, post_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update id=VALUES(id), url=VALUES(url), title=VALUES(title), type=VALUES(type), thumb=VALUES(thumb), count=VALUES(count), images=VALUES(images), tags=VALUES(tags), post_time=VALUES(post_time)"
        title = unicodedata.normalize('NFKD', values['title']).encode('ascii', 'ignore')
        images = ", ".join('%s' % k for k in values['images'])
        params = (
        hashlib.md5(title + images).hexdigest(), values['url'], values['title'], values['type'], values['thumb'],
        values['count'], images, '', values['date'])
        try:
            cursor.execute(sql, params)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print ("An error occured: {}".format(err))
            return False

    def replace(self, tablename=None, **values):
        if self.connection == '':
            print "Please connect first"
            return False

        tablename = self.escape(tablename)
        if values:
            _keys = ", ".join(self.escape(k) for k in values)
            _values = ", ".join([self.placeholder, ] * len(values))
            sql_query = "REPLACE INTO %s (%s) VALUES (%s)" % (tablename, _keys, _values)
        else:
            sql_query = "REPLACE INTO %s DEFAULT VALUES" % tablename

        cur = self.connection.cursor()
        try:
            if values:
                cur.execute(sql_query, list(itervalues(values)))
            else:
                cur.execute(sql_query)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print ("An error occured: {}".format(err))
            return False
