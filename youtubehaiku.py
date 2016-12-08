#! python 3
# youtubehaiku.py
# gets links to youtube haiku

import praw
import webbrowser
import os


my_user_agent = ''
my_client_id = ''
my_client_secret = ''
links =[]


reddit = praw.Reddit(user_agent=my_user_agent, client_id=my_client_id, client_secret=my_client_secret)


#Gets submissions from reddit
for submissions in reddit.subreddit('youtubehaiku').hot(limit=27):
	new_link = str(submissions.url)
	if "www.reddit.com" in new_link:
		continue
	links.append(new_link)

#Open file for reading and gets the list of links from the file
read_file = open("seen.txt","r+")
check_lines = read_file.readlines()
stripped_lines = [i.strip() for i in check_lines]

#if check_lines is empty (file is empty), then open all the links & write the links to the file
if not check_lines:
	print('No old links detected, opening all links')
	for link in links:
		read_file.write(link+'\n')
		webbrowser.open(link)
	read_file.close
else:
#if file is not empty, then compare the links from the list and new links from reddit and open the new ones
	print('Opening new links')
	unique_links = set(links + stripped_lines)
	compared_links = set(unique_links).difference(stripped_lines)
	write_file =open("seen.txt","a")
	for link in compared_links:
		webbrowser.open(link)
		write_file.write(link+'\n')
	read_file.close
	
input('Done, press Enter to exit')

	




