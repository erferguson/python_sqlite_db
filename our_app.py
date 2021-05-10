import database

# Add a Record to the DB
# database.add_one("Duncan", "Ferguson", "df@everton.fc")

# DELETE record use rowid as STRING
# database.delete_one('8')

# ADD MANY Records
# new_teammates = [
    # ('Tim', 'Howard','th@everton.fc'),
    # ('Brian', 'McBride','bm@everton.fc')
    # ]
# database.add_many(new_teammates)

database.email_lookup("th@everton.fc")

#Show all the Records
# database.show_all()