#! python 3
# youtubehaiku.py
# gets links to youtube haiku

import praw
import webbrowser


my_user_agent = 'youtubeHaikuGetLinks'
my_client_id = '4C0PjNu3i98OfA'
my_client_secret = 'AbpDpvUY_XJqobvCj-31BRb3xFw'

reddit = praw.Reddit(user_agent=my_user_agent, client_id=my_client_id, client_secret=my_client_secret)

for submissions in reddit.subreddit('youtubehaiku').hot(limit=27):
	links = str(submissions.url)
	if "www.reddit.com" in links:
		continue
	webbrowser.open_new_tab(links)

