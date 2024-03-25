voters = [
    {"name": "John", "registered": True},
    {"name": "Jane", "registered": False},
    {"name": "Alice", "registered": True}
]

registered_voters = list(filter(lambda voter: voter["registered"], voters))
