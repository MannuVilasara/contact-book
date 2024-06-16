# 👥 contact: A simple cli based contact book

> NOTE: This is my project done for internship.

```bash
❯ contact -h
usage: contact [-h] [--add ADD] [--delete DELETE] [--search SEARCH] [--update UPDATE] [--list]

A Contact Book written in python

options:
  -h, --help       show this help message and exit
  --add ADD        Add new contact
  --delete DELETE  Delete a contact
  --search SEARCH  Search for a contact
  --update UPDATE  Update Contact
  --list           List all contacts

```

```bash
❯ contact
+---------+------------+---------------+-----------+
| Name    |      Phone | Email         | Address   |
+=========+============+===============+===========+
| someone | 0000011111 | idk@something | jupiter   |
+---------+------------+---------------+-----------+
| root    | 1234509876 | root@root     | 127.0.0.1 |
+---------+------------+---------------+-----------+

Total contacts:  2

[?] Choose Action:
 > Add
   Delete
   Update
   Search
   List
   Exit (q)
```

## Feature:

- Add Contact
- Delete Contact
- Update Contact
- Search Contact
- List all Contacts

## Tech Used:

- colorama: For showing coloured outputs
- argparse: To get arguments
- inquirer: For interactive menu
- tabulate: To show contacts in Table

⭐ Star the repo :)
