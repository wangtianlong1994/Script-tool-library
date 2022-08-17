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
# import os
# from xml.dom.minidom import parse
#
# def readXML():
#     for i in os.listdir("./5-2_xml"):
#         domTree = parse("./5-2_xml/"+i)
#         s = "./5-2_xml/"+i
#         # 文档根元素
#         rootNode = domTree.documentElement
#         # print(rootNode.nodeName)
#         customers = rootNode.getElementsByTagName("name")
#
#         for i in range(len(customers)):
#             if "yewei" not in str(customers[i].firstChild.data) and "blue" not in str(customers[i].firstChild.data) :
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "ng"
#                 print("改变后："+customers[i].firstChild.data)
#         #
#                 print(s)
#         with open(s, 'w') as fh:
#             rootNode.writexml(fh)
# if __name__ == '__main__':
#     readXML()


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

#
# #修改xml节点名称
# import os
# from xml.dom.minidom import parse
#
# def readXML():
#     for i in os.listdir("4_xml"):
#         domTree = parse("4_xml/"+i)
#         s = "4_xml/"+i
#         # 文档根元素
#         rootNode = domTree.documentElement
#         # print(rootNode.nodeName)
#         customers = rootNode.getElementsByTagName("name")
#
#         for i in range(len(customers)):
#             if "qingzhou" in str(customers[i].firstChild.data):
#                 print(s)
#                 print("改变前："+customers[i].firstChild.data)
#                 customers[i].firstChild.data = "qingya"
#                 print("改变后："+customers[i].firstChild.data)
#
#         with open(s, 'w') as fh:
#             rootNode.writexml(fh)
# if __name__ == '__main__':
#     readXML()

#
#删除空白xml文件
import os
from xml.dom.minidom import parse

def readXML():
    for i in os.listdir("4_xml"):
        domTree = parse("4_xml/"+i)
        s = "4_xml/"+i
        # 文档根元素
        rootNode = domTree.documentElement
        # print(rootNode.nodeName)
        customers = rootNode.getElementsByTagName("object")
        if customers:
            pass
        else:
            os.remove(s)
if __name__ == '__main__':
    readXML()