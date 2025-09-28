from colorama import Fore, Style, init

init(autoreset=True)

class TextStyle:

    @staticmethod
    def error(text: str) -> str:
        return f"{Fore.RED}{text}{Style.RESET_ALL}"
    
    def error2(text: str) -> str:
        return f"{Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def success(text: str) -> str:
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def list1(text: str) -> str:
        return f"{Fore.LIGHTMAGENTA_EX}{text}{Style.RESET_ALL}"

    @staticmethod
    def list2(text: str) -> str:
        return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def info(text: str) -> str:
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def warning(text: str) -> str:
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def text(text: str) -> str:
        return f"{Fore.LIGHTBLUE_EX}{text}{Style.RESET_ALL}"