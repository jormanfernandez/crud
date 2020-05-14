from datetime import datetime
import os

messageTypes = {
    1: "[INFO]",
    2: "[WARNING]",
    3: "[ERROR]"
}

prepends = {
    1: "\x1b[0;0;0m",
    2: "\x1b[1;33;40m",
    3: "\x1b[1;31;40m"
}

def Log(message, level=1, file="api", req=None):
    """
    Displays different levels of warnings
    
    Args:
        message (str): The message to be shown
        file (str): File where the log will be written
        req (Falcon HTTP Request Object): Falcon request object to extrapolate data for the log
        level (int): The type of message to be show.
                     1 - Info type
                     2 - Warning type
                     3 - Error type
    Returns:
        None
    """

    now = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
    msgType = messageTypes[level] if level in messageTypes else messageTypes[1]
    prepend = prepends[level] if level in prepends else prepends[1]
    ip = " " if req is None else f" ({req.remote_addr}) "
    text = f"{now} - {msgType}:{ip}{message}"

    print(f"{prepend} {text} {prepends[1]} \n")
    if file is not None:
        LogInFile(text, file)

def LogInFile(message, file):
    """
    Store in a log file a specific message
    
    Args:
        message (str): The message to be stored
        file (str): File where the log will be written
    Returns:
        None
    """
    scriptPath = os.path.dirname(__file__)
    logPath = os.path.join(scriptPath, f"../../../logs/{file}.log")

    logger = open(logPath, "a")
    logger.write(f"{message}\n")
    logger.close()
