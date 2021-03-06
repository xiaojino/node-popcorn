# -*- coding: utf-8 -*-
import thulac
import sys
print "name: ", sys.argv[0]
for i in range(1, len(sys.argv)):#这里参数从1开始
    print "param", i, sys.argv[i]
# fileNo = sys.argv[1]
rawFileName = sys.argv[1]
dataFileName = sys.argv[2]
tmpFileName =  sys.argv[3]
sortFileName = sys.argv[4]

# @see 读取文件内容
def readFile(filename):
  content = ""
  try:
    fo = open(filename)
    print "读取文件名：", filename
    for line in fo.readlines():
      content += line.strip()
    print "字数：", content.length
  except IOError as e:
    print "文件不存在或者文件读取失败"
    return ""
  else:
    fo.close()
    return content
# @see 写入文件内容（数组会使用writelines进行写入）
# @param toFile 文件名
#        content 内容
def writeFile(toFile, content):
  try:
    fo = open(toFile, 'wb')
    print "文件名：", toFile
    if type(content) == type([]):
      fo.writelines(content)
    else:
      fo.write(content)
  except IOError:
    print "没有找到文件或文件读取失败"
  else:
    print "文件写入成功"
    fo.close()

# 分词
thu1 = thulac.thulac(seg_only=True) #默认模式
# text = thu1.cut("我爱北京天安门", text=False) #一句话分词
thu1.cut_f(rawFileName, dataFileName) # 文本文件分词


# 排序
word_lst= []
word_dict= {}
word_items= []
def cmp_times (x, y):
  if x.times > y.times :
    return 1
  elif x.times < y.times :
    return -1
  else:
    return 0
class wordItem:
  label = ''
  times = 0
  def __init__(self, l, t):
    self.label = l
    self.times = t
  def __lt__(self, other):
    return self.times < other.times
with open(dataFileName) as wf, open(sortFileName,'w') as wf2, open(tmpFileName, 'w') as wf3:

  for word in wf:  
        word_lst.append(word.split(' ')) 
        for item in word_lst:  
             for item2 in item:  
                if item2 not in word_dict:
                    word_dict[item2] = 1  
                else:  
                    word_dict[item2] += 1  

  for key in word_dict:  
      word_items.append(wordItem(key, word_dict[key]))
      wf3.write(key+' '+str(word_dict[key])+'\n')

  word_items.sort(reverse = True)
  for item in word_items:
      wf2.write(item.label+' '+str(item.times) + '\n')
# raw_input() #added