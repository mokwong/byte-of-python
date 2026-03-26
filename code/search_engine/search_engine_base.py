class SearchEngineBase(object):

    def __init__(self):
        pass

    def add_corpus(self, file_path):
        """
        添加语料 搜索器爬虫到语料后，送给索引器，索引器对内容进行处理，形成索引
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        """
        索引器处理语料，形成索引
        :param id:
        :param text:
        :return:
        """
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        """
        检索器检索内容
        :param query: 搜索内容
        :return: 搜索结果
        """
        raise Exception('search not implemented.')


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input("输入你需要检索的内容：")
        if query == 'q':
            break
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)
