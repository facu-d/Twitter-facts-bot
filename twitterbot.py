import sqlite3
from sqlite3 import Error
from datetime import date
import tweepy
import time
import schedule

def sql_connect():
    try:
        conn = sqlite3.connect('factsdb.db')
        print ("DB CONNECTED")
        return conn 
    except Error:
        print (Error)

def sql_create_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("CREATE TABLE facts(id integer PRIMARY KEY, fact text, uploadDate text)")
    print ("Table FACTS created")
    conn.commit()


def update_fact(factid):
    conn = sql_connect()
    today = date.today()
    fecha = today.strftime("%d/%m/%Y")
    cursorObj = conn.cursor()
    cursorObj.execute('UPDATE facts SET uploadDate =:fecha where id =:id', {"fecha": fecha, "id":factid})
    print ("Fact ID: " + str(factid) + " updated")
    conn.commit()

def publish_tweet(factid, fact):
    api.update_status("[BOT] " + fact)
    print ("Fact ID:" + str(factid) + " uploaded")
    update_fact(factid)

def read_fact(conn):
    null = "-"
    cursorObj = conn.cursor()
    print ("Fetching fact...")
    for row in cursorObj.execute('SELECT * FROM facts where uploadDate =:null LIMIT 1', {"null": null}):
        factid = row[0]
        fact = row[1]
        publish_tweet(factid, fact)


conn = sql_connect()

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
# Create API object
api = tweepy.API(auth)

schedule.every(36).hours.do(read_fact, conn)

while True:
    schedule.run_pending()
    time.sleep(1)

