from .path import Path

class GenericPath:
    """Base class for Path definition"""
    def __init__(self, path, extension):
        self.path = Path
        self.extension = extension
        self.path_metadata = {}

    def path_check(self):
        raise NotImplementedError("""Check if it is a valid path""")

    def _path_exists(self):
        raise NotImplementedError("""Check if path exists""")

    def _is_file_directory(self):
        raise NotImplementedError("""Is directory or file""")

    def _count_files(self):
        raise NotImplementedError("""Count number of files with extension in directory""")