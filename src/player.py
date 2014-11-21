from gi.repository import Gst
from gi.repository import GLib
from sys import argv
import os


TEST = os.path.expanduser('~/Music/deadlock-code-of-honor.mp3')


class Playlist:
    _playlist = []
    _current = None

    def __contains__(self, fname):
        return fname in self._playlist

    def __delitem__(self, pos):
        del self._playlist[pos]

    def __getitem__(self, pos):
        return self._playlist[pos]

    def __len__(self):
        return len(self._playlist)

    def __setitem__(self, pos, fname):
        self._playlist[pos] = fname

    def _next(self):
        total_tracks = len(self._playlist)
        if total_tracks == 0 or self._current == total_tracks - 1:
            self._current = None
        else:
            self._current += 1

        return self.current()

    def _prev(self):
        total_tracks = len(self._playlist)
        if total_tracks == 0 or self._current == 0:
            self._current = None
        else:
            self._current -= 1
        return self.current()

    def current(self):
        return self._playlist[self._current]

    def jump(self, pos):
        assert 0 <= pos < len(self._playlist)
        self._current = pos
        return self.current()

    def add(self, fname, pos=-1):
        assert os.path.abspath(fname)
        self._playlist.insert(pos, fname)


class Player:
    playlist = Playlist()

    def play(self, pos=0):
        fname = self.playlist.jump(pos)
        uri = Gst.filename_to_uri(fname)
        playbin = Gst.ElementFactory.make('playbin', 'playbin')
        #bus = playbin.get_bus()
        #bus.add_signal_watch()
        playbin.set_property('uri', uri)
        playbin.set_state(Gst.State.PLAYING)


Gst.init(argv)
p = Player()
p.playlist.add(TEST)
p.play()

loop = GLib.MainLoop()
loop.run()
