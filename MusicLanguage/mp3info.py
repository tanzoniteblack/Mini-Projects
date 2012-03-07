"""Framework for getting music tags from song files.  Should eventually be extended to more than just mp3.  The object created will be a type of dictionary.  The idea for this code is taken from http://www.diveintopython.net/object_oriented_framework/index.html."""

class MP3Tags(dict):
    """Store ID3v1.0 MP3 tags in a dictionary."""
    
