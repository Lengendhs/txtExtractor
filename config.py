#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6628610020:AAGvOUZSMROgMJubPJk5qFQc2lTgg330xhY")
    API_ID = int(os.environ.get("API_ID", "22278147"))
    API_HASH = os.environ.get("API_HASH", "379775c2b8cda0ccf30784963f300111)
    AUTH_USERS = os.environ.get("AUTH_USERS", "6813146748")
