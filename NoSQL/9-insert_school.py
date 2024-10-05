#!/usr/bin/env python3
""" MongoDB Document Insertion Examples """

from pymongo import MongoClient

# Function to insert a simple document
def insert_simple_document(collection, document):
    """Inserts a simple document into the collection."""
    result = collection.insert_one(document)
    print(f"Inserted simple document with _id: {result.inserted_id}")

# Function to insert a complex document
def insert_complex_document(collection, document):
    """Inserts a complex document into the collection."""
    result = collection.insert_one(document)
    print(f"Inserted complex document with _id: {result.inserted_id}")

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.my_db
    school_collection = db.school

    # 1. Empty collection - create one simple document
    print("Empty collection - creating one simple document")
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

    # 5. Collection with 5 documents - create 1 complex document
    print("\nCollection with 5 documents - creating one complex document")
    insert_complex_document(school_collection, {
        "name": "Complex School A",
        "address": "123 Complex St",
        "courses": ["Math", "Science", "Art"],
        "enrollment": {
            "total": 150,
            "grades": [9, 10, 11, 12]
        }
    })

    # 6. Collection with 5 documents - create 5 complex documents
    print("\nCollection with 5 documents - creating 5 complex documents")
    for i in range(1, 6):
        insert_complex_document(school_collection, {
            "name": f"Complex School {i}",
            "address": f"{i} Complex St",
            "courses": [f"Subject {i}1", f"Subject {i}2"],
            "enrollment": {
                "total": 100 + (i * 10),
                "grades": [9, 10]
            }
        })

    # Output the documents in the collection
    print("\nDocuments in the collection:")
    for school in school_collection.find():
        print(school)

if __name__ == "__main__":
    main()
