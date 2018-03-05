from steem import Steem
from steem.account import Account
from steem.post import Post
from steem.steem import Commit
import sys
import os
import json
import time
import operator





accountName="account name" #this is your Steemit account name without the '@'
key="steemit key here" #you can use your steemit posting key here
keyWord="ketchup" #this is the word the bot looks for to upvote the post
votePercentage=10 #this can range from 1 to 100

s = Steem(nodes=["https://rpc.buildteam.io", "https://gtg.steem.house:8090", "https://seed.bitcoiner.me"], wif=key)
t = Commit(steemd_instance=s, keys=key)

print('start')
scanned=0
while(1):
    time.sleep(5)
    print("True Start")
    try:
        for p in s.stream_comments():
            print(scanned)
            scanned=scanned+1

            lowerClean = p.body.lower()
            stringForTest=lowerClean.split()

            if keyWord in stringForTest and len(stringForTest)>150:
                if p.is_main_post():
                    identID='@' + p.author + '/' + p.permlink
                    t.vote(identID, 10 , account=accountName)

                    t.post('Title of Post', "Reply Body Here", accountName, reply_identifier='@' + p.author + '/' + p.permlink)
                    #The 'Title of Post' can be anything since it does not show up when replying. You can leave that as is. The 'Reply Body Here' is the actual reply message that will show up on teh post you upvoted with the bot.

                    time.sleep(20)


    except Exception as e:
        print(e)
        print("There was an error.")
