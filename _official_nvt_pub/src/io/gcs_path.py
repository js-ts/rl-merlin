from generic_path import GenericPath

from fsspec.core import get_fs_token_paths

class GcsPath(GenericPath):
    def __init__(self, 
                 path_name: str, 
                 extension: str, 
                 recursive: bool = False):
        # Fetch name protocol implementation for GCS

        self.fs_spec, _, _ = get_fs_token_paths(path_name)
        path_metadata = self._path_check(path_name, extension, recursive)
        super().__init__(path_name=path_name, 
                         extension=extension, 
                         path_metadata=path_metadata)

    def _path_check(self, path_name, extension, recursive):
        path_metadata = {}

        if self._is_path_exists(path_name):
            path_metadata['is_path_exists'] = True
            path_metadata['is_directory'] = self._is_directory(path_name)
            path_metadata['protocol'] = self._get_protocol()
            path_metadata['num_files'] = self._get_num_files(
                                            path_name,
                                            path_metadata['is_directory'],
                                            recursive,
                                            extension)
            if path_metadata['num_files'] > 0:
                path_metadata['is_valid_path'] = True

        return path_metadata

    def _is_path_exists(self, path_name: str):
        return self.fs_spec.exists(path_name)

    def _is_directory(self, path_name: str):
        return self.fs_spec.isdir(path_name)

    def _get_num_files(self, 
                       path_name: str, 
                       is_directory: bool, 
                       recursive: bool, 
                       extension: str):
        if not is_directory:
            return 1
        else:
            if not path_name.endswith('/'):
                path_name = path_name + '/'
            if recursive:
                file_list = self.fs_spec.glob(f'{path_name}**.{extension}')
            else:
                file_list = self.fs_spec.glob(f'{path_name}*.{extension}')

        return len(file_list)

    def _get_protocol(self):
        if 'gs' in self.fs_spec.protocol:
            return 'gs'
        else:
            return self.fs_spec.protocol