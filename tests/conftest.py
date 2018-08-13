import os
from io import BytesIO

import pytest
from PIL import Image
from zds_client import Client

from .constants import BASE_DIR

CONFIG_FILE = os.path.join(BASE_DIR, 'config.yml')

Client.load_config(BASE_DIR, CONFIG_FILE)

_zrc_client = Client('zrc')
_drc_client = Client('drc')
_ztc_client = Client('ztc')
_orc_client = Client('orc')


@pytest.fixture
def text_file(request):
    """
    Generate a temporary '.txt' file.

    Returns file as a file opened in binary read mode.
    Use .read() function to get file content as bytes.
    """

    PATH = 'dummy.txt'
    with open(PATH, 'w') as tmp:
        tmp.write('some additional information')
    data = open(PATH, 'rb')

    def fin():
        data.close()
        os.remove(PATH)

    request.addfinalizer(fin)
    return data


@pytest.fixture
def png_file(request):
    """
    Generate a temporary '.png' image.

    Returns file as a 'BytesIO' object.
    Use .getvalue() to get image content as bytes.
    """
    im_format = 'png'
    im = Image.new('RGB', (1, 1), 'blue')  # only 1 blue pixel
    buffered = BytesIO()
    im.save(buffered, format=im_format)
    return buffered


@pytest.fixture
def zrc_client():
    return _zrc_client


@pytest.fixture
def drc_client():
    return _drc_client


@pytest.fixture
def ztc_client():
    return _ztc_client


@pytest.fixture
def orc_client():
    return _orc_client
