from collections import deque


class QueueTask:

    def __init__(
        self,
        name,
        callback,
        *args,
        **kwargs
    ):

        self.name = name

        self.callback = callback

        self.args = args

        self.kwargs = kwargs

        self.completed = False

        self.result = None



class ExecutionQueue:

    def __init__(self):

        self.queue = deque()

        self.history = []



    def add_task(

        self,

        name,

        callback,

        *args,

        **kwargs

    ):

        self.queue.append(

            QueueTask(

                name,

                callback,

                *args,

                **kwargs

            )

        )



    def run(self):

        results = []


        while self.queue:


            task = self.queue.popleft()


            print(

                f"[QUEUE] {task.name}"

            )


            task.result = task.callback(

                *task.args,

                **task.kwargs

            )


            task.completed = True


            self.history.append(

                task

            )


            results.append(

                task.result

            )


        return results



    def pending(self):

        return len(

            self.queue

        )



    def completed(self):

        return len(

            self.history

        )



    def clear(self):

        self.queue.clear()



    def report(self):

        report = []


        for task in self.history:

            report.append(

                {

                    "task": task.name,

                    "completed": task.completed

                }

            )


        return report



execution_queue = ExecutionQueue()
