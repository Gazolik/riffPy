from copy import deepcopy
from . import CHUNKHEADER_SIZE, CHUNKTYPE_SIZE
from .data import Data

class Chunk(object):
    def __init__(self, name):
        self.name = name

    @property
    def size(self):
        """

        :return: The size of the chunk's data
        """
        raise NotImplementedError('Failed to retrieve the size'
                                  ' of a generic chunk')

    @property
    def total_size(self):
        """

        :return: The total size of the chunk (including the header)
        """
        return self.size + CHUNKHEADER_SIZE


class ListChunk(Chunk):
    def __init__(self, name, sub_chunks, form_type):
        super().__init__(name)
        self.sub_chunks = sub_chunks
        self.form_type = form_type

    @property
    def size(self):
        """The size of a ListChunk is the sum of the sizes
        of the subchunks.

        :return: The size of the chunk
        """
        size = 0
        for chunk in self.sub_chunks:
            size += chunk.size
        return size

    @property
    def total_size(self):
        return super(ListChunk, self).total_size + CHUNKTYPE_SIZE

    def append(self, chunk: Chunk):
        self.sub_chunks.append(deepcopy(chunk))


class RiffChunk(ListChunk):
    def __init__(self, name, sub_chunks, form_type):
        super().__init__(name, sub_chunks, form_type)


class FinalChunk(Chunk):
    """
    A FinalChunk is a chunk without subchunks
    """
    def __init__(self, name, data: Data):
        super().__init__(name)
        self.data = data
        self._size = data.size

    @property
    def size(self):
        return self._size