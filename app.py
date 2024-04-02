import praw
import time

#this needs to be filled out with account details
reddit = praw.Reddit(client_id='', client_secret="",
                     password='', user_agent='',
                     username='')
subreddit_name = "" #the subreddit you want to post to


#read the text file with youtube links
links = []
f = open("videos.txt", "r", encoding = "utf-8")
line1 = ""
for line in f.readlines():
    line = line.rstrip()
    if line1 == "":
        line1 = line
    else:
        links.append((line1, line))
        line1 = ""
f.close()

delay = 12*60*60     # 12h time delay

# post on reddit
for link in links:
    reddit.subreddit(subreddit_name).submit(link[0], url=link[1])
    print("posted")
    if delay >= 16*60:
        print("Next post in " + str(delay/60) + " minutes.")
        time.sleep(delay)
        delay = delay / 2
    else:
        print("Next post in " + str(delay/60) + " minutes.")
        time.sleep(16*60)
