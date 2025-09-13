import sqlite3

import execute_query

FILE = "./files/dialogues_translation_format.txt"


ID = 0
SPANISH = 4
ENGLISH = 2


def line_to_write_in_file(query_line: tuple) -> str:
    if (query_line[SPANISH] is None):
        if (query_line[ENGLISH] is None):
            return ("")
        else:
            return ("FALTA!!!!")
    else:
        return (query_line[SPANISH])

    
def db_to_text(connection: sqlite3.Connection):
    query_results: list

    query_results = execute_query.execute_query(connection, "SELECT * FROM pathologic WHERE id BETWEEN 526692 AND 527819")

    with open(FILE, "w") as fd:
        for line in query_results:
            fd.write(f"<string id=\"%d\"><![CDATA[%s]]></string>\n" %(line[ID], line_to_write_in_file(line)))