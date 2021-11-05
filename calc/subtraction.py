
"""This is the subtraction calculation that is being inherits
the value A and value B from the calculation class"""
#this is called a namespace it is like files and
# folders the classes are files and the folders organize the classes
#It looks like a folder and file path but it is sort
# of a virtual representation of how the program is organized

"""This is subtraction operation object"""

from calc.calculation import Calculation

class Subtraction(Calculation):
    """This is subtraction class"""
    def get_result(self):
        """This is subtraction class"""
        return self.value_a - self.value_b