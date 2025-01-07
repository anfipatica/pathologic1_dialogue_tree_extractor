import glob

FILE = "dialogues.txt"
SEPARATOR = "------------------------------------------------------------"

def	find_line(file) -> str:

	line: str = ""

	for line in file:
		if line.find("textarr=[") != -1:
			return (line)

def	fix_dialogue(dialogue: str) -> list[str]:

	dialogue = dialogue.replace('\"', '\'')
	dialogue = dialogue.removeprefix("                    textarr=[\'")
	fixed_dialogue = dialogue.split("\', \'")
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
	j = 0
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
		dialogue = find_line(file)
	return fix_dialogue(dialogue)


def	main_character_dialogues(filename_pattern: str):

	files_en = glob.glob(filename_pattern)
	files_en.sort()
	files_ru = glob.glob("../html_ru/%s" %(filename_pattern))
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

if	__name__ == "__main__":
	main()