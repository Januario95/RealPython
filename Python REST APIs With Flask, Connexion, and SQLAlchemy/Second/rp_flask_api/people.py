import random
from datetime import datetime, timedelta

def get_timestamp():
	now = datetime.now() - timedelta(
		hours=random.randint(0, 15),
		minutes=random.randint(0, 59),
		seconds=random.randint(0, 59))
	return now.strftime('%Y-%m-%d %H:%M:%S')

PEOPLE = {
	'Fairy': {
        'fname': 'Tooth',
        'lname': 'Fairy',
        'timestamp': get_timestamp(),
    },
    'Ruprecht': {
        'fname': 'Knecht',
        'lname': 'Ruprecht',
        'timestamp': get_timestamp(),
    },
    'Bunny': {
        'fname': 'Easter',
        'lname': 'Bunny',
        'timestamp': get_timestamp(),
    }
}

def read_all():
	return list(PEOPLE.values())

