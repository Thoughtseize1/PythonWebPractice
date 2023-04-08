from prettytable import PrettyTable

table = PrettyTable(["Currency:", "Sale:", "Buy:"])

# Add rows to the table
table.add_row(["", "18.03.2023", ""])
table.add_row(["USD", "38.6", "38.1"])
table.add_row(["EUR", "40.9", "39.9"])

table.add_row(["", "17.03.2023", ""])
table.add_row(["USD", "38.6", "38.1"])
table.add_row(["EUR", "40.85", "39.85"])

table.add_row(["", "16.03.2023", ""])
table.add_row(["USD", "38.52", "38.02"])
table.add_row(["EUR", "40.65", "39.65"])

# Set style
table.align["Currency:"] = "l"
table.align["Sale:"] = "r"
table.align["Buy:"] = "r"
# table.hrules = PrettyTable.ALL

print(table)
