import sqlite3
from grower import Grower

conn = sqlite3.connect('grower.db')

c = conn.cursor()

# c.execute("""CREATE TABLE growers (
#     growernumber text,
#     natid text
#     )""")

def insert_grower(grower):
    with conn:
        c.execute("INSERT INTO growers VALUES (:growernumber, :natid)", {'growernumber': grower.growernumber, 'natid': grower.natid})


def get_grower_by_grower_number(growernumber):
    c.execute("SELECT * FROM growers where growernumber = :growernumber", {'growernumber': growernumber})
    return (c.fetchall())


def update_pay(emp, pay):
    pass


def remove_emp(emp):
    pass

# grower1 = Grower('V113813', '32-809432R21')
# grower2 = Grower('V101010', '32-543213J87')

# insert_grower(grower1)
# insert_grower(grower2)

# growers = get_grower_by_grower_number('V123456')
# print(growers)

conn.close()