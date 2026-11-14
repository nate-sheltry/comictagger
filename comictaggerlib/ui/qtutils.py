"""Some utilities for the GUI"""

from __future__ import annotations

import io
import logging
import traceback

from comictaggerlib.graphics import graphics_path

logger = logging.getLogger(__name__)

try:
    from PyQt5 import QtGui, QtWidgets

    qt_available = True
except ImportError:
    qt_available = False

if qt_available:
    try:
        from PIL import Image, ImageOps, ImageQt
        import pillow_jxl
        pil_available = True
    except ImportError:
        pil_available = False

    def reduce_widget_font_size(widget: QtWidgets.QWidget, delta: int = 2) -> None:
        f = widget.font()
        if f.pointSize() > 10:
            f.setPointSize(f.pointSize() - delta)
        widget.setFont(f)

    def center_window_on_screen(window: QtWidgets.QWidget) -> None:
        """Center the window on screen.

        This implementation will handle the window
        being resized or the screen resolution changing.
        """
        # Get the current screens' dimensions...
        screen = QtGui.QGuiApplication.primaryScreen().geometry()
        # The horizontal position is calculated as (screen width - window width) / 2
        hpos = int((screen.width() - window.width()) / 2)
        # And vertical position the same, but with the height dimensions
        vpos = int((screen.height() - window.height()) / 2)
        # And the move call repositions the window
        window.move(hpos, vpos)

    def center_window_on_parent(window: QtWidgets.QWidget) -> None:

        top_level = window
        while top_level.parent() is not None:
            parent = top_level.parent()
            if isinstance(parent, QtWidgets.QWidget):
                top_level = parent

        # Get the current screens' dimensions...
        main_window_size = top_level.geometry()
        # ... and get this windows' dimensions
        # The horizontal position is calculated as (screen width - window width) / 2
        hpos = int((main_window_size.width() - window.width()) / 2)
        # And vertical position the same, but with the height dimensions
        vpos = int((main_window_size.height() - window.height()) / 2)
        # And the move call repositions the window
        window.move(hpos + main_window_size.left(), vpos + main_window_size.top())

    def get_qimage_from_data(image_data: bytes) -> QtGui.QImage:
        img = QtGui.QImage()
        # First try Qt's installed image decoders.
        if img.loadFromData(image_data):
            return img
        if pil_available:
            try:
                with Image.open(io.BytesIO(image_data)) as source:
                    source.seek(0)
                    rgba = ImageOps.exif_transpose(source).convert("RGBA")
                    width, height = rgba.size
                    pixels = rgba.tobytes("raw", "RGBA")
                    img = QtGui.QImage(
                        pixels,
                        width,
                        height,
                        width * 4,
                        QtGui.QImage.Format_RGBA8888,
                    ).copy()
                if not img.isNull():
                    return img
            except Exception:
                logger.exception("Pillow failed to decode the page image.")
        # if still nothing, go with default image
        img = QtGui.QImage()
        if not img.load(str(graphics_path / "nocover.png")):
            logger.error("Could not load fallback image")
        return img

    def qt_error(msg: str, e: Exception | None = None) -> None:
        trace = ""
        if e:
            trace = "\n".join(traceback.format_exception(type(e), e, e.__traceback__))

        QtWidgets.QMessageBox.critical(QtWidgets.QMainWindow(), "Error", msg + trace)
