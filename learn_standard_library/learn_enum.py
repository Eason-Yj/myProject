import enum
from enum import Enum, unique, IntEnum


# ### 创建普通枚举值
class exp1(Enum):
    var1 = 1
    var2 = 1
    var3 = 3


# ### 创建value不能重复的枚举值
@unique
class exp2(Enum):
    var1 = 1
    var2 = 2
    var3 = 3


# ### 创建value类型只能为int类型的枚举值
class exp3(IntEnum):
    var1 = 1
    var2 = 1
    var3 = 3
    var4 = "4"


# ### 基本用法
print(exp1.var1)
print(exp1.var1.name)  # var1
print(exp1.var1.value)  # 1

print(exp1.__members__)
# {'var1': <exp1.var1: 1>, 'var2': <exp1.var1: 1>, 'var3': <exp1.var3: 3>}

print(exp1.__members__.items())
# dict_items([('var1', <exp1.var1: 1>), ('var2', <exp1.var1: 1>), ('var3', <exp1.var3: 3>)}

# 遍历所有的枚举值
members = exp1.__members__
for key in members:
    member = members[key]
    print(member)
    print(member.name)
    print(member.value)
