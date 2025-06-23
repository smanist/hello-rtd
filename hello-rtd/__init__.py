"""
A microscopic demo library used only to prove that Read the Docs can
install the package, import it, and build API docs via autodoc.
"""

__all__ = ["say_hello"]


def say_hello(name: str = "RTD") -> str:
    """
    Return a friendly greeting.

    Parameters
    ----------
    name
        Person or thing to greet.

    Examples
    --------
    >>> say_hello("World")
    'Hello, World!'
    """
    return f"Hello, {name}!"
