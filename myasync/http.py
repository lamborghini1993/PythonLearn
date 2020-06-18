# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 14:53:08
@UpdateDate: 2019-09-20 15:28:05
@Description: 
    Simple example querying HTTP headers of the URL passed on the command line
'''

import asyncio
import sys
import urllib.parse


async def print_http_headers(url: str):
    url = urllib.parse.urlsplit(url)
    if url.scheme == "https":
        reader, writer = await asycnio.open_connection(url.hostname, 443, ssl=True)
    else:
        reader, writer = await asycnio.open_connection(url.hostname, 80)
    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )
    writer.write(query.encode("latin-1"))
    while True:
        line = await reader.readline()
        if not line:
            break
        line = line.decode("latin1").rstrip()
        if line:
            print(f"Http header > {line}")

    writer.close()

url = sys.argv[1]
asyncio.run(print_http_headers(url))
