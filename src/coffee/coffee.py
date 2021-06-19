"""
.. module:: coffee
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: nick <nicksonthc@gmail.com>


"""

# def public_fn_with_googley_docstring(name, state=None):
#     """This function does something.

#     Args:
#        name (str):  The name to use.

#     Kwargs:
#        state (bool): Current state to be in.

#     Returns:
#        int.  The return code::

#           0 -- Success!
#           1 -- No good.
#           2 -- Try again.

#     Raises:
#        AttributeError, KeyError

#     A really great idea.  A way you might use me is

#     >>> print public_fn_with_googley_docstring(name='foo', state=None)
#     0

#     BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

#     """
#     return 0

# def public_fn_with_sphinxy_docstring(name, state=None):
#     """This function does something.

#     :param name: The name to use.
#     :type name: str.
#     :param state: Current state to be in.
#     :type state: bool.
#     :returns:  int -- the return code.
#     :raises: AttributeError, KeyError

#     """
#     return 0


# def _private_fn_with_docstring(foo, bar='baz', foobarbas=None):
#     """I have a docstring, but won't be imported if you just use ``:members:``.
#     """
#     return None


class Brewing(object):
    """We use this as a public class example class.

    You never call this class before calling :func:`coffee.purchase module.`.

    .. note::

       You need ready your damn beans for this class.

    """

    def __init__(self, barista:object, making:str='drip')->None:
        """A really simple class.

        Args:
           barista (object): inject object dependency

        Kwargs:
           making (str): default brewing lor

        """
        self._barista = barista
        self._making = making

    def pour_water(self, capacity:float, container:str='glass')->bool:
        """This gets the water to ready

        This really should have a full function definition, but I am too lazy.

        >>> print pour_water(200)
        200, 'glass'
        >>> print pour_water(300, 'jar')
        300, 'jar'

        Isn't that what you want?

        """
        return True

    def get_coffee(self, guest:bool):
        """A private function to get coffee.

        This really should have a full function definition, but I am too lazy.

        """
        return self

