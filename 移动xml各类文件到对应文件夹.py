#拆分各类xml文件，根据xml节点将其移动到对应类别文件夹
import os
import shutil
from xml.dom.minidom import parse

def readXML():
    for i in os.listdir("Annotations"):
        domTree = parse("Annotations/"+i)
        s = "Annotations/"+i
        # 文档根元素
        rootNode = domTree.documentElement
        # print(rootNode.nodeName)
        customers = rootNode.getElementsByTagName("name")
        if len(customers) < 1:
            print(i)
            os.remove(f"Annotations/{i}")
        # else:
        #     if customers[0].firstChild.data == "Hao":
        #         shutil.move(s, f"好/{i}")
        #     else:
        #         shutil.move(s, f"凹坑/{i}")
if __name__ == '__main__':
    readXML()