# import os
# import xml.etree.ElementTree as ET
#
# paths = "Annotations/"
# xml_list = os.listdir(paths)
# for xmls in xml_list:
#     tree = ET.parse(paths + xmls)
#     root = tree.getroot()
#     root.find("filename").text = xmls
#     tree.write(paths + xmls)

# #修改xml节点名称
# import os
# from xml.dom.minidom import parse
#
# def readXML():
#     for i in os.listdir("5"):
#         domTree = parse("5/"+i)
#         s = "5/"+i
#         # 文档根元素
#         rootNode = domTree.documentElement
#         # print(rootNode.nodeName)
#         customers = rootNode.getElementsByTagName("name")
#
#         domTree1 = parse("4/" + i)
#         # 文档根元素
#         rootNode1 = domTree1.documentElement
#         # print(rootNode.nodeName)
#         customers1 = rootNode1.getElementsByTagName("name")
#         for i in range(len(customers1)):
#             if "PoPi" in str(customers1[i].firstChild.data):
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = customers1[i].firstChild.data
#                 print("改变后："+customers[i].firstChild.data)
#
#         with open(s, 'w') as fh:
#             rootNode.writexml(fh)
# if __name__ == '__main__':
#     readXML()
#

#
#修改xml节点名称
import os
from xml.dom.minidom import parse

def readXML():
    for i in os.listdir("./xml"):
        domTree = parse("./xml/"+i)
        s = "./xml/"+i
        # 文档根元素
        rootNode = domTree.documentElement
        # print(rootNode.nodeName)
        customers = rootNode.getElementsByTagName("name")

        for i in range(len(customers)):
            if "wuya" in str(customers[i].firstChild.data):
                print("改变前："+customers[i].firstChild.data)
                customers[i].firstChild.data = "wuhan"
                print("改变后："+customers[i].firstChild.data)
        #
        with open(s, 'w') as fh:
            rootNode.writexml(fh)
if __name__ == '__main__':
    readXML()


# #修改xml节点数据
# import os
# import xml.etree.ElementTree as ET
#
# def readXML():
#     for i in os.listdir("xmls"):
#         s = "xmls/"+i
#         tree = ET.parse(s)
#         root = tree.getroot()
#         filename = root.find('path')
#         file = f'{filename.text.replace("2工位训练用","纽扣电池处理后数据")}'
#         filename.text = file
#         print(filename.text)
#         tree.write(s,"UTF-8")
# if __name__ == '__main__':
#     readXML()


# #修改xml节点名称
# import os
# from xml.dom.minidom import parse
#
# def readXML():
#     for i in os.listdir("Annotations"):
#         domTree = parse("Annotations/"+i)
#         s = "Annotations/"+i
#         # 文档根元素
#         rootNode = domTree.documentElement
#         # print(rootNode.nodeName)
#         customers = rootNode.getElementsByTagName("name")
#
#         for i in range(len(customers)):
#             if "0" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "AoXian"
#                 print("改变后："+customers[i].firstChild.data)
#             elif "1" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "HeiBan"
#                 print("改变后："+customers[i].firstChild.data)
#             elif "2" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "GanTiao"
#                 print("改变后："+customers[i].firstChild.data)
#             elif "3" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "LieKou"
#                 print("改变后："+customers[i].firstChild.data)
#             elif "4" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "HaoZao"
#                 print("改变后："+customers[i].firstChild.data)
#             elif "5" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "NiaoZhuo"
#                 print("改变后："+customers[i].firstChild.data)
#             elif "6" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "LanZao"
#                 print("改变后："+customers[i].firstChild.data)
#             elif "7" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "ShuZao"
#                 print("改变后："+customers[i].firstChild.data)
#         with open(s, 'w') as fh:
#             rootNode.writexml(fh)
# if __name__ == '__main__':
#     readXML()
