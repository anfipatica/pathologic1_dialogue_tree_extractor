import shutil

import utils.colors as color
import classes.LineInfo as LineInfo

CURRENT=2

def	print_line(line_info: LineInfo, line_index: int):

	columns = shutil.get_terminal_size(fallback=(80, 24)).columns

	if line_index == CURRENT:
		print(f"{color.BLUE}╔{"═" * (columns-3)}╗{color.STD}")
		print(f"{color.BLUE}║ {color.BG_BLUE}{color.WHITE} {line_info.id[0]}: {line_info.healer[0]} -> {line_info.character[0]}{color.STD}\n{color.BLUE}║")
		print("║ En | %s" %(line_info.english[0]))
		print("║ Ru | %s" %(line_info.russian[0]))
		print("║ Sp | "+color.STD+"%s" %(line_info.spanish)[0])
		print(f"{color.BLUE}╚{"═" * (columns-3)}╝{color.STD}")
	else:
		print(f"{color.GRAY}| {color.BG_GRAY}{color.WHITE} {line_info.id[0]}: {line_info.healer[0]} -> {line_info.character[0]}{color.STD}\n{color.GRAY}|")
		print("| En | %s" %(line_info.english[0]))
		print("| Ru | %s" %(line_info.russian[0]))
		print(f"| Sp | {line_info.spanish[0]}{color.STD}\n\n")

def	print_lines(line_info: list):
	i: int = 0
	for line in line_info:
		print_line(line, i)
		i += 1
