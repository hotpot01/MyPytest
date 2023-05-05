import os

print(os.path.basename(__file__))



#完全自己搭建的框架，层级嵌套比较混乱

#一个psm下的所有接口

#执行，和分级执行

#分环境执行，这个框架都不能覆盖
#
# 有学习到：
# 配置文件的读写
# os和sys库的区别
# Utils.get_conf("common", "env")
#rpc和http test
# env=boe;
# domain=pony-lessson-backend  (不是拼接到的，而是查询到的)
# return config[section][key]
# env = Utils.get_env()
# psm = file_name.replace(".py", "")
# domain = Utils.get_conf("domains", f"{env}_{psm}_domain")