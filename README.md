# Twitter facts bot

A twitter bot that every 36 hours reads a Sqlite DB and select one random fact and finally it uploads to your Twitter Account. It is made with Python, Sqlite, Tweeppy and Schedule.

## Prerequisits 📋
_You will need two libraries that we will install with PIP_
```
pip install tweepy
pip install schedule
```

## Setup 🔧
You need to edit your _Twitter API keys_ on lines __50__ and __51__
```
auth = tweepy.OAuthHandler("XXXXXXXX", "XXXXXXXX")
auth.set_access_token("XXXXXXXX", "XXXXXXXX")
```

## Customize ⌨️
You can put whatever you want in your DB and it will do the same thing. I upload the facts to the database with SQLiteDatabaseBrowser using a CVS file.
