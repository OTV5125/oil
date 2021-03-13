import json;
import pymysql
import pymysql.cursors

class Mysql:
   def connect(self):
      f = open('config.json', 'r')
      config = json.loads(f.read())
      if config["Mysql"] is None:
         print('config mysql not found in config.json')
      else:
         mysql=config["Mysql"]

      self.con = pymysql.connect(host=mysql["host"],
         user=mysql["user"],
         password=mysql["password"],
         db=mysql["db"],
         charset=mysql["charset"],
         cursorclass=pymysql.cursors.DictCursor
      )

   def getCars(self):
      self.connect()
      try:
         with self.con.cursor() as cur:
            cur.execute('SELECT id, name, comsumption FROM car')
            rows = cur.fetchall()
            return rows
      finally:
         self.con.close()

   def getRoute(self):
      self.connect()
      try:
         with self.con.cursor() as cur:
            cur.execute('SELECT id, name, distantion FROM route')
            rows = cur.fetchall()
            return rows
      finally:
         self.con.close()

   def getCarById(self, id):
      self.connect()
      try:
         with self.con.cursor() as cur:
            cur.execute('SELECT id, name, comsumption FROM car WHERE id=%s', id)
            row = cur.fetchone()
            return row
      finally:
         self.con.close()

   def getRouteById(self, id):
      self.connect()
      try:
         with self.con.cursor() as cur:
            cur.execute('SELECT id, name, distantion FROM route WHERE id=%s', id)
            row = cur.fetchone()
            return row
      finally:
         self.con.close()

