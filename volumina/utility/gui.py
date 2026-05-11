###############################################################################
#   volumina: volume slicing and editing library
#
#       Copyright (C) 2011-2026, the ilastik developers
#                                <team@ilastik.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the Lesser GNU General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# See the files LICENSE.lgpl2 and LICENSE.lgpl3 for full text of the
# GNU Lesser General Public License version 2.1 and 3 respectively.
# This information is also available on the ilastik web site at:
# 		   http://ilastik.org/license/
###############################################################################
from typing import Optional, Union

from qtpy.QtCore import Qt, QSize
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QApplication


def dpr():
    return QApplication.instance().devicePixelRatio()


def em():
    """DPI-aware UI sizing unit based on current font metrics, similar to CSS 'em'.
    Preferred base unit for specifying sizes of UI elements"""
    return QApplication.instance().fontMetrics().ascent()


def line_height():
    """Like `em` but includes descent (slightly larger). Better for vertical spacing/layout."""
    return QApplication.instance().fontMetrics().height()


def phys(logical):
    """Convert a logical pixel value to physical pixels on this device.
    To be avoided, but sometimes necessary to work around Qt scaling quirks."""
    return round(logical * dpr())


def scale_pixmap(pixmap: QPixmap, size: QSize):
    pixmap = pixmap.scaled(
        size,
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation,
    )
    pixmap.setDevicePixelRatio(dpr())
    return pixmap
