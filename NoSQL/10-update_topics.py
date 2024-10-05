#!/usr/bin/env python3
""" 
10-main

This script serves as the main entry point for updating topics in a MongoDB 
collection of schools. It connects to the MongoDB database, updates the 
topics for a specific school, and prints the updated list of schools along 
with their topics.

Prerequisites:
- Ensure MongoDB is running and accessible at 'mongodb://127.0.0.1:27017'.
- The `list_all` function should be defined in the `8-all` module.
- The `update_topics` function should be defined in the `10-update_topics` module.
"""

from pymongo import MongoClient

# Import the list_all function from the '8-all' module to retrieve school records.
list_all = __import__('8-all').list_all

# Import the update_topics function from the '10-update_topics' module to update school topics.
update_topics = __import__('10-update_topics').update_topics

if __name__ == "__main__":
    # Establish a connection to the MongoDB server at the specified URI.
    # This assumes the MongoDB server is running locally on the default port (27017).
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the 'school' collection in the 'my_db' database.
    # This collection is expected to contain documents representing different schools.
    school_collection = client.my_db.school

    # Update the topics for "Holberton school" with a new list of topics.
    # This function call will modify the relevant document(s) in the collection.
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    # Retrieve and list all schools in the collection after the update.
    schools = list_all(school_collection)
    for school in schools:
        # Print each school's _id, name, and topics.
        # The get method is used to avoid KeyError if the key does not exist.
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    # Update the topics for "Holberton school" again, this time with a different list of topics.
    update_topics(school_collection, "Holberton school", ["iOS"])

    # Retrieve and list all schools in the collection again after the second update.
    schools = list_all(school_collection)
    for school in schools:
        # Print each school's _id, name, and updated topics.
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
