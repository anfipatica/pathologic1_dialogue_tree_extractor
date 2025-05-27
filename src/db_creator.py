import main
import sqlite3

from dialogues_cleaner import main_character_dialogues

def	insert_dialogues(conversation: str, id_list: list[str], english: list[str],
					 russian: list[str], cursor: sqlite3.Cursor):
	i: int = 0

	if (not english or len(english) == 0):
		return
	for id in id_list:
		try:
			cursor.execute("""
				 INSERT INTO pathologic (id, conversation, english, russian) 
				 VALUES (?, ?, ?, ?)
				 """, (int(id), conversation, english[i], russian[i]))
		except sqlite3.Error as e:
			print(e)
		i += 1
	cursor.connection.commit()
	query_result = cursor.execute("SELECT id, english FROM pathologic")

def	create_db(cursor: sqlite3.Cursor):
	main_character_dialogues("NPC_Danko_*.html", cursor)
	main_character_dialogues("NPC_Burah_*.html", cursor)
	main_character_dialogues("NPC_Klara_*.html", cursor)
	main_character_dialogues("NPC_Random_*.html", cursor)
	print("done")