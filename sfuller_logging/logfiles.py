import logging
import logging.handlers
import os

def setup_logs(filename, toaddrs, manual_path=False):
    import os
    print(os.getcwd())
    
    if manual_path:
        filepath = f"{manual_path}{filename}.log"
    elif toaddrs="sebastian.fuller@captify.co.uk":
        filepath = f"/home/sebastian_fuller/log/{filename}.log"
    elif toaddrs="business.insights@captify.co.uk":
        filepath = f"/home/andrea_tonali/log/{filename}.log"
    else:
        filepath = f"{filename}.log"
    
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

    log_file = logging.getLogger("file")

    return log_file, log_email
