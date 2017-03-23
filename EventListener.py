import sublime_plugin

class EventListener(sublime_plugin.EventListener):
    """Displays the mode of each window in the status bar. One of "FILE MODE",
    "FOLDER MODE" or "PROJECT MODE"."""

    def on_new(self, view):
        STATUS_KEY = '000_WindowMode'
        window = view.window()
        project = window.project_data()
        if project:
            filename = window.project_file_name()
            if filename:
                view.set_status(STATUS_KEY, 'PROJECT MODE')
            else:
                view.set_status(STATUS_KEY, 'FOLDER MODE')
            return
        else:
            view.set_status(STATUS_KEY, 'FILE MODE')

    def on_clone(self, view):
        self.on_new(view)

    def on_load(self, view):
        self.on_new(view)

    def on_activated(self, view):
        self.on_new(view)
