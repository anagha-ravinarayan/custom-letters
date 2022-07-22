with open("Input/Letters/starting_letter.txt") as starting_file:
    contents = starting_file.read()

invited_names = []
with open("Input/Names/invited_names.txt") as invited_names_file:
    names_in_file = invited_names_file.readlines()
    for name in names_in_file:
        invited_names.append(name.strip("\n"))

for name in invited_names:
    file_name = f"letter-for-{name.lower()}.txt"
    file_path = f"Output/ReadyToSend/{file_name}"
    file_contents = contents.replace("[name]", name)
    with open(file=file_path, mode="w") as file_to_write:
        file_to_write.write(file_contents)
