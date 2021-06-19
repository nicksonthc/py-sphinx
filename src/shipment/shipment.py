class Shipment:
    def __init__(self,type="Truck") -> None:
        """
        Args:
        type (str):  ['Truck','Freight','Air','Nickson Express'] 
        
        Returns:
        
            Shipment object 
            None 
            
        """  
        if type in ['Truck','Freight','Air','Nickson Express'] :
            self.type = type
        else :
            return None

    def confirmShipment(self):
        """ Trigger multiple ::member routine to ochestration services

        .. note::

            Won't imported ::member function to markup docs.

        1. self._requestQuote(self)

        2. self._agreeShippingIncoterms(self)

        3. self._issueCommercialInvoice(self)

        Args:
            self (Shipment): the constructor object
        
        Returns:
            bool.  The return code:: 
                0 -- False

                1 -- True

        """
        self._requestQuote(self)
        self._agreeShippingIncoterms(self)
        self._issueCommercialInvoice(self)

        return True 
    

    def _requestQuote(self):
        """ Trigger ochestration services. """
        return True

    def _agreeShippingIncoterms(self):
        """ Trigger ochestration services. """
        return True

    def _issueCommercialInvoice(self):
        """ Trigger ochestration services. """
        return True


def helper_one():
    " Without doc string"

    
def helper_two(name='nickson'):
    """This function does something with input args.

    Args:
       name (str):  The name to use.

    Kwargs:
       state (bool): Current state to be in.

    Returns:
       int.  The return code::

          0 -- Success!
          1 -- No good.
          2 -- Try again.

    Raises:
       AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> helper_two(name='nickson')
    0

    """
    return 0

