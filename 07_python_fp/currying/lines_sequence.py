from functools import reduce


def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.split("\n")
            sequence_count = reduce(
                lambda count, line: count + 1 if sequence in line else count, lines, 0
            )
            return sequence_count

        return with_length

    return with_char
