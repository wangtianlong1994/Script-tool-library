#对比xml文件是否有漏框
import os
from xml.dom.minidom import parse

def readXML():
    names = "train_xml"
    for i in os.listdir(names):
        domTree = parse(names+"/"+i)
        # 文档根元素
        rootNode = domTree.documentElement
        # print(rootNode.nodeName)
        customers = rootNode.getElementsByTagName("name")
        if not customers:
            print(i)
            os.remove(names+"/"+i)
        # a = 0
        # for customer in customers:
        #     a += 1
        # if a == 20 or a == 16:
        #     pass
        # else:
        #     print(i)

if __name__ == '__main__':
    readXML()
