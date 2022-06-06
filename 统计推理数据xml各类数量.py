# # huizao
# import xml.etree.ElementTree as ET
# import os
#
# xmlfilepath = 'new_xml/'
# # xmlfilepath = 'data/test'
# # xmlfilepath = 'data/1'
#
# total_xml = os.listdir(xmlfilepath)
# lists = []
# haozao = 0
# aoxian = 0
# heiban = 0
# liekou = 0
# niaozhuo = 0
# gantiao = 0
# lanzao = 0
# shuzao = 0
# popi = 0
# heilie = 0
# for i in total_xml:
#     i = 'new_xml/' + i
#     tree = ET.parse(i)
#     root = tree.getroot()
#     for names in root.findall("object"):
#         name = names.find('name').text
#         if name == "4" or name == "HaoZao":
#             haozao += 1
#         elif name == "1" or name == "HeiBan":
#             heiban += 1
#         elif name == "5" or name == "NiaoZhuo":
#             niaozhuo += 1
#         elif name == "0" or name == "AoXian":
#             aoxian += 1
#         elif name == "2" or name == "GanTiao":
#             gantiao += 1
#         elif name == "6" or name == "LanZao":
#             lanzao += 1
#         elif name == "7" or name == "ShuZao":
#             shuzao += 1
#         elif name == "8" or name == "PoPi":
#             popi += 1
#         elif name == "3" or name == "LieKou":
#             liekou += 1
#         elif name == "9" or name == "HeiLie":
#             heilie += 1
# zs = haozao + gantiao + heiban + liekou + aoxian + niaozhuo + lanzao + shuzao
# print("统计数据集各类数量如下：好枣-%s-,干条-%s-,黑斑-%s-,裂口-%s-,凹陷-%s-,鸟琢-%s-,烂枣-%s-,竖枣-%s-,破皮-%s-,黑裂-%s,总数-%s-" % (haozao, gantiao, heiban, liekou, aoxian, niaozhuo, lanzao, shuzao, popi, heilie, zs))
#

# # junzao
# #7类
# import xml.etree.ElementTree as ET
# import os
#
# xmlfilepath = 'new_xml/'
# # xmlfilepath = 'data/test'
# # xmlfilepath = 'data/1'
#
# total_xml = os.listdir(xmlfilepath)
# lists = []
# haozao = 0
# bianxing = 0
# heiban = 0
# liekou = 0
# xiaoniao = 0
# gantiao = 0
# lanzao = 0
# shuzao = 0
# daniao = 0
# fengban = 0
# huangpi = 0
# for i in total_xml:
#     i = 'new_xml/' + i
#     tree = ET.parse(i)
#     root = tree.getroot()
#     for names in root.findall("object"):
#         name = names.find('name').text
#         if name == "4" or name == "HaoZao":
#             haozao += 1
#         elif name == "1" or name == "HeiBan":
#             heiban += 1
#         elif name == "5" or name == "XiaoNiao":
#             xiaoniao += 1
#         elif name == "0" or name == "BianXing":
#             bianxing += 1
#         elif name == "2" or name == "GanTiao":
#             gantiao += 1
#         elif name == "6" or name == "DaNiao":
#             daniao += 1
#         elif name == "7" or name == "LanZao":
#             lanzao += 1
#         elif name == "8" or name == "LieKou":
#             liekou += 1
#         elif name == "3" or name == "HuangPi":
#             huangpi += 1
#         elif name == "9" or name == "ShuZao":
#             shuzao += 1
#         elif name == "10" or name == "FengBan":
#             fengban += 1
# zs = haozao + gantiao + heiban + liekou + bianxing + daniao + lanzao + shuzao + xiaoniao + fengban + huangpi
# print("统计数据集各类数量如下：好枣-%s-,干条-%s-,黑斑-%s-,裂口-%s-,变形-%s-,大鸟琢-%s-,烂枣-%s-,竖枣-%s-,小鸟啄-%s-,风斑-%s,黄皮-%s,总数-%s-" % (haozao, gantiao, heiban, liekou, bianxing, daniao, lanzao, shuzao, xiaoniao, fengban, huangpi, zs))

# junzao
#7类
import xml.etree.ElementTree as ET
import os

