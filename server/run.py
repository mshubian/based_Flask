# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------
# Copyright (c) Yovole network tech info (Shanghai) Co. Ltd.  All rights reserved.
# -----------------------------------------------------------------------------------

#!flask/bin/python

from server import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
