
#以一个dict传入数据，
#组合的时候，怎么把key带上
#组合生成一个json数据

d={"user_id_type":["user_id","union_id","open_id"],"department_id_type":["user_id","union_id","open_id"],
   "int_type":[1,2,3],"eva_list":[["777888"],["111222"]]}

#正交表
from pyDOE2 import ff2n
import copy
d = { "user_id_type": ["user_id", "union_id", "open_id"], "department_id_type": ["dep_id", "open_dep_id"], "int_type": [1, 2, 3], "eva_list": [["777888"], ["111222"]] }
# 设置每个因素的级别数
level = 2
# 将字典转换为列表
input_list = []
for k, v in d.items():
   if isinstance(v, list):
      input_list.append(v)
   else:
      input_list.append([v])
# 生成正交表


output_list = ff2n(len(input_list)).tolist()
# 将正交表中的0和1替换为每个因素的级别值
for i in range(len(output_list)):
   for j in range(len(output_list[i])):
      if output_list[i][j] == -1:
         output_list[i][j] = input_list[j][0]
      else:
         output_list[i][j] = input_list[j][1]
# 将列表转换回字典
output_dict_list = []
for item in output_list:
   temp_dict = {}
   for i in range(len(item)):
      key = list(d.keys())[i]
      temp_dict[key] = item[i]
      output_dict_list.append(temp_dict)
# 显示生成的正交表
for item in output_dict_list:
   print(item)






def genData(name,d):
   pass