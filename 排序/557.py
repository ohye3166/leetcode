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

def main():
    while True:
        solution = Solution()
        s = input("请输入：")
        print("结果是：" + solution.reverseWords(s))


if __name__ == '__main__':
    main()
