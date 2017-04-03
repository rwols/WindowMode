import sublime_plugin

class EventListener(sublime_plugin.EventListener):
    """Displays the mode of each window in the status bar. One of "FILE MODE",
    "FOLDER MODE" or "PROJECT MODE"."""

    def on_new(self, view):
        # \x01 is the "start of heading" non-printable character in ASCII.
        # Sublime uses the status key for ordering purposes and doesn't print
        # it anywhere, so this works fine. We use \x01 to make sure that the
        # status is the left-most item in the status bar.
        STATUS_KEY = '\x01WindowMode'
        window = view.window()
        if not window:
            return
        if window.project_data():
            status = 'PROJECT_MODE' if window.project_file_name() else 'FOLDER_MODE'
        else:
            status = 'FILE MODE'
        view.set_status(STATUS_KEY, status)

    def on_clone(self, view):
        self.on_new(view)

    def on_load(self, view):
        self.on_new(view)

    def on_activated(self, view):
        self.on_new(view)
