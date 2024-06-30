

'''
todo: 按照符号切割句子太长
'''
import re
from base_chunker import ChunkerBase
from ..utils.common_utils import genenrate_id_based_string

class NestedChunker(ChunkerBase):
    def __init__(self) -> None:
        pass
    
    def _nested_chunker(self, paragraph):
        sentent_list = []
        sentences = []
        pattern = r'(\.{3,6}|[！？。!?])'
        parts = re.split(pattern, paragraph)
        for i in range(0, len(parts)-1, 2):
            sentence = parts[i] + parts[i+1]
            sentences.append(sentence)
        if len(parts) % 2 != 0:
            last_sentence = parts[-1].strip()
            if last_sentence:
                sentences.append(last_sentence)
        start = 0
        for s in sentences:
            s_len = len(s)
            sentent_list.append(
                {
                    "passage_id": genenrate_id_based_string(s),
                    "passage_content": s,
                    "start": start,
                    "end": start + s_len
                }
            )
            start += s_len
        return sentent_list

    def chunker(self, text, window_size, stride, *args, **kwargs):
        return self._sign_chunker(text)
    
    

