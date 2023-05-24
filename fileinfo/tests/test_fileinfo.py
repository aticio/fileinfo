#!/usr/bin/env python

"""Tests for `fileinfo` package."""

from fileinfo.fileinfo import FileInfo
from unittest.mock import patch


def test_init():
    filename = "somefile.ext"
    fi = FileInfo(filename)
    assert fi.filename == filename


def test_init_relative():
    filename = "somefile.ext"
    relative_path = "../{}".format(filename)
    fi = FileInfo(relative_path)
    assert fi.filename == filename


def test_get_info():
    filename = "somefile.ext"
    original_path = "../{}".format(filename)

    with patch("os.path.abspath") as abspath_mock:
        test_abspath = "some/abs/path"
        abspath_mock.return_value = test_abspath
        fi = FileInfo(original_path)
        assert fi.get_info() == (filename, original_path, test_abspath)
