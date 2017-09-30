from .chunk import RiffChunk, Chunk


class ChunkWriter(object):

    def __init__(self, bigendian=False):
        self.bigendian = bigendian

    def write_riff(self, riff: RiffChunk, filename):
        with open(filename, 'wb') as file:
            self.write_chunk(file, riff)


    def write_chunk(self, file_stream, chunk: Chunk):
        file_stream.write(chunk.byte_serialize())
