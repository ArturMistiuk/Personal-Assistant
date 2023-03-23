def input_error(func):
    # Decorator for exit

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "This record is not exist"
        except ValueError:
            return "This record is not correct!"
        except IndexError:
            return "This command is wrong"

    return wrapper
