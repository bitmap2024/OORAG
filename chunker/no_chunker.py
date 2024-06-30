

from base_chunker import ChunkerBase

class No_chunker(ChunkerBase):
    def __init__(self) -> None:
        pass

    def _nested_chunker(self, paragraph):
        pass