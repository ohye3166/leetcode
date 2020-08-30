# -*- coding: utf-8 -*-
# @Time : 2020年08月30日 21时16分
# @Email : 562672808@qq.com
# @Author : ohye3166
# @File : 557.py
# @notice ：
"""
问题：给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""
class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])[::-1]
class SingleWord(object):
    def reverseWords(self,s):
        return ' '.join(s.split()[::-1])

def main():
    # while True:
    #     solution = Solution()
    #     s = input("请输入：")
    #     print("结果是：" + solution.reverseWords(s))

    while True:
        singleWord = SingleWord()
        s = input("请输入：")
        print("结果是：" + singleWord.reverseWords(s))



if __name__ == '__main__':
    main()

"""
收获：
1.split()函数：默认采用分隔符进行分割,返回一个list;
2.‘ ’.join(list)：把list拼接为一个str
3.把list反向，然后输出：hello world 变成 world hello
4.再把str反向，world hello 变成最终结果
"""



