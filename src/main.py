import os
import sqlite3

import pdf_creator
import db_creator
import db_functions as db
import translator_assistant
import execute_query

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
	print("4) Use the translation assistant")
	print("Q) quit\n")

	user_input = input(">> ")
	if (not user_input or "1234Qq".find(user_input) == -1):
		print(RED+">> Invalid option"+STD)
		os.system("sleep 1")
		return(main_menu())
	return (user_input)


def	main():
	user_choice: str = main_menu().upper()
	connection: sqlite3.Connection = db.create_connection()

	match user_choice:
		case "1":
			pdf_creator.create_pdf()
		case "2":
			db_creator.create_db(None) #FIX THIS!! change the cursor it receives to a connection!!
		case "3":
			execute_query.execute_query(connection)
		case "4":
			translator_assistant.start_assisting(connection)
		case "Q":
			print("Thanks for using this program :)")

	connection.close()


if	__name__ == "__main__":
	main()