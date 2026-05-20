# -*- coding: utf-8 -*-
"""
@File    : 文档
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/5/19 21:56
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

from langchain_community.document_loaders import UnstructuredExcelLoader, PyPDFLoader
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "test.xlsx"

loader = UnstructuredExcelLoader(file_path)
docs = loader.load()

print(type(loader))
print(type(docs))
print(len(docs))
print(type(docs[0]))
print(docs[0].page_content)
print(docs[0].metadata)
print("-"* 20)

file_path = "test0.pdf"

loader = PyPDFLoader(file_path)
docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)