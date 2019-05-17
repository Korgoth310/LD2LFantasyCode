import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    #""" create a database connection to the SQLite database
    #    specified by db_file
    #:param db_file: database file
    #:return: Connection object or None
    #"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return None

def create_table(conn, create_table_sql):
    #""" create a table from the create_table_sql statement
    #:param conn: Connection object
    #:param create_table_sql: a CREATE TABLE statement
    #:return:
    #"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = 'E:\LD2L_Fantasy_Repository'

    sql_create_player_table = """CREATE TABLE IF NOT EXISTS players (
                                    player_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    LD2L_team text NOT NULL
                                    );"""
    
    sql_create_game_table = """CREATE TABLE IF NOT EXISTS games (
                                    match_id integer PRIMARY KEY,
                                    date datetime NOT NULL,
                                    week integer NOT NULL
                                    );"""
    
    sql_create_playergame_table = """CREATE TABLE IF NOT EXISTS players_in_game (
                                    player_ id integer PRIMARY KEY,
                                    match_id integer PRIMARY KEY,
                                    points float,
                                    kills integer,
                                    deaths integer,
                                    last_hits integer,
                                    gold_per_minute integer,
                                    tower_kills integer,
                                    roshan_kills integer
                                    kill_participation float,
                                    wards_placed integer,
                                    camps_stacked integer,
                                    rune_pickups integer,
                                    first_blood integer,
                                    stuns float
                                    );"""
    
    con = create_connection(database)
    if conn is not None:
        
        create_table(conn, sql_create_player_table)

        create_table(conn, sql_create_game_table)

        create_table(conn, sql_create_playergame_table)
    
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()


