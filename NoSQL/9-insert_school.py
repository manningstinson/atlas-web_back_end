#!/usr/bin/env python3
""" MongoDB Document Insertion Examples

This script demonstrates how to connect to a MongoDB database and perform
various document insertion operations based on the state of the collection.
It includes examples for inserting simple and complex documents in different
scenarios.

Prerequisites:
- MongoDB must be installed.
- PyMongo must be installed (`pip install pymongo`).
"""

import subprocess
from pymongo import MongoClient

def start_mongodb():
    """Starts the MongoDB service if it is not already running."""
    try:
        # Check the status of the MongoDB service
        status = subprocess.run(["systemctl", "is-active", "mongodb"], capture_output=True, text=True)
        if status.stdout.strip() != "active":
            print("Starting MongoDB...")
            # Attempt to start the MongoDB service
            result = subprocess.run(["sudo", "systemctl", "start", "mongodb"], capture_output=True, text=True)
            if result.returncode == 0:
                print("MongoDB started successfully.")
            else:
                print(f"Failed to start MongoDB: {result.stderr}")
        else:
            print("MongoDB is already running.")
    except Exception as e:
        print(f"An error occurred while trying to start MongoDB: {e}")

def insert_simple_document(collection, document):
    """Inserts a simple document into the specified MongoDB collection.

    Args:
        collection: The pymongo collection object where the document will be inserted.
        document (dict): The simple document to be inserted.

    Prints:
        The _id of the inserted document.
    """
    result = collection.insert_one(document)
    print(f"Inserted simple document with _id: {result.inserted_id}")

def insert_complex_document(collection, document):
    """Inserts a complex document into the specified MongoDB collection.

    Args:
        collection: The pymongo collection object where the document will be inserted.
        document (dict): The complex document to be inserted.

    Prints:
        The _id of the inserted document.
    """
    result = collection.insert_one(document)
    print(f"Inserted complex document with _id: {result.inserted_id}")

def main():
    """Main function to execute the MongoDB document insertion scenarios."""
    # Start MongoDB
    start_mongodb()

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.my_db
    school_collection = db.school

    # 1. Empty collection - create one simple document
    print("\nEmpty collection - creating one simple document")
    school_collection.delete_many({})  # Ensure the collection is empty
    insert_simple_document(school_collection, {"name": "Simple School A"})

    # 2. Collection with 1 document - create one simple document
    print("\nCollection with 1 document - creating one simple document")
    insert_simple_document(school_collection, {"name": "Simple School B"})

    # 3. Collection with 5 documents - create one simple document
    print("\nCollection with 5 documents - creating one simple document")
    for i in range(3, 6):
        insert_simple_document(school_collection, {"name": f"Simple School {i}"})

    # 4. Collection with 5 documents - create 5 simple documents
    print("\nCollection with 5 documents - creating 5 simple documents")
    for i in range(6, 11):
        insert_simple_document(school_collection, {"name": f"Simple School {i}"})

    # 5. Collection with 5 documents - create one complex document
    print("\nCollection with 5 documents - creating one complex document")
    insert_complex_document(school_collection, {
        "name": "Complex School",
        "address": "123 Complex St",
        "courses": ["Math", "Science", "Art"],
        "students": [{"name": "Alice"}, {"name": "Bob"}]
    })

    # 6. Collection with 5 documents - create 5 complex documents
    print("\nCollection with 5 documents - creating 5 complex documents")
    for i in range(1, 6):
        insert_complex_document(school_collection, {
            "name": f"Complex School {i}",
            "address": f"{i} Complex Ave",
            "courses": ["Course A", "Course B"],
            "students": [{"name": f"Student {j}"} for j in range(1, 4)]
        })

if __name__ == "__main__":
    main()
