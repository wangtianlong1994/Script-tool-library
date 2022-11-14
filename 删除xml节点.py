# from lxml import etree
# import os
#
# # 删除指定文件夹下xml文件中节点（存在多个重复节点删除，需要执行多次）
#
# def createFile(oripath):
#     xml_list = os.listdir("./Annotations")
#     for i in xml_list:  # 遍历所有xml文件
#         fullPath = oripath + i  # 完整路径
#
#         remove_(fullPath)  # 将完整路径作为参数传入调用该函数
# def remove_(path):  # path 是原来xml文件的完整路径
#     tree = etree.parse(path)
#     for i in tree.iter():  # i是该xml中的所有标签
#         if i.tag == "object":  # 找到为object的tag
#             if i.find("name").text == "fanduan":
#                 parent = i.getparent()
#                 print(i)
#                 parent.remove(i)
#     tree.write(path, encoding='utf-8')  # 将tree写入新的文件
#
#
# if __name__ == '__main__':
#     path = "./Annotations/"  # 你要处理的xml文件所在的文件夹路径
#     createFile(path)


#删除多余xml节点
import os
from xml.dom.minidom import parse

def readXML():
    for i in os.listdir("1_aokeng_ao_png_xml"):
        domTree = parse("1_aokeng_ao_png_xml/"+i)
        s = "1_aokeng_ao_png_xml/"+i
        # 文档根元素
        rootNode = domTree.documentElement
        # print(rootNode.nodeName)

        customers = rootNode.getElementsByTagName("name")
        if len(customers) > 1:
            print(i)
        # for i in range(len(customers)):
        #     pass
        #     if "qingzhou" in str(customers[i].firstChild.data):
        #         print(s)
        #         print("改变前："+customers[i].firstChild.data)
        #         customers[i].firstChild.data = "qingya"
        #         print("改变后："+customers[i].firstChild.data)
        #
        # with open(s, 'w') as fh:
        #     rootNode.writexml(fh)
if __name__ == '__main__':
    readXML()