
import re
from base_chunker import ChunkerBase
from ..utils.common_utils import genenrate_id_based_string

class SignMvChunker(ChunkerBase):
    def __init__(self) -> None:
        super().__init__()
    
    def _sign_mv_chunker(self, paragraph, window_size, stride):
        '''
            先按照标点符号切割
            最切割后的长句子,按照滑动窗口切割
        '''
        sentences = []
        sentent_list = []
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
        end = 0
        for s in sentences:
            s_len = len(s)
            if s_len < window_size:
                sentent_list.append(
                    {
                        "passage_id": genenrate_id_based_string(s),
                        "passage_content": s,
                        "start": start,
                        "end": start + s_len
                    }
                )
                end = start + s_len
            else:
                s_start = start
                s_end = start + s_len  
                start = 0
                end = start + window_size
                while end < s_len:
                    passage_content = s[start:end]
                    passage_id = genenrate_id_based_string(passage_content)
                    sentent_list.append(
                        {
                            "passage_id": passage_id,
                            "passage_content": passage_content, 
                            "start": s_start,
                            "end": s_start + window_size
                        }
                    )
                    start += stride
                    end = start + window_size
                    s_start += stride
                # 扫尾
                passage_content = s[start:]
                passage_id = genenrate_id_based_string(passage_content)
                end = s_end
                sentent_list.append(
                    {
                        "passage_id":passage_id,
                        "passage_content":passage_content,
                        "start":s_start, 
                        "end": end
                    }
                )
            start = end
        return sentent_list
        
        # # 长度合并
        # for sen in sentent_list:
            
        
        
        # # 符号找
        
        
    def chunker(self, text, window_size, stride, *args, **kwargs):
        return self._sign_mv_chunker(text, window_size, stride, *args, **kwargs)