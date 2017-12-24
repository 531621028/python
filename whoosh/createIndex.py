# coding:UTF-8
import os
from whoosh.fields import Schema, ID, TEXT
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer


def getIndex(dirPath):
    schema = Schema(
        path=ID(stored=True),
        fileName=TEXT(stored=True, analyzer=ChineseAnalyzer()))
    indexDir = dirPath + os.path.sep + 'index'
    if not os.path.exists(indexDir):
        os.mkdir(indexDir)
        index = create_in(indexDir, schema)
    index = open_dir(indexDir)
    return index


def writeDocument(index, documents=[]):
    writer = index.writer()
    for document in documents:
        # print(document)
        writer.add_document(path=document[0], fileName=document[1])
    writer.commit()


def generateIndexFile(dirPath):
    allFiles = os.walk(dirPath)
    files = []
    for directory, _, fileNames in allFiles:
        for fileName in fileNames:
            files.append((directory, fileName))
    index = getIndex(dirPath)
    writeDocument(index, files)


def searchFile(index, condition=''):
    parser = QueryParser(u"fileName", schema=index.schema)
    query = parser.parse(condition)
    print(query)
    with index.searcher() as s:
        results = s.search(query)
        for result in results:
            print(result['path']+os.path.sep+result['fileName'])


if __name__ == '__main__':
    # generateIndexFile('E:\Python\whoosh')
    searchFile(getIndex('E:\Python\whoosh'), 'cre*')
    print(os.path.sep)