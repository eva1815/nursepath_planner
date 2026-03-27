from controllers.application_controller import ApplicationController
from repositories.init_db import initialize_database


if __name__ == "__main__":
    initialize_database()
    controller = ApplicationController()
    controller.run()
