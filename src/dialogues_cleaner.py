import sqlite3
import glob

from typing import TextIO

import db_creator
import pdf_creator

DIALOGUES_PATH = "/home/anfi/Desktop/pathologic_stuff/pathologic1_dialogue_tree_extractor/dialogues_html/"

#find a line inside a text file
def	find_line(file: TextIO, pattern: str ) -> str:

	for line in file:
		if line.find(pattern) != -1:
			return (line)

#A personalized split to separate the dialogues without quotes and commas conflicts.
def	ft_split(dialogue: str) -> list[str]:
	dialogue_list: list[str] = []
	dialogue_len: int = len(dialogue)
	i: int = 0
	line_len: int

	while i < dialogue_len:
		if (dialogue[i] == '\'' or dialogue[i] == '\"'):
			quote = dialogue[i]
			line_len = 1
			while dialogue[i + line_len] != quote:
				line_len += 1
			dialogue_list.append(dialogue[(i+1):(i+line_len)])
			i += line_len
		i += 1
	return (dialogue_list)

#Cleans the long af line that contains all the dialogues inside an html file,
#returning a list separating each dialogue.
def	split_dialogue(file_name: str) -> list[str]:
	splitted_dialogue: list[str] = None

	with open(file_name) as file:
		dialogue = find_line(file, "textarr=[")
	dialogue = dialogue.removeprefix("                    textarr=[")
	dialogue = dialogue.removesuffix("];\n")

	splitted_dialogue = ft_split(dialogue)
	if (len(splitted_dialogue) == 0):
		return (None)
	return (splitted_dialogue)

#Cleans and splits the dialogues ids inside the html file
def	split_dialogue_ids(file_name: str) -> list[str]:

	with open(file_name) as file:
		dialogue_ids = find_line(file, "inarr=[")
		dialogue_ids = dialogue_ids.removeprefix("                    inarr=[")
		dialogue_ids = dialogue_ids.removesuffix("];\n")

	return (dialogue_ids.split(", "))


def	main_character_dialogues(filename_pattern: str, cursor: sqlite3.Cursor):

	files_en = glob.glob("%s/html_en/%s" %(DIALOGUES_PATH, filename_pattern))
	files_en.sort()
	files_ru = glob.glob("%s/html_ru/%s" %(DIALOGUES_PATH, filename_pattern))
	files_ru.sort()
	i = 0
	for current_file in files_en:
		print("current file = %s\n" %(current_file))
		dialogue_en = split_dialogue(current_file)
		dialogue_ru = split_dialogue(files_ru[i])
		dialogue_id = split_dialogue_ids(current_file)
		if (cursor is None):
			pdf_creator.write_dialogue(dialogue_en, dialogue_ru)
		else:
			db_creator.insert_dialogues(current_file, dialogue_id, dialogue_en, dialogue_ru, cursor)
		i += 1