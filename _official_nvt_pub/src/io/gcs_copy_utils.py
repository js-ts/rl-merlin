'''A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
'''

from __future__ import annotations
from google.cloud import storage
from google.cloud.storage import Blob
from google.cloud.storage import Bucket
from typing import Dict, List, NamedTuple
from pathlib import Path
import subprocess

import fsspec


class DataPath(NamedTuple):
    pass


class SourceEmpty(Exception):
    pass


class GcsCopyUtils:
    '''The Vehicle object contains a lot of vehicles

    Parameters
    ----------
        says_str : str
            a formatted string to print out what the animal says
        name : str
            the name of the animal
        sound : str
            the sound that the animal makes
        num_legs : int
            the number of legs the animal has (default 4)
    '''

    def __init__(
        self, 
        gcs_source: List[Blob],
        local_destination: Path,
        gcs_destination: Bucket,
        recursive: bool,
        validate: bool,
        download_incomplete: bool
    ):
        # validated_paths
        pass

    def _compose_gcloud_download_cmd(gcs_paths: List[str],
                                    local_destination: str, 
                                    extension: str = 'parquet', 
                                    recursive: bool = False) -> str:
        '''
        Valid paths:
            gs://my_bucket/file.parquet # file
            gs://my_bucket/subfolder or gs://my_bucket/subfolder/ # path
            gs://my_bucket/subfolder/* # all files, 1 level
            gs://my_bucket/subfolder/** # all files, n levels
        '''

        rec_symbol = '**' if recursive else '*'

        formated_paths = []
        for path in gcs_paths:
            if path.endswith(f'.{extension}'):
                formated_paths.append(path)
            else:
                if path.endswith('/'):
                    formated_paths.append(f'{path}{rec_symbol}.{extension}')
                elif path.endswith('/*') or path.endswith('/**'):
                    formated_paths.append(f'{path}.{extension}')
                else:
                    formated_paths.append(f'{path}/{rec_symbol}.{extension}')

        gcloud_cmd = ['gcloud', 'alpha', 'storage', 'cp', 
                        *formated_paths, local_destination]

        return gcloud_cmd

    def _compose_gcloud_upload_cmd(local_path: str, 
                               gcs_destination: str) -> List[str]:
        gcloud_cmd = ['gcloud', 'alpha', 'storage', 'cp', 
                        '-r', local_path, gcs_destination]
        return gcloud_cmd

    def _execute_gcloud_cmd(gcloud_cmd: List) -> Dict[str,str]:
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







a = Path('/home/renatoleite/')
a.exists()
str(a)

isinstance([], list)



import gcsfs
t2 = gcsfs.GCSFileSystem()
test = fsspec.filesystem('gs')
test.exists('renatoleite-criteo-partial/data/day_0.parquet')
test.info('renatoleite-criteo-partial/')
test.info

type(test)

t2.info('renatoleite-criteo-partial/data/')
t2.cat('renatoleite-criteo-partial/data/')

files = t2.walk('renatoleite-criteo-partial/')
a = list(files)


for i in a:
    if not i[2]:
        print(f'Path {i[0]}, Folders {i[1]} and no files.')
    else:
        print(f'Path {i[0]}, Folders {i[1]} and Files {i[2]}')

all_files = []
for files in a:
    for file in files[2]:
        if file: all_files.append(file)

all_files

