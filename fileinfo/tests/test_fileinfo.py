#!/usr/bin/env python

"""Tests for `fileinfo` package."""

from fileinfo.fileinfo import fileinfo

def test_init():
    filename = "somefile.ext"
    fi = FileInfo(filename)
    assert fi.filename == filename


def test_init_relative():
    filename = "somefile.ext"
    relative_path = "../{}".format(filename)
    fi = FileInfo(relative_path)
    assert fi.filename == filename