from prettytable import PrettyTable

table=PrettyTable()
table.names=['Name','Age']
table.add_row(['Alice',24])
table.add_row(['Bob',19])
table.add_row(['Charlie',30])

print(table)
