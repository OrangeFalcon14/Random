from typing import List, Any

try:
    import sqlite3
except ImportError as e:
    raise e


class Connection:
    """
    Connection is a wrapper class for sqlite3.Connection. It provides the following methods:
    ->get_table(table) - returns all records from the specified table
    ->execute(sql) - runs sqlite3.Connection.cursor().execute(sql)
    ->get_table_names() - returns a list containing the names of tables in the connected database
    ->get_number_of_rows(table) - returns number of records in the specified table
    ->create_table(name, fields) - creates a table with the name specified and with the columns and their respective
    """
    def __init__(self, db_path: str) -> None:
        try:
            self.connection = sqlite3.connect(db_path)
        except Exception as e:
            raise e
        self.cursor = self.connection.cursor()

    def get_table(self, table: str) -> List[Any]:
        """Returns all records from the specified table."""
        try:
            return self.cursor.execute("SELECT * FROM " + table).fetchall()
        except Exception as e:
            raise e

    def execute(self, sql: str, **kwargs) -> sqlite3.Cursor:
        """Executes a query."""
        try:
            return self.cursor.execute(sql, kwargs)
        except Exception as e:
            raise e

    def get_table_names(self) -> List[Any]:
        """Returns a list of all tables in a database"""
        return [x[0] for x in self.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]

    def get_number_of_rows(self, table: str) -> int:
        """Returns the number of records in the specified table"""
        return int(self.execute("SELECT Count(*) FROM " + table).fetchall()[0][0])

    def create_table(self, name: str, fields: dict) -> None:
        """Creates a table"""
        try:
            command = f"CREATE TABLE IF NOT EXISTS {name} ("
            i = 0
            for key, value in fields.items():
                command += f"{str(key)} {str(value)}"
                if i == len(fields) - 1:
                    pass
                else:
                    command += ","
                i += 1
            command += ")"
            self.execute(command)
        except sqlite3.OperationalError as e:
            raise e
        except Exception as e:
            raise e

    def get_columns(self, table: str) -> List[Any]:
        """Returns the columns or fields in the specified table"""

        try:
            data = self.cursor.execute(f"SELECT * FROM {table}")
            columns = []
            for x in data.description:
                columns.append(x[0])
            return columns
        except Exception as e:
            raise e

    def close(self) -> None:
        self.connection.close()