xmlfilepath = 'new_xml/'
# xmlfilepath = 'data/test'
# xmlfilepath = 'data/1'

total_xml = os.listdir(xmlfilepath)
lists = []
haozao = 0
bianxing = 0
heiban = 0
liekou = 0
gantiao = 0
lanzao = 0
shuzao = 0
niaozhuo = 0

for i in total_xml:
    i = 'new_xml/' + i
    tree = ET.parse(i)
    root = tree.getroot()
    for names in root.findall("object"):
        name = names.find('name').text
        if name == "0" or name == "BianXing":
            bianxing += 1
        elif name == "1" or name == "HeiBan":
            heiban += 1
        elif name == "2" or name == "GanTiao":
            gantiao += 1
        elif name == "3" or name == "LieKou":
            liekou += 1
        elif name == "4" or name == "HaoZao":
            haozao += 1
        elif name == "5" or name == "NiaoZhuo":
            niaozhuo += 1
        elif name == "6" or name == "LanZao":
            lanzao += 1
        elif name == "7" or name == "ShuZao":
            shuzao += 1

zs = haozao + gantiao + heiban + liekou + bianxing + niaozhuo + lanzao + shuzao
print("统计数据集各类数量如下：好枣-%s-,干条-%s-,黑斑-%s-,裂口-%s-,变形-%s-,鸟琢-%s-,烂枣-%s-,竖枣-%s-,总数-%s-" % (haozao, gantiao, heiban, liekou, bianxing, niaozhuo, lanzao, shuzao, zs))




# 第四次
# 统计数据集各类数量如下：好枣-4887-,干条-426-,黑斑-1041-,裂口-1841-,变形-470-,大鸟琢-5-,烂枣-11-,竖枣-3-,小鸟啄-531-,风斑-273,黄皮-0,总数-9488-
# 第三次
# 统计数据集各类数量如下：好枣-6325-,干条-243-,黑斑-814-,裂口-929-,变形-655-,大鸟琢-4-,烂枣-15-,竖枣-3-,小鸟啄-232-,风斑-0,黄皮-0,总数-9220-
# 5
    # 统计数据集各类数量如下：好枣-5084-,干条-368-,黑斑-776-,裂口-1548-,变形-409-,大鸟琢-13-,烂枣-8-,竖枣-3-,小鸟啄-779-,风斑-376,黄皮-0,总数-9364-

# 统计数据集各类数量如下：好枣-4873-,干条-409-,黑斑-981-,裂口-1559-,变形-599-,大鸟琢-8-,烂枣-7-,竖枣-2-,小鸟啄-738-,风斑-298,黄皮-0,总数-9474-

# 最新5
# 统计数据集各类数量如下：好枣-4117-,干条-351-,黑斑-573-,裂口-1747-,变形-599-,大鸟琢-6-,烂枣-13-,竖枣-1-,小鸟啄-934-,风斑-267,黄皮-0,总数-8608-
# 3
# 统计数据集各类数量如下：好枣-5776-,干条-148-,黑斑-521-,裂口-1262-,变形-561-,大鸟琢-2-,烂枣-15-,竖枣-0-,小鸟啄-230-,风斑-0,黄皮-0,总数-8515-
# 4
# 统计数据集各类数量如下：好枣-4403-,干条-245-,黑斑-730-,裂口-2167-,变形-378-,大鸟琢-8-,烂枣-15-,竖枣-0-,小鸟啄-550-,风斑-179,黄皮-0,总数-8675-
# 5
# 统计数据集各类数量如下：好枣-4386-,干条-276-,黑斑-649-,裂口-1929-,变形-454-,大鸟琢-7-,烂枣-12-,竖枣-2-,小鸟啄-743-,风斑-191,黄皮-0,总数-8649-
# 5+3 liekou
# 统计数据集各类数量如下：好枣-4100-,干条-306-,黑斑-534-,裂口-1774-,变形-566-,大鸟琢-5-,烂枣-18-,竖枣-8-,小鸟啄-942-,风斑-278,黄皮-0,总数-8531-

# 干条严格-类别重构-合并
# 统计数据集各类数量如下：好枣-4693-,干条-365-,黑斑-528-,裂口-1845-,变形-670-,鸟琢-191-,烂枣-25-,竖枣-19-,总数-8336-
