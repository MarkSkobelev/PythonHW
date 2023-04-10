import csv
import json
import os
import pickle

__all__ = ['dir_walk']

def dir_walk(dir: str) -> None:
    res = []
    for path, direct, files in os.walk(dir, topdown=True, onerror=None, followlinks=False):
        for catalog in direct:
            dir_size = 0
            for root, cat, files_cat in os.walk(f'{path}\\{catalog}'):
                for file in files_cat:
                    dir_size += os.path.getsize(f'{root}\\{file}')
            catalogs = {'path': path, 'search': catalog, 'file_dir': 'directory',
                        'size': f'{dir_size = } bytes'}
            res.append(catalogs)
        for file in files:
            size = os.path.getsize(f'{path}\\{file}')
            f = {'path': path, 'search': file, 'file_dir': 'file', 'size': f'{size = } bytes'}
            res.append(f)

    with open('dir_walk.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=2)

    f_names = ['path', 'search', 'file_dir', 'size']
    with open('dir_walk.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=f_names)
        writer.writeheader()
        writer.writerows(res)

    with open('dir_walk.pickle', 'wb') as f:
        pickle.dump(res, f)

if __name__ == '__main__':
    dir_walk('C:\\Users\\Владелец\\Desktop\\GB\\PYTHON_23\\PythonHW\\Seminar7')

