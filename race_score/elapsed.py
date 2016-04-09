"""
Almost all chip timing systems report their results in time of day (TOD).
Therefore, some logic must exist to calculate the elapsed times that will be
used to rank the participants.

Obviously, some timing systems, such as a stopwatch, will record elapsed time.
Many chip timing sysems will allow you to set the start time such that the
clock starts at '00:00:00.00' at the beginning of the race. However, split
times, and staggered starts for large events often make these capabilities
useless.
"""
from __future__ import unicode_literals
from __future__ import absolute_import


class Elapsed(object):

    """
    Logic for converting TOD to elapsed times.

    Attributes:
        rules (list): Rules for elapsed time conversions.
    """

    def __init__(self):
        """Initialize."""
        self.rules = []
        self.field_map = []

    def set_field_map(self, field_map):
        """Set the map of field attribute/property names to Ids which will be
        used in the equation. The map is ordered such that the list item
        proceeding the current item can be assumed to be cronologically before
        the current item.

        We will use the order of the items to compute "replacement" elapsed
        times when missing a "starting" value for our equation.

        Args:
            field_map (list): List of (id, field name).
        """
        self.field_map = field_map

    def _parse_equation(self, equation):
        """Given an equation and the known mapping of item data to
        attribute/property names, return a function which will produce the
        expected result.

        Args:
            equation (string): Equation which should be used to calculate the
                elapsed time.

        Returns:
            function: Routine which will be used to calculate results.
        """
        return lambda x: 0

    def set_rule(self, name, equation):
        """Set a rule for converting TOD to elapsed time.

        Args:
            name (string): Name of the field where the elapsed time will be
                recorded.
            equation (string): Equation which should be used to calculate the
                elapsed time.
        """
        self.rules.append((name, equation))

    def _process_item(self, item):
        """Process an item to generate suitable elapsed time values based on
        specified rules and existing TOD values.

        Args:
            item (object): Item for which we want to copute elapsed times.

        Returns:
            Item with attributes/properites for generated elapsed times.
        """
        for rule in self.rules:
            elapsed = rule[1](item)
            try:
                item.setattr(rule[0], elapsed)
            except AttributeError:
                item[rule[0]] = elapsed
        return item

    def process(self, items):
        """Given a list or generator, yield each item after processing them to
        generate suitable elapsed time values.

        Args:
            items (list): List or generator which yields items to convert
                elapsed time values for.

        Yields:
            Item with attributes/properites for generated elapsed times.
        """
        for item in items:
            yield self._process_item(item)

