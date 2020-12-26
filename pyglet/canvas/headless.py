# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# Copyright (c) 2008-2020 pyglet contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

from pyglet import app
from .base import Display, Screen, ScreenMode, Canvas


from pyglet.egl import egl


class HeadlessDisplay(Display):

    def __init__(self):
        super().__init__()
        # TODO: fix this placeholder:
        self._screens = [HeadlessScreen(self, 0, 0, 1920, 1080)]
        display = egl.EGLNativeDisplayType()
        self._display_connection = egl.eglGetDisplay(display)
        egl.eglInitialize(self._display_connection, None, None)

    def get_screens(self):
        return self._screens

    def __del__(self):
        egl.eglTerminate(self._display_connection)


class HeadlessCanvas(Canvas):
    def __init__(self, display, egl_surface):
        super(HeadlessCanvas, self).__init__(display)
        self.egl_surface = egl_surface

class HeadlessScreen(Screen):
    def __init__(self, display, x, y, width, height):
        super().__init__(display, x, y, width, height)

    def get_matching_configs(self, template):
        canvas = HeadlessCanvas(self.display, None)
        configs = template.match(canvas)
        # XXX deprecate
        for config in configs:
            config.screen = self
        # print("Canvas", canvas, "configs", configs)
        return configs

    def get_modes(self):
        pass

    def get_mode(self):
        pass

    def set_mode(self, mode):
        pass

    def restore_mode(self):
        pass
