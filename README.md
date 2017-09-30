# riffPy

Read content of RIFF format files (.wav, .avi ...)


## Usage

::
	from riffPy.riff.reader import ChunkReader
	from riffPy.riff.writer import ChunkWriter
	# Read riff from file
    riff = reader.read_riff('./input_file.wav')
	# Modify the Riff structure
    riff.form_type = b'ABCD'
	# Write Riff into a new file
    writer.write_riff(riff, './output_file.wav')

	

The riffPy/ui package can help you to see the content of your file:

install PyQt5
::
	$ pip install PyQt5

Run the main.py file
Drag and drop your Riff file in the left white rectangle, and click on one of the "load" button.
