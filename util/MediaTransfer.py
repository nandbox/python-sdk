import datetime

import requests


def download_file(token, media_file_id, saving_dir_path, saving_file_name, download_server_url):
    downloadStartTime = datetime.datetime.now()
    savingDirPath = saving_dir_path if saving_dir_path is not None else './'
    mediaFileFullPath = f'{savingDirPath}/{saving_file_name}'
    headers = {
        'Content-Type': 'application/json',
        'X-TOKEN': token
    }
    r = requests.get(download_server_url + media_file_id, allow_redirects=True, headers=headers, timeout=30000)
    downloadEndTime = datetime.datetime.now()
    open(mediaFileFullPath, 'wb').write(r.content)
    print(f'Downloaded file {media_file_id} took around {(downloadEndTime - downloadStartTime) / 1000} seconds')
    print('File saved locally successfully')


def upload_file(token, media_file_full_path):
    pass
