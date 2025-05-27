import sqlite3
import db_functions as db
import readline
import os

STD='\033[0m'
GRAY='\033[90m'
RED='\033[31m'
BLUE='\033[34m'
CYAN='\033[36m'
BBLUE='\033[44m'


class LineInfo:
	def __init__(self: "LineInfo"):
		self.id: tuple[int]
		self.english: tuple[str]
		self.russian: tuple[str]
		self.spanish: tuple[str]
		self.healer: tuple[str]
		self.character: tuple[str]




def	get_line_by_id(id: int, connection: sqlite3.Connection) -> LineInfo:

	cursor: sqlite3.Connection = connection.cursor()
	line_info: LineInfo = LineInfo()

	line_info.id  = db.try_execute_and_fetchone(cursor, "SELECT id FROM pathologic WHERE id=?", (id,))
	line_info.english = db.try_execute_and_fetchone(cursor, "SELECT english FROM pathologic WHERE id=?", (id,))
	line_info.russian = db.try_execute_and_fetchone(cursor, "SELECT russian FROM pathologic WHERE id=?", (id,))
	line_info.spanish = db.try_execute_and_fetchone(cursor, "SELECT spanish FROM pathologic WHERE id=?", (id,))
	line_info.healer = db.try_execute_and_fetchone(cursor, "SELECT healer FROM pathologic WHERE id=?", (id,))
	line_info.character = db.try_execute_and_fetchone(cursor, "SELECT character FROM pathologic WHERE id=?", (id,))

	cursor.close()
	return (line_info)



def	update_spanish_line(connection: sqlite3.Connection, line_info: LineInfo):

	cursor = connection.cursor()
	try:
		print(line_info.spanish)
		cursor.execute("UPDATE pathologic SET spanish=? WHERE id=?", (line_info.spanish[0] ,line_info.id[0]))
	except sqlite3.Error as e:
		print(e)

def	print_line(line_info: LineInfo):
	print(f"{BLUE}| {BBLUE} {line_info.id[0]}: {line_info.healer[0]} -> {line_info.character[0]}{STD}\n{BLUE}|")
	print("| En | %s" %(line_info.english[0]))
	print("| Ru | %s" %(line_info.russian[0]))
	print("| Sp | "+STD+"%s\n\n" %(line_info.spanish)[0])


def	ask_confirmation() -> str:
	user_input: str

	print("\nCommit this update? (y/n) ", end="")
	user_input = input()

	if (not user_input or "yYnN".find(user_input) == -1):
		print(RED+"Invalid input"+STD)
		return (ask_confirmation())
	return (user_input.upper())

def start_assisting(connection: sqlite3.Connection):
	line_info: LineInfo

	os.system("clear")
	current_line: int = db.get_last_translated_line()
	line_info = get_line_by_id(current_line, connection)
	print_line(line_info)
	line_info.spanish = tuple((input(">> "),))
	update_spanish_line(connection, line_info)

	os.system("clear")
	print_line(line_info)

	if (ask_confirmation() == "Y"):
		connection.commit()
	else:
		print("Making a rollback...")
		connection.rollback()
		line_info.spanish = db.try_execute_and_fetchone(connection.cursor(), "SELECT spanish FROM pathologic WHERE id=?", line_info.id)

	print_line(line_info)



	db.set_last_translated_line(current_line)