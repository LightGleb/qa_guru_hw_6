import os
import zipfile
import pytest
import shutil

from paths import RESOURCE_DIR, TMP_DIR


@pytest.fixture(scope="session", autouse=True)
def packing_files_into_archive():
    if not os.path.exists('resource'):  # проверяем существует ли папка
        os.mkdir('resource')  # создаем папку если её нет
    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, "archive.zip"), 'w') as zf:  # создаем архив
        for file in os.listdir(TMP_DIR):  # добавляем файлы в архив
            zf.write(os.path.join(TMP_DIR, file), file)  # добавляем файл в архив

    yield
    shutil.rmtree(RESOURCE_DIR)  # удаляем папку со всеми файлами и подпапками
