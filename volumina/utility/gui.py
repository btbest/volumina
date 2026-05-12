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
from qtpy.QtCore import Qt, QSize
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QApplication


def line_height() -> int:
    """
    Physical pixels per text line at font display size on this display.
    Similar to CSS 'em', this serves as a base unit for specifying sizes of UI elements.
    Typically around 13 on laptop or older screens, or around 30 on 4K screens."""
    return QApplication.instance().fontMetrics().height()


def dpr() -> float:
    """Device display scaling factor.
    On Win, corresponds to display scaling setting (e.g. 150%, 200% -> 1.5, 2.0)."""
    return QApplication.instance().devicePixelRatio()


def phys(logical) -> int:
    """Convert a logical pixel value to physical pixels on this device.
    To be avoided, but sometimes necessary to work around Qt scaling quirks."""
    return round(logical * dpr())


def scale_pixmap(pixmap: QPixmap, size: QSize) -> QPixmap:
    pixmap = pixmap.scaled(
        size,
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation,
    )
    pixmap.setDevicePixelRatio(dpr())
    return pixmap
