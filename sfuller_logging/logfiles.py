import logging
import logging.handlers
import os
from datetime import datetime

def setup_logs(filename, toaddrs, manual_path=False):  
    if manual_path:
        filepath = f"{manual_path}{filename}.log"
    else:
        filepath = f"{os.getcwd()}/log/{filename}.log"
    
    logging.basicConfig(filename=filepath,
                        format='%(levelname)s: %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.gmail.com", 587),
                                                fromaddr=os.getenv("GOOGLE_EMAIL"), 
                                                toaddrs=[toaddrs],
                                                credentials=(os.getenv("GOOGLE_EMAIL"), os.getenv("GOOGLE_PASSWORD")),
                                                secure=(),
                                                subject=f"{filename} failed to run"
                                            )

    log_email = logging.getLogger("email")
    log_email.addHandler(smtp_handler)
    log_email.setLevel(logging.ERROR)

    class PrintToConsole:
        def info(self, txt):
            now = datetime.now()
            current_time = now.strftime("%Y/%m/%d %H:%M:%S")
            print(f"{current_time}: {txt}")

    log_file = PrintToConsole()

    return log_file, log_email
