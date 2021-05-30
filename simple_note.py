import argparse
import datetime
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument("-s", help="show notes", action="store_true")
parser.add_argument("-n", help="add note", type=str)
parser.add_argument('-d', help="delete index", type=int)
parser.add_argument('-f', help="find note that starts with or contains", type=str)
args = parser.parse_args()
db_file = "./noter.json"
now = str(datetime.datetime.now())

if not os.path.exists(db_file):
	with open(db_file, 'w') as o:
		print(f'Creating database in "{db_file}" ... ')
		data = { 
		"notes": [],
		"last_updated": now
		}
		json.dump(data, o)
		print('Databse created. You are ready to add notes.')


if args.n:
	with open(db_file, 'r') as f:

		data = json.load(f)
		data["notes"].append({
			"note": args.n,
			"date": now
			}
		)
		data["last_updated"] = now
		
		with open(db_file, 'w') as o:
			json.dump(data, o)
			print('\n', '-'*20, '\n')
			print('Note added:', args.n)
			print('\n', '-'*20, '\n')

if args.s:
	with open(db_file, 'r') as f:
		data = json.load(f)
		
		for idx, note_data in enumerate(data['notes']):
			print(f"{'-'*20}'\n'{note_data['note']}'\n\n'{note_data['date']}")
			print(f'ID: {idx}\n')

if args.d:
	with open(db_file, 'r') as f:
		

		try:
			data = json.load(f)
			deleted_note = data["notes"].pop(args.d)["note"]
			
			with open(db_file, 'w') as o:
				json.dump(data, o)
				print('\n', '-'*20, '\n')
				print('Note delted:', deleted_note)
				print('\n', '-'*20, '\n')
		
		except Exception as e:
			print(e)

if args.f:
	with open(db_file, 'r') as f:
		data = json.load(f)
		filtered = filter(lambda x: args.f in x["note"], data["notes"])
		filtered = list(filtered)
		print(f"{len(filtered)} results found: \n\n")
		
		for idx, note_data in enumerate(filtered):
			print(f"{'-'*20}\n{note_data['note']}\n\n{note_data['date']}")
			print(f'ID: {idx}\n')
