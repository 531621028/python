# coding:GBK
import os.path
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer

schema = Schema(
    title=TEXT(stored=True),
    content=TEXT(stored=True, analyzer=ChineseAnalyzer()),
    #content=TEXT(stored=True),
    path=ID(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)
ix = open_dir("index")
writer = ix.writer()
writer.add_document(title=u"学习", path=u"/a", content=u"hello 胡康康")
writer.add_document(title=u"学习", path=u"/a", content=u"hello world")
writer.commit()
searcher = ix.searcher()
qp = QueryParser("content", schema=ix.schema)
q = qp.parse(u"hello")
print(q)
with ix.searcher() as s:
    results = s.search(q)
    for result in results:
        print(result.highlights("content"))
# results = searcher.find('content', "th*")
# for hit in results:
#     print(hit.highlights("content"))