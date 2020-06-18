# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 14:11:05
@UpdateDate: 2019-09-20 14:12:04
@Description: 
'''

import asyncio
import datetime
import time


async def display_date():
    end_time = time.time() + 5
    while True:
        print(datetime.datetime.now())
        if (time.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())
