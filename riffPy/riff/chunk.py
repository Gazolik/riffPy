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
        total_size = self.size
        if total_size % 2 != 0:
            total_size += 1
        return total_size + CHUNKHEADER_SIZE

    def byte_serialize(self, bigendian=False):
        """

        :return: The chunk as serialized data
        """
        print('Appending chunk {} of size {}'.format(self.name, self.size))
        serialized = b''
        serialized += self.name
        return serialized


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
            size += chunk.total_size
        return size + CHUNKTYPE_SIZE

    @property
    def total_size(self):
        return super(ListChunk, self).total_size + CHUNKTYPE_SIZE

    def append(self, chunk: Chunk):
        self.sub_chunks.append(deepcopy(chunk))

    def byte_serialize(self, bigendian=False):
        serialized = super().byte_serialize()
        serialized += self.size.to_bytes(4, 'little' if bigendian is False else 'big')
        serialized += self.form_type
        for sub in self.sub_chunks:
            serialized += sub.byte_serialize()
            if sub.size % 2 != 0:
                serialized += b' '
        return serialized


class RiffChunk(ListChunk):
    def __init__(self, name, sub_chunks, form_type):
        super().__init__(name, sub_chunks, form_type)

    @property
    def size(self):
        return super().size - CHUNKTYPE_SIZE


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

    def byte_serialize(self, bigendian=False):
        serialized = super().byte_serialize()
        serialized += self.size.to_bytes(4, 'little' if bigendian is False else 'big')
        serialized += self.data.content
        return serialized