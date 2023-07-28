import json
import yaml
import datetime
from yaml import load, SafeLoader


person = {
	'firstName': 'John',
	'dateOfBirth': datetime.date(1969, 12, 31),
	'married': False,
	'spouse': None,
	'children': ['Bobby', 'Molly'],
}

# print(json.dumps(person, indent=4, default=str))


email_message = """
message:
	date: 2022‐01‐16 12:46:17Z
	from: john.doe@domain.com
	to:
	‐ bobby@domain.com
	‐ molly@domain.com
	cc:
	‐ jane.doe@domain.com
	subject: Friendly reminder
	content: |
	Dear XYZ,

	Lorem ipsum dolor sit amet...
	attachments:
	image1.gif: !!binary
	R0lGODdhCAAIAPAAAAIGAfr4+SwAA
	AAACAAIAAACDIyPeWCsClxDMsZ3CgA7
"""
# print(yaml.safe_load(email_message))
print(load(email_message, SafeLoader))
























