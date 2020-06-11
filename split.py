import os
import re
os.system('cls')
grower_num_regex1 = re.compile(r'\w{1}\d{6}\w{1}')
grower_num_regex2= re.compile(r'\w{1}\d{6}')
id_num_regex1 = re.compile(r'\d{2}-\d{6}\w{1}\d{2}')
id_num_regex2 = re.compile(r'\d{2}-\d{7}\w{1}\d{2}')

text  = 'V123456W 12-3456789A00'
new = text.split()
grower = new[0]
id = new[1]

validated_grower = grower_num_regex1.search(grower) or grower_num_regex2.search(grower)
validated_id = id_num_regex1.search(id) or id_num_regex2.search(id)

print(validated_grower.group())
print(validated_id.group())

# print(grower, id)