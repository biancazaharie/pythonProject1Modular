# from test import test_service, test_service2
# test_service2()
from console_ui import ConsoleUI
from service import Service

if __name__ == '__main__':
    service = Service()
    console_ui = ConsoleUI(service)
    console_ui.run()