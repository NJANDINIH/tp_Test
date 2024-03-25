def register_party(parties):
    for party in parties:
        if party["member_count"] >= 1000:
            print(f"Party {party['party_name']} is registered.")
            # Add code here to register the party in your system
        else:
            print(f"Party {party['party_name']} does not have enough members to register.")

