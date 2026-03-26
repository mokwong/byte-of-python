import bag_of_words_engine
import search_engine_base


class MyVersionBOWInvertedIndexEngine(search_engine_base.SearchEngineBase):
    """
    倒排索引

    word -> text_id_set
    """

    def __init__(self):
        super(MyVersionBOWInvertedIndexEngine, self).__init__()
        self.__inverted_index = {}

    def process_corpus(self, id, text):
        words = bag_of_words_engine.BOWEngine.parse_text_to_words(text)
        for word in words:
            if word not in self.__inverted_index:
                # 创建空集合要用 set()，而不能 {}，因为 {} 是创建一个空字典
                self.__inverted_index[word] = set()
            self.__inverted_index[word].add(id)

    def search(self, query):
        query_words = list(bag_of_words_engine.BOWEngine.parse_text_to_words(query))
        # 处理空查询的情况
        if not query_words:
            return []
        result_set = self.__inverted_index[query_words[0]]
        for query_word in query_words[1:]:
            # 直接取交集，性能没那么好？
            result_set = result_set.intersection(self.__inverted_index[query_word])
            if len(result_set) == 0:
                return []
        return list(result_set)


search_engine = MyVersionBOWInvertedIndexEngine()
search_engine_base.main(search_engine)
