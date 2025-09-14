import sqlite3

import utils.colors as color
import translation_program.db_functions as db

def	print_total_translated_lines(connection: sqlite3.Connection):
	today_lines: tuple
	total_lines: tuple

	today_lines = db.try_execute_and_fetchone(connection.cursor(), "SELECT SUM(lines) FROM lines_per_day WHERE date IS CURRENT_DATE", None)
	total_lines = db.try_execute_and_fetchone(connection.cursor(), "SELECT COUNT(id) FROM pathologic WHERE spanish IS NOT NULL", None)
	print(f"{color.BLUE}")
	print(f"TOTAL LINES TRANSLATED TODAY: {today_lines[0]} / {total_lines[0]}")
	if (today_lines[0] < 5):
		print("Not even half way there, keep translating!! ^u^")
	elif (today_lines[0] < 8):
		print("Almost there! keep going! =owo=")
	elif (today_lines[0] < 10):
		print("SO CLOSE!!! one last effort! uwu <3")
	elif (today_lines[0] < 20):
		print("WELL DONE!!! *.· ¨,*·. .*")
	else:
		print("WOAH THERE, take a rest, you made the work of two days! *o*")
	print(f"{color.STD}")



def	update_lines_per_day(connection: sqlite3.Connection, total_lines_translated: int):

	db.try_execute_and_fetchone(connection.cursor(),"INSERT INTO lines_per_day (lines) VALUES (?)", (total_lines_translated,))
	connection.commit()