from core.cyber import cyber
from core.session import session


class Controller:

    def send(

        self,

        text

    ):

        session.user(

            text

        )

        response = cyber.ask(

            text

        )

        session.cyber(

            response

        )

        return response


controller = Controller()
