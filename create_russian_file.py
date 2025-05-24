from typing import TextIO
import glob

FILE = "dialogues_db.txt"
SEPARATOR = "------------------------------------------------------------"

def	find_line(file: TextIO, pattern: str ) -> str:

	for line in file:
		if line.find(pattern) != -1:
			return (line)

def	split_dialogues(dialogue: str) -> list[str]:
	dialogue_list: list[str] = []
	dialogue_len = len(dialogue)
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

def	fix_dialogue(dialogue: str, dialogue_ids: str) -> list[str]:

	i = 0

	dialogue = dialogue.removeprefix("                    textarr=[")
	dialogue = dialogue.removesuffix("];\n")
	fixed_dialogue = split_dialogues(dialogue)

	if (len(fixed_dialogue) == 0):
		return (None)

	dialogue_ids = dialogue_ids.removeprefix("                    inarr=[")
	dialogue_ids = dialogue_ids.removesuffix("];\n")
	dialogue_ids = dialogue_ids.split(", ")

	for id in dialogue_ids :
		fixed_dialogue[i] = id+" | "+fixed_dialogue[i]
		i += 1
	return (fixed_dialogue)

def	get_whole_line(dialogue: list[str], i: int):
	if i + 1 >= len(dialogue):
		return
	index = dialogue[i + 1].find(":")
	while (i + 1 < len(dialogue) and (index == -1 or index > 28)):
		dialogue[i] = dialogue[i] + ' ' + dialogue[i + 1]
		dialogue.pop(i + 1)
		index = dialogue[i + 1].find(":")

def	write_dialogue(dialogue_en: list[str], dialogue_ru: list[str]):

	i = 0
	if (dialogue_en == None):
		print("  ↳ No dialogues found in this file\n")
		return
	
	with open(FILE, "a") as file:
		while i < len(dialogue_en) and i < len(dialogue_ru):
			get_whole_line(dialogue_en, i)
			get_whole_line(dialogue_ru, i)
			file.write("%s\n" %(dialogue_en[i]))
			file.write("%s\n\n" %(dialogue_ru[i]))
			i += 1

		file.write("\n{SEPARATOR}\n\n")

def	write_in_file(file: str, text: str):
	with open(file, "a") as fd:
		fd.write(text)


def	get_dialogue_list(file_name: str) -> list[str]:
	with open(file_name) as file:
		dialogue_ids = find_line(file, "inarr=[")
		dialogue = find_line(file, "textarr=[")
	return fix_dialogue(dialogue, dialogue_ids)



def	main_character_dialogues(filename_pattern: str):

	files_en = glob.glob("./html_en/%s" %(filename_pattern))
	files_en.sort()
	files_ru = glob.glob("./html_ru/%s" %(filename_pattern))
	files_ru.sort()
	i = 0
	for current_file in files_en:
		print("current file = %s\n" %(current_file))
		write_in_file(FILE, " *** %s ***\n" %(current_file))
		dialogue_en = get_dialogue_list(current_file)
		dialogue_ru = get_dialogue_list(files_ru[i])
		write_dialogue(dialogue_en, dialogue_ru)
		i += 1

def	main():

	open(FILE, "w").close()
	main_character_dialogues("NPC_Danko_*.html")
	main_character_dialogues("NPC_Burah_*.html")
	main_character_dialogues("NPC_Klara_*.html")
	main_character_dialogues("NPC_Random_*.html")
	print("done")

if	__name__ == "__main__":
	main()