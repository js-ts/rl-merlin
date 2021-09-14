from dataclasses import dataclass

@dataclass
class PathMetadata:
    is_directory: bool = False
    num_files: int = 1
    protocol: str = 'file'
    is_valid: bool = True
    is_path_exists: bool = True