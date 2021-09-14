# Copyright 2014 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


'''Wrapper around `gcloud alpha storage` to help perform download
or upload from/to GCS.
'''


from typing import Dict, List, Union
import subprocess


class GcsCopyUtils:
    '''Helper class to perform download/upload from/to GCS
    using `gcloud alpha storage` command line interface.

    Parameters
    ----------
        gcs_source: Union[str,List[str]]
            Path or a list of paths to be DOWNLOADED from GCS.
            The path can be a single file (one path), a list with multiple 
            files (multiple paths), one folder (one path), multiple folders 
            (multiple paths) or a combination of files and folders from GCS.
            Examples:
                (one file): 'gs://my_bucket/file.parquet'
                (multiple files): ['gs://my_bucket/file1.parquet',
                                   'gs://my_bucket/file1.parquet']
                (one folder): 'gs://my_bucket/subfolder'
                (multiple folders): ['gs://my_bucket/subfolder1',
                                     'gs://my_bucket/subfolder2']
                (combination): ['gs://my_bucket/file1.parquet',
                                'gs://my_bucket/subfolder2']
                There is a flag specifically to indicate recursion during 
                download, but if specified in the path, the flag will be 
                ignored. Examples:
                (all files, 1 level): gs://my_bucket/subfolder/*
                (all files, all levels): gs://my_bucket/subfolder/**

        gcs_source: Union[str,List[str]]
        local_download_path: str
        local_upload_path: str
        gcs_dest: str
        recursive: bool
        extension: str
    '''

    def __init__(
        self, 
        gcs_source: Union[str,List[str]],
        local_download_path: str,
        local_upload_path: str,
        gcs_dest: str,
        recursive: bool,
        extension: str
    ):
        if isinstance(gcs_source, list):
            self.gcs_source = gcs_source
        elif isinstance(gcs_source, str):
            self.gcs_source = [gcs_source]

        self.gcs_dest = gcs_dest
        self.local_download_path = local_download_path
        self.local_upload_path = local_upload_path
        self.recursive = recursive
        self.extension = extension

    def compose_gcloud_download_cmd(self) -> str:
        '''
        Valid paths:
            gs://my_bucket/file.parquet # file
            gs://my_bucket/subfolder or gs://my_bucket/subfolder/ # path
            gs://my_bucket/subfolder/* # all files, 1 level
            gs://my_bucket/subfolder/** # all files, all levels
        '''
        rec_symbol = '**' if self.recursive else '*'
        formated_paths = []

        for path in self.gcs_source:
            if path.endswith(f'.{self.extension}'):
                formated_paths.append(path)
            else:
                if path.endswith('/'):
                    formated_paths.append(
                        f'{path}{rec_symbol}.{self.extension}')
                elif (path.endswith('/*') or path.endswith('/**')):
                    formated_paths.append(f'{path}.{self.extension}')
                else:
                    formated_paths.append(
                        f'{path}/{rec_symbol}.{self.extension}')

        gcloud_cmd = ['gcloud', 'alpha', 'storage', 'cp', 
                            *formated_paths, self.local_download_path]

        return gcloud_cmd

    def compose_gcloud_upload_cmd(self) -> List[str]:
        gcloud_cmd = ['gcloud', 'alpha', 'storage', 'cp', 
                            '-r', self.local_download_path, self.gcs_dest]
        return gcloud_cmd

    def execute_gcloud_cmd(self, gcloud_cmd: List[str]) -> Dict[str,str]:
        output = subprocess.run(gcloud_cmd, capture_output=True, text=True)
        return {'returncode': output.returncode,
                'stdout': output.stdout,
                'stderr': output.stderr}

    def foo(self):
        '''Fetches rows from a Smalltable.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by table_handle.  String keys will be UTF-8 encoded.

        Parameters
        ----------
        content_type: str
            If not None, set the content-type to this value
        content_encoding: str
            If not None, set the content-encoding.
            See https://cloud.google.com/storage/docs/transcoding
        kw_args: key-value pairs like field="value" or field=None
            value must be string to add or modify, or None to delete

        Returns
        -------
        Entire metadata after update (even if only path is passed)
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
        b'Zim': ('Irk', 'Invader'),
        b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).
        
        Raises
        ------
            IOError: An error occurred accessing the smalltable.
        '''
        pass
