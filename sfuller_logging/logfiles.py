import logging
import logging.handlers
import os

def setup_logs(filename, toaddrs):
    logging.basicConfig(filename=filename,
                        format='%(levelname)s: %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.gmail.com", 587),
                                                fromaddr=os.getenv("GOOGLE_EMAIL"), 
                                                toaddrs=[toaddrs],
                                                credentials=(os.getenv("GOOGLE_EMAIL"), os.getenv("GOOGLE_PASSWORD")),
                                                secure=(),
                                                subject=f"{os.path.basename(__file__)} failed to run"
                                            )

    log_email = logging.getLogger("email")
    log_email.addHandler(smtp_handler)
    log_email.setLevel(logging.ERROR)

    log_file = logging.getLogger("file")

    return log_file, log_email
