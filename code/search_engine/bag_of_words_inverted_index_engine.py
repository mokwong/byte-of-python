import bag_of_words_engine
import search_engine_base


class BOWInvertedIndexEngine(search_engine_base.SearchEngineBase):
    """
    倒排索引

    word -> text_id_list
    """

    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.__inverted_index = {}

    def process_corpus(self, id, text):
        words = bag_of_words_engine.BOWEngine.parse_text_to_words(text)
        for word in words:
            if word not in self.__inverted_index:
                self.__inverted_index[word] = []
            self.__inverted_index[word].append(id)

    def search(self, query):
        """
        它会根据 query_words 拿到所有的倒序索引，如果拿不到，就表示有的 query word 不存在于任何文章中，直接返回空；
        拿到之后，运行一个“合并 K 个有序数组”的算法，从中拿到我们想要的 ID，并返回。
        :param query:
        :return:
        """
        query_words = list(bag_of_words_engine.BOWEngine.parse_text_to_words(query))
        query_words_index = list()
        for _ in query_words:
            query_words_index.append(0)

        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.__inverted_index:
                return []

        result = []
        while True:

            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []

            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.__inverted_index[query_word]

                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1


search_engine = BOWInvertedIndexEngine()
search_engine_base.main(search_engine)
