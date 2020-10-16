import os
import sys
import argparse
import functions




info = {"link" : "http://www.wuxiaworld.com/emperor-index/emperor-chapter-",
    "ChapterName" : "emperor-chapter-",
    "NovelName" : "Emperor's Dominaion",
    "author" : "Yan Bi Xiao Sheng, Bao"}


my_parser = argparse.ArgumentParser(description='Make an epub from a web adress')

my_parser.add_argument('Address', metavar='address', type=str, help='The adress where the book is located')
my_parser.add_argument('FirstChapter', metavar='starting_chapter', type=str, help='The chapter where you want to start the ebook')
my_parser.add_argument('LastChapter', metavar='ending_chapter', type=str, help='The chapter where you want to end the ebook')

args = my_parser.parse_args()

adress = args.Address
starting_chapter = args.FirstChapter
ending_chapter = args.LastChapter

print(f"Adress = {adress}")
print(f"First Chapter = {starting_chapter}")
print(f"Last Chapter = {ending_chapter}")

link_list = []