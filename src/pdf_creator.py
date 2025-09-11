import main
import dialogues_cleaner

FILE = "/home/anfi/Desktop/pathologic_stuff/pathologic1_dialogue_tree_extractor/dialogues.txt"
SEPARATOR = "------------------------------------------------------------"

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

def	create_pdf():
	open(FILE, "w").close()
	dialogues_cleaner.main_character_dialogues("NPC_Danko_*.html", None)
	dialogues_cleaner.main_character_dialogues("NPC_Burah_*.html", None)
	dialogues_cleaner.main_character_dialogues("NPC_Klara_*.html", None)
	dialogues_cleaner.main_character_dialogues("NPC_Random_*.html", None)
	print("done")