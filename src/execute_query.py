import os
import sqlite3
import translation_program.db_functions as db
import readline

STD='\033[0m'
GRAY='\033[90m'
BLUE='\033[34m'
RED='\033[31m'

# SELECT id, conversation, healer FROM pathologic WHERE conversation LIKE '%_Danko_%'
# UPDATE pathologic SET healer='Daniil' WHERE conversation LIKE '%_Danko_%'


# SELECT id, conversation, healer FROM pathologic WHERE conversation NOT LIKE '%_Random_%' AND conversation NOT LIKE '%_Klara_%' AND conversation NOT LIKE '%_Burah_%' AND conversation NOT LIKE '%_Danko_%'

def	execute_query(connection: sqlite3.Connection):
	cursor: sqlite3.Cursor = connection.cursor()
	query: str = None
	query_results: list

	while True:
		query = input(f"{BLUE}Enter query (q to exit): {STD}")
		if (query == "q" or query == "Q"):
			break
		if (query == "commit"):
			connection.commit()
			continue
		query_results = db.try_execute_and_fetchall(cursor, query, None)
		if (not query_results):
			print("No results")
		else:
			for result in query_results:
				print(result)

# def	execute_query(connection: sqlite3.Connection, query: str) -> list:
# 	cursor: sqlite3.Cursor = connection.cursor()
# 	query_results: list

# 	query_results = db.try_execute_and_fetchall(cursor, query, None)
# 	return (query_results)