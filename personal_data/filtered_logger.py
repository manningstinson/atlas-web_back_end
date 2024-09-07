#!/usr/bin/env python3
"""
This module provides tools to filter sensitive information from logs and
handle secure database connections.
"""

import re
import logging
from typing import List, Tuple
import os
import mysql.connector
from mysql.connector import connection


# Task 0: Function to filter sensitive fields
def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the obfuscated log message by replacing field values with a
    redaction string.
    """
    for field in fields:
        message = re.sub(rf"(?<={field}=)[^{separator}]*", redaction, message)
    return message


# Task 1: RedactingFormatter class
class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class to obfuscate sensitive information in logs.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and filter out PII fields.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)


# Task 2: Create logger with PII filtering
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Creates a logger that obfuscates PII data in logs.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


# Task 3: Connect to secure database
def get_db() -> connection.MySQLConnection:
    """
    Connects to the database using credentials from environment variables.
    """
    return mysql.connector.connect(
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    )


# Task 4: Main function to read and filter data from the database
def main():
    """
    Main function to read data from users table and log the filtered output.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        msg = (f"name={row[0]}; email={row[1]}; phone={row[2]}; ssn={row[3]}; "
               f"password={row[4]}; ip={row[5]}; last_login={row[6]}; "
               f"user_agent={row[7]};")
        logger.info(msg)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
