
from operator import itemgetter
import requests
import json

#Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Explore the structure of the data
submission_ids = r.json()
submission_dicts = []

print(submission_ids[:30])

for submission_id in submission_ids[:30]:
	#Make a separate API call for each submission
	url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	#Build a dictionary for each article

	try:
		comentario = response_dict['descendants']
		titulo = response_dict['title']

	except KeyError:
		print(f"This is not working out: {submission_id}")

	else:
		submission_dict = {
			"title": titulo,
			"hn_link": f"https://news.ycombinator.com/item?id={submission_id}", 
			"comments": comentario, #response_dict['descendants'],
		}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments'),
		reverse = True)

for submission_dict in submission_dicts:
	print(f"\nTitle: {submission_dict['title']}")
	print(f"Discussion link: {submission_dict['hn_link']}")
	print(f"Comments: {submission_dict['comments']}")