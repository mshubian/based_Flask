# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------------
# Copyright (c) Yovole network tech info (Shanghai) Co. Ltd.  All rights reserved.
# -----------------------------------------------------------------------------------

__author__ = 'hubian'


class VM:
    OS_TYPE_LINUX = 0
    OS_TYPE_WINDOWS = 1


class NETWORK:
    IP_TYPE_PUBLIC = 0
    IP_TYPE_PRIVATE = 1


class DISK:
    TYPE_SYSTEM = 0
    TYPE_MOUNTED = 1

    FORMAT_NTFS = 0
    FORMAT_EXT4 = 1


class IMAGE:
    TYPE_DEFAULT = 0  # Router or Monitor
    TYPE_PROVIDER = 1  # vm images type
    TYPE_CUSTOMIZE = 2   # created by users
