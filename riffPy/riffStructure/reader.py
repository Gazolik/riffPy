import chunk

from . import CHUNKTYPE_SIZE, CHUNKHEADER_SIZE
from .chunk import RiffChunk, ListChunk, FinalChunk
from .data import Data



class ChunkReader(object):
    def __init__(self, bigendian=False):
        self.bigendian = bigendian

    def read_riff(self, filename):
        """ Read a RIFF file and put it in a RiffChunk object

        :param filename: The path to the RIFF file
        :return: A RiffChunk Object
        """
        with open(filename, 'rb') as file:
            current_chunk = chunk.Chunk(file, bigendian=self.bigendian)
            riff_name = current_chunk.getname()
            riff_size = current_chunk.getsize() - CHUNKTYPE_SIZE
            riff_type = current_chunk.read(CHUNKTYPE_SIZE)
            sub_chunks = self.read_chunks(riff_size, file)
            riff_chunk = RiffChunk(riff_name, sub_chunks, riff_type)
        return riff_chunk

    def read_chunks(self, size, file):
        """Read a list of chunks

        :param size: The total size of the list
        :param file: The file handler
        :return: a list of chunks
        """
        chunks = []
        offset = 0
        while offset < size:
            try:
                chunk = self.read_chunk(file)
            except EOFError:
                break
            chunks.append(chunk)
            offset += chunk.size + CHUNKHEADER_SIZE
        return chunks

    def read_chunk(self, file):
        """Read a chunk starting at the actual position of the file handler

        :param file: The file handler
        :return: a Chunk
        """
        current_chunk = chunk.Chunk(file, bigendian=self.bigendian)
        chunk_name = current_chunk.getname()
        print(chunk_name)
        chunk_size = current_chunk.getsize()
        if chunk_name == b'LIST':
            chunk_type = current_chunk.read(CHUNKTYPE_SIZE)
            sub_chunks = self.read_chunks(chunk_size - CHUNKTYPE_SIZE, file)
            return_chunk = ListChunk(chunk_name, sub_chunks, chunk_type)
        else:
            chunk_data = Data(current_chunk.read(chunk_size))
            return_chunk = FinalChunk(chunk_name, chunk_data)
        return return_chunk
