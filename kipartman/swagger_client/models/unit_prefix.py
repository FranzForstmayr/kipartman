# coding: utf-8

"""
    Kipartman

    Kipartman api specifications

    OpenAPI spec version: 1.0.0
    Contact: --
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UnitPrefix(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'symbol': 'str',
        'power': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'symbol': 'symbol',
        'power': 'power'
    }

    def __init__(self, id=None, name=None, symbol=None, power=None):
        """
        UnitPrefix - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._symbol = None
        self._power = None

        self.id = id
        self.name = name
        self.symbol = symbol
        self.power = power

    @property
    def id(self):
        """
        Gets the id of this UnitPrefix.

        :return: The id of this UnitPrefix.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UnitPrefix.

        :param id: The id of this UnitPrefix.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UnitPrefix.

        :return: The name of this UnitPrefix.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnitPrefix.

        :param name: The name of this UnitPrefix.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def symbol(self):
        """
        Gets the symbol of this UnitPrefix.

        :return: The symbol of this UnitPrefix.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this UnitPrefix.

        :param symbol: The symbol of this UnitPrefix.
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")

        self._symbol = symbol

    @property
    def power(self):
        """
        Gets the power of this UnitPrefix.

        :return: The power of this UnitPrefix.
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        """
        Sets the power of this UnitPrefix.

        :param power: The power of this UnitPrefix.
        :type: str
        """
        if power is None:
            raise ValueError("Invalid value for `power`, must not be `None`")

        self._power = power

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UnitPrefix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
