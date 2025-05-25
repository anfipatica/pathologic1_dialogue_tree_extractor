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