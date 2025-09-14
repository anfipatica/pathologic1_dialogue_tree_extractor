import utils.colors as color

def get_pronouns_list()-> tuple[list[str], list[str]]:

	formal_pronouns = [
		# Personal
		"вы", "Вы",    # nominativo
		"вас", "Вас",  # genitivo / acusativo
		"вам", "Вам",  # dativo
		"вами", "Вами", # instrumental
		"о вас", "О вас",# prepositivo
		# Posesivos
		"ваш",       # masc. sing.
		"ваша",      # fem. sing.
		"ваше",      # neutro sing.
		"ваши",      # plural
		# Posesivos declinados
		"вашего", "вашей", "вашему", "вашем",
		"ваших", "вашими",
		#verbos
		"ете", "ёте",    # 1ª conjugación presente/futuro
		"ите",           # 2ª conjugación presente/futuro
		"ли"             # pasado plural / formal singular
	]

	informal_pronouns = [
		# Personal
		"ты", "Ты",      # nominativo
		"тебя", "Тебя",     # genitivo / acusativo
		"тебе", "Тебе",     # dativo
		"тобой", "Тобой",    # instrumental
		"тобою", "Тобою",    # instrumental (forma alternativa, más literaria)
		"о тебе", "О тебе",   # prepositivo
		# Posesivos
		"твой",     # masc. sing.
		"твоя",     # fem. sing.
		"твоё",     # neutro sing.
		"твои",     # plural
		# Posesivos declinados (ejemplos comunes)
		"твоего", "твоей", "твоему", "твоём",
		"твоих", "твоими",
		#verbos
		"ешь", "ёшь",   # 1ª conjugación presente/futuro
		"ишь",           # 2ª conjugación presente/futuro
		# pasado singular depende del género, normalmente se reconoce con contexto
	]
	return ([formal_pronouns, informal_pronouns])

def	highlight_rusian_pronouns(line: str) ->str:
	formal_pronouns: list[str]
	informal_pronouns: list[str]

	if (line is None):
		return (None)
	formal_pronouns, informal_pronouns = get_pronouns_list()
	for pronoun in formal_pronouns:
		if (line.count(pronoun) > 0):
			line = line.replace(pronoun, f"{color.MAGENTA}{color.BOLD}{pronoun}{color.STD}{color.BLUE}")

	for pronoun in informal_pronouns:
		if (line.count(pronoun) > 0):
			line = line.replace(pronoun, f"{color.GREEN}{color.BOLD}{pronoun}{color.STD}{color.BLUE}")
	return (line)