import os
import sqlite3

import pdf_creator
import db_creator
import translation_program.db_functions as db
import translation_program.translator_assistant as translator_assistant
import execute_query
import db_to_text
from translation_program import lines_per_day_queries as lines_queries
from utils.git_upload import upload_to_github


STD='\033[39m'
GRAY='\033[90m'
RED='\033[31m'


def	main_menu() -> str:
	user_input: str

	os.system("clear")
	print("What do you want to do?\n")
	print("1) Extract dialogues as a pdf")
	print("2) Create or update the database")
	print("3) Make a query")
	print("4) Use the translation program")
	print("5) Extract database as translation file")
	print("Q) quit\n")

	user_input = input(">> ")
	if (not user_input or "12345Qq".find(user_input) == -1):
		print(RED+">> Invalid option"+STD)
		os.system("sleep 1")
		return(main_menu())
	return (user_input)


def	main():
	user_choice: str = main_menu().upper()
	connection: sqlite3.Connection = db.create_connection()
	lines_queries.update_lines_per_day(connection, 0)

	match user_choice:
		case "1":
			pdf_creator.create_pdf()
		case "2":
			db_creator.create_db(None) #FIX THIS!! change the cursor it receives to a connection!!
		case "3":
			execute_query.execute_query(connection)
		case "4":
			translator_assistant.start_translation_program(connection)
		case "5":
			db_to_text.db_to_text(connection)


	#upload_to_github()
	lines_queries.print_total_translated_lines(connection)
	connection.close()
	print("Thanks for using this program :)")


if	__name__ == "__main__":
	main()