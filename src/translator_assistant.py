import sqlite3
import db_functions as db
import readline
import os

import utils.colors as color
import classes.LineInfo as LineInfo
import line_printers
from pynput import keyboard

CURRENT=2
#527567
def	get_line_by_id(id: int, connection: sqlite3.Connection) -> LineInfo:

	cursor: sqlite3.Connection = connection.cursor()
	line_info: LineInfo.LineInfo = LineInfo.LineInfo()

	line_info.id  = db.try_execute_and_fetchone(cursor, "SELECT id FROM pathologic WHERE id=?", (id,))
	if (not line_info.id[0]): #For the empty dialogues that have not been uploaded to the db
		cursor.execute("INSERT INTO pathologic (id) VALUES (?)", (id,))
		connection.commit()
		line_info.id  = db.try_execute_and_fetchone(cursor, "SELECT id FROM pathologic WHERE id=?", (id,))
	line_info.english = db.try_execute_and_fetchone(cursor, "SELECT english FROM pathologic WHERE id=?", (id,))
	line_info.russian = db.try_execute_and_fetchone(cursor, "SELECT russian FROM pathologic WHERE id=?", (id,))
	line_info.spanish = db.try_execute_and_fetchone(cursor, "SELECT spanish FROM pathologic WHERE id=?", (id,))
	line_info.healer = db.try_execute_and_fetchone(cursor, "SELECT healer FROM pathologic WHERE id=?", (id,))
	line_info.character = db.try_execute_and_fetchone(cursor, "SELECT character FROM pathologic WHERE id=?", (id,))
	cursor.close()
	return (line_info)

def	update_spanish_line(connection: sqlite3.Connection, line_info: LineInfo.LineInfo):

	cursor = connection.cursor()
	try:
		print(line_info.spanish)
		cursor.execute("UPDATE pathologic SET spanish=? WHERE id=?", (line_info.spanish[0] ,line_info.id[0]))
	except sqlite3.Error as e:
		print(e)


def	ask_confirmation() -> str:
	user_input: str

	print("\nCommit this update? (y/n) ", end="")
	user_input = input()

	if (not user_input or "yYnN".find(user_input) == -1):
		print(color.RED+"Invalid input"+color.STD)
		return (ask_confirmation())
	return (user_input.upper())


NOT_ACTIVATED=0
CTRL_LEFT=-1
CTRL_RIGHT=1

LINE_COMMITED=1
EXIT=-2

hotkey_activated: int = NOT_ACTIVATED
ctrl_pressed: bool = False


def	ft_on_press(key: keyboard.Key):
	global ctrl_pressed
	global hotkey_activated
	if key == keyboard.Key.ctrl:
		ctrl_pressed = True
	elif (ctrl_pressed == True):
		if key == keyboard.Key.left:
			hotkey_activated = CTRL_LEFT
			keyboard_ = keyboard.Controller()
			keyboard_.type("\n")
		if key == keyboard.Key.right:
			hotkey_activated = CTRL_RIGHT
			keyboard_ = keyboard.Controller()
			keyboard_.type("\n")
def	ft_on_release(key: keyboard.Key):
	global ctrl_pressed
	global hotkey_activated
	if (key == keyboard.Key.ctrl):
		ctrl_pressed = False
		hotkey_activated = NOT_ACTIVATED
	elif ((key == keyboard.Key.left or key == keyboard.Key.right) and hotkey_activated != NOT_ACTIVATED):
		hotkey_activated = NOT_ACTIVATED

def	translate_line(connection: sqlite3.Connection, current_line: int) -> int:
	line_info: list[LineInfo.LineInfo] = [None] * 5

	os.system("clear")

	line_info[0] = get_line_by_id(current_line - 2, connection)
	line_info[1] = get_line_by_id(current_line - 1, connection)
	line_info[CURRENT] = get_line_by_id(current_line, connection)
	line_info[3] = get_line_by_id(current_line + 1, connection)
	line_info[4] = get_line_by_id(current_line + 2, connection)

	line_printers.print_lines(line_info)
	with keyboard.Listener(on_press=ft_on_press, on_release=ft_on_release) as listener:
		line_info[CURRENT].spanish = tuple((input(">> "),))

	print(hotkey_activated)
	print(ctrl_pressed)
	if (hotkey_activated != NOT_ACTIVATED):
		return (hotkey_activated)
	if (line_info[CURRENT].spanish[0] == "q"):
		return (EXIT)

	update_spanish_line(connection, line_info[CURRENT])

	os.system("clear")
	line_printers.print_line(line_info[CURRENT], CURRENT)
	if (ask_confirmation() == "Y"):
		connection.commit()
		return 1
	else:
		print("Making a rollback...")
		connection.rollback()
		line_info[CURRENT].spanish = db.try_execute_and_fetchone(connection.cursor(), "SELECT spanish FROM pathologic WHERE id=?", line_info[CURRENT].id)
		return 0


# 527581 -> current first line id, until program isnt fully functional further updates will
# need to be revised.
def start_assisting(connection: sqlite3.Connection):
	translate_line_result: int

	while True:
		current_line: int = db.get_last_translated_line()
		translate_line_result = translate_line(connection, current_line)
		if (translate_line_result == CTRL_RIGHT or translate_line_result == LINE_COMMITED):
			db.set_last_translated_line(current_line + 1)
		elif (translate_line_result == CTRL_LEFT):
			db.set_last_translated_line(current_line - 1)
		elif (translate_line_result == -2): #EXIT CASE, NOT DONE YET
			return
