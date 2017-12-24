# coding:UTF-8
import os.path
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer
schema = Schema(
    path=ID(stored=True),
    filename=TEXT(stored=True, analyzer=ChineseAnalyzer()))
