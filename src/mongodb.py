import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class MongoDBLogger:
    def __init__(self):
        mongo_uri = os.getenv("MONGODB_URI")
        db_name = os.getenv("MONGODB_DB", "rag_chatbot")
        collection_name = os.getenv("MONGODB_COLLECTION", "user_questions")

        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_question(self, question: str):
        document = {
            "question": question,
            "created_at": datetime.now(timezone.utc),
        }

        result = self.collection.insert_one(document)
        return result.inserted_id

    def save_question_and_answer(self, question: str, answer: str):
        document = {
            "question": question,
            "answer": answer,
            "created_at": datetime.now(timezone.utc),
        }

        result = self.collection.insert_one(document)
        return result.inserted_id