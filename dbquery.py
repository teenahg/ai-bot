import cx_Oracle
# conn = cx_Oracle.connect('timb/xyzzy/orac')
# userpass = 'xyzzy'
conn = cx_Oracle.connect('timb', 'xyzzy', '172.18.170.10/orac')
# curr = conn.cursor()
# curr.execute('select name from growermaster_test where grower = `V123456`')
# for line in curr:
#     print(line)
if conn:
    print('congrats')
else:
    print('failed')
conn.close()