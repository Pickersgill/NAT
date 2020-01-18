import sqlite3
import markdown

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

markdown.parse("testmd.note", cursor)
