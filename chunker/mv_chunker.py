

from base_chunker import ChunkerBase
from ..utils.common_utils import genenrate_id_based_string

class MvChunker(ChunkerBase):
    def __init__(self) -> None:
        pass
    
    def _mv_chunker(self, text, window_size=256, stride=170):
        start, end , sentent_list = 0, window_size, []
        content_len = len(text)
        while end < content_len: 
            passage_content = text[start:end]
            passage_id = genenrate_id_based_string(passage_content)
            sentent_list.append(
                {
                    "passage_id": passage_id,
                    "passage_content": passage_content, 
                    "start": start,
                    "end": end
                }
            )
            start += stride
            end = start + window_size
        # 扫尾
        passage_content = text[start:]
        passage_id = genenrate_id_based_string(passage_content)
        end = content_len
        sentent_list.append(
            {
                "passage_id":passage_id,
                "passage_content":passage_content,
                "start":start, 
                "end": end
            }
        )
        return sentent_list
    
    def chunker(self, text, window_size, stride, *args, **kwargs):
        return self._mv_chunker(text, window_size, stride)
    