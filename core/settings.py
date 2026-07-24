from PySide2.QtCore import QSettings


class AppSettings:

    def __init__(self):

        self.settings = QSettings(
            "Cybertron",
            "CybertronAI"
        )


    def save_window(self, window):

        self.settings.setValue(
            "geometry",
            window.saveGeometry()
        )

        self.settings.setValue(
            "window_state",
            window.saveState()
        )

        # Save splitter sizes if it exists
        if hasattr(window, "main_splitter"):

            self.settings.setValue(
                "splitter_sizes",
                window.main_splitter.saveState()
            )


    def restore_window(self, window):

        geometry = self.settings.value(
            "geometry"
        )

        state = self.settings.value(
            "window_state"
        )


        if geometry:

            window.restoreGeometry(
                geometry
            )


        if state:

            window.restoreState(
                state
            )


        # Restore splitter sizes
        if hasattr(window, "main_splitter"):

            splitter = self.settings.value(
                "splitter_sizes"
            )

            if splitter:

                window.main_splitter.restoreState(
                    splitter
                )


settings = AppSettings()
