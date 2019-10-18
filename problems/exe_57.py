def break_test_sentence(sentence, k):
    words = sentence.split()

    broken_text = list()
    char_counter = -1
    current_words = list()
    index = 0
    while index < len(words):
        word = words[index]

        if len(word) > k:
            return None

        # 1 is for space
        if char_counter + len(word) + 1 <= k:
            char_counter += len(word) + 1
            current_words.append(word)
            index += 1
        else:
            broken_text.append(" ".join(current_words))
            char_counter = -1
            current_words = list()

    broken_text.extend(current_words)
    return broken_text


print(break_test_sentence("the quick brown fox jumps over the lazy dog", 10))
