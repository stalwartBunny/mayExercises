from sys import argv

script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
#this comment is for science, time travel science. please ignore.
print(f"Do you like ice cream?")
likes = input(prompt)

print(f"Where's your favorite sports team located, {user_name}?")
located = input(prompt)

print("What game system do you enjoy?")
system = input(prompt)

print(f"""
Alright, in short summary you told me {likes} regarding my ice cream inquiry.
You said {located} homes your favorite ball team.
And you enjoy playing games on {system}.
Nice, time to plug those into the security questions for your bank account and be on my way.""")
