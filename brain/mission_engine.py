import threading
import time

from brain.planner import planner


class MissionEngine:

    def __init__(self):

        self.running = False

        self.paused = False

        self.thread = None

        self.callbacks = []

    def load_plan(self, plan):

        planner.active_plan = plan

    def add_callback(self, callback):

        self.callbacks.append(callback)

    def notify(self):

        for callback in self.callbacks:

            try:

                callback(planner.active_plan)

            except Exception as e:

                print(e)

    def start(self):

        if planner.active_plan is None:

            return False

        if self.running:

            return False

        self.running = True

        self.paused = False

        self.thread = threading.Thread(

            target=self._run,

            daemon=True

        )

        self.thread.start()

        return True

    def pause(self):

        self.paused = True

    def resume(self):

        self.paused = False

    def stop(self):

        self.running = False

    def is_running(self):

        return self.running

    def _run(self):

        while self.running:

            if self.paused:

                time.sleep(0.1)

                continue

            task = planner.current_task()

            if task is None:

                break

            self.notify()

            print(f"Running: {task.title}")

            if task.action:

                try:

                    task.action()

                except Exception as e:

                    print(e)

            planner.complete_current()

            self.notify()

            time.sleep(0.5)

        self.running = False

        self.notify()


mission_engine = MissionEngine()
