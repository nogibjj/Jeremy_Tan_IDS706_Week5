"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/serve_times.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("ServeTimesDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS ServeTimesDB")
    c.execute(
        """
        CREATE TABLE ServeTimesDB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            server TEXT,
            seconds_before_next_point INTEGER,
            day TEXT,
            opponent TEXT,
            game_score TEXT,
            sets INTEGER,
            game TEXT
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO ServeTimesDB (
            server, 
            seconds_before_next_point, 
            day, opponent, game_score, 
            sets, 
            game
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "ServeTimesDB.db"
