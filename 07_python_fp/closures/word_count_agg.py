def word_count_aggregator():
    count = 0

    def count_word(doc):
        nonlocal count
        count += len(doc.split())
        return count

    return count_word
