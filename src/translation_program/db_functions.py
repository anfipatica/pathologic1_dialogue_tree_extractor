import sqlite3

STD='\033[0m'
RED='\033[31m'

DB_PATH = "./database/patho.db"
LAST_TRANSLATED_LINE_PATH = "./database/.last_translated_line.txt"
def	create_connection() -> sqlite3.Connection:
	connection = sqlite3.connect(DB_PATH)
	# cursor = connection.cursor()
	# print(cursor)
	# try:
	# 	cursor.execute(
	# 		"CREATE TABLE pathologic(" \
	# 		"id INT PRIMARY KEY," \
	# 		"conversation TEXT,"\
	# 		"english TEXT," \
	# 		"russian TEXT," \
	# 		"spanish TEXT)")
	# except sqlite3.Error as e:
	# 	print(e)

	return (connection)

#CREATE TABLE lines_per_day(id INT PRIMARY KEY, date DATE DEFAULT CURRENT_DATE, lines INT)

def	get_last_translated_line() -> int:
	'''
	This function RETURNS the index of the last translated line saved in a hidden file
	'''
	last_line_id: int

	with open(LAST_TRANSLATED_LINE_PATH) as file:
		last_line_id = int(file.read())
	return(last_line_id)


def	set_last_translated_line(last_line_id: int):
	'''
	This function REWRITES the index of the last translated line saved in a hidden file
	'''
	with open(LAST_TRANSLATED_LINE_PATH, "w") as file:
		file.write(str(last_line_id))


def	try_execute_and_fetchone(cursor: sqlite3.Cursor, query: str, parameter: tuple) -> tuple:
	query_result: tuple

	if (parameter == None):
		try:
			cursor.execute(query)
		except sqlite3.Error as e:
			print(e)
			return ((None,))
	else :
		try:
			cursor.execute(query, parameter)
		except sqlite3.Error as e:
			print(e)
			return ((None,))
	query_result = cursor.fetchone()
	if (not query_result):
		return ((None,))
	return (query_result)


def	try_execute_and_fetchall(cursor: sqlite3.Cursor, query: str, parameter: tuple) -> list:

	if (not parameter):
		try:
			cursor.execute(query)
		except sqlite3.Error as e:
			print(f"{RED}{e}{STD}")
			return(None)
	else:
		try:
			cursor.execute(query, parameter)
		except sqlite3.Error as e:
			print(f"{RED}{e}{STD}")
			return(None)
	return(cursor.fetchall())