"""Helper Class Module."""

# src/utils/utils.py
import sqlite3


class Record:
    """Class for generic record."""

    def __init__(self, conn: sqlite3.Connection, table_name: str) -> None:
        """Initialize Record object."""
        self.conn = conn
        self.table_name = table_name

    def add_to_db(self, record_data: dict, id_col_name: str) -> None:
        """Add record to table."""
        c = self.conn.cursor()
        # check if record already exists
        c.execute(
            f"SELECT COUNT(*) FROM {self.table_name} \
                WHERE {id_col_name} = ?",
            (record_data[id_col_name],),
        )
        count = c.fetchone()[0]
        if count > 0:
            print(
                f"{self.table_name} with {id_col_name} \
                    {record_data[id_col_name]} already exists."
            )
            return
        # insert new record
        columns = ", ".join(record_data.keys())
        placeholders = ", ".join("?" * len(record_data))
        values = tuple(record_data.values())
        c.execute(
            f"INSERT INTO {self.table_name} ({columns}) \
                VALUES ({placeholders})",
            values,
        )
        self.conn.commit()

    def delete_from_db(self, record_id: str, id_col_name: str) -> None:
        """Delete record from table."""
        c = self.conn.cursor()
        c.execute(
            f"DELETE FROM {self.table_name} WHERE \
                {id_col_name} = ?",
            (record_id,),
        )
        self.conn.commit()

    def update_in_db(self, record_data: dict, id_col_name: str) -> None:
        """Update record in table."""
        c = self.conn.cursor()
        set_clause = ", ".join([f"{key} = ?" for key in record_data.keys()])
        values = tuple(record_data.values()) + (record_data[id_col_name],)
        c.execute(
            f"UPDATE {self.table_name} SET {set_clause} \
                WHERE {id_col_name} = ?",
            values,
        )
        self.conn.commit()
