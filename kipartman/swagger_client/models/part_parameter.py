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


class PartParameter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, unit=None, numeric=None, text_value=None, min_value=None, min_prefix=None, nom_value=None, nom_prefix=None, max_value=None, max_prefix=None):
        """
        PartParameter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'unit': 'Unit',
            'numeric': 'bool',
            'text_value': 'str',
            'min_value': 'float',
            'min_prefix': 'UnitPrefix',
            'nom_value': 'float',
            'nom_prefix': 'UnitPrefix',
            'max_value': 'float',
            'max_prefix': 'UnitPrefix'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'unit': 'unit',
            'numeric': 'numeric',
            'text_value': 'text_value',
            'min_value': 'min_value',
            'min_prefix': 'min_prefix',
            'nom_value': 'nom_value',
            'nom_prefix': 'nom_prefix',
            'max_value': 'max_value',
            'max_prefix': 'max_prefix'
        }

        self._name = name
        self._description = description
        self._unit = unit
        self._numeric = numeric
        self._text_value = text_value
        self._min_value = min_value
        self._min_prefix = min_prefix
        self._nom_value = nom_value
        self._nom_prefix = nom_prefix
        self._max_value = max_value
        self._max_prefix = max_prefix

    @property
    def name(self):
        """
        Gets the name of this PartParameter.

        :return: The name of this PartParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PartParameter.

        :param name: The name of this PartParameter.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PartParameter.

        :return: The description of this PartParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PartParameter.

        :param description: The description of this PartParameter.
        :type: str
        """

        self._description = description

    @property
    def unit(self):
        """
        Gets the unit of this PartParameter.

        :return: The unit of this PartParameter.
        :rtype: Unit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this PartParameter.

        :param unit: The unit of this PartParameter.
        :type: Unit
        """

        self._unit = unit

    @property
    def numeric(self):
        """
        Gets the numeric of this PartParameter.

        :return: The numeric of this PartParameter.
        :rtype: bool
        """
        return self._numeric

    @numeric.setter
    def numeric(self, numeric):
        """
        Sets the numeric of this PartParameter.

        :param numeric: The numeric of this PartParameter.
        :type: bool
        """

        self._numeric = numeric

    @property
    def text_value(self):
        """
        Gets the text_value of this PartParameter.

        :return: The text_value of this PartParameter.
        :rtype: str
        """
        return self._text_value

    @text_value.setter
    def text_value(self, text_value):
        """
        Sets the text_value of this PartParameter.

        :param text_value: The text_value of this PartParameter.
        :type: str
        """

        self._text_value = text_value

    @property
    def min_value(self):
        """
        Gets the min_value of this PartParameter.

        :return: The min_value of this PartParameter.
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """
        Sets the min_value of this PartParameter.

        :param min_value: The min_value of this PartParameter.
        :type: float
        """

        self._min_value = min_value

    @property
    def min_prefix(self):
        """
        Gets the min_prefix of this PartParameter.

        :return: The min_prefix of this PartParameter.
        :rtype: UnitPrefix
        """
        return self._min_prefix

    @min_prefix.setter
    def min_prefix(self, min_prefix):
        """
        Sets the min_prefix of this PartParameter.

        :param min_prefix: The min_prefix of this PartParameter.
        :type: UnitPrefix
        """

        self._min_prefix = min_prefix

    @property
    def nom_value(self):
        """
        Gets the nom_value of this PartParameter.

        :return: The nom_value of this PartParameter.
        :rtype: float
        """
        return self._nom_value

    @nom_value.setter
    def nom_value(self, nom_value):
        """
        Sets the nom_value of this PartParameter.

        :param nom_value: The nom_value of this PartParameter.
        :type: float
        """

        self._nom_value = nom_value

    @property
    def nom_prefix(self):
        """
        Gets the nom_prefix of this PartParameter.

        :return: The nom_prefix of this PartParameter.
        :rtype: UnitPrefix
        """
        return self._nom_prefix

    @nom_prefix.setter
    def nom_prefix(self, nom_prefix):
        """
        Sets the nom_prefix of this PartParameter.

        :param nom_prefix: The nom_prefix of this PartParameter.
        :type: UnitPrefix
        """

        self._nom_prefix = nom_prefix

    @property
    def max_value(self):
        """
        Gets the max_value of this PartParameter.

        :return: The max_value of this PartParameter.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """
        Sets the max_value of this PartParameter.

        :param max_value: The max_value of this PartParameter.
        :type: float
        """

        self._max_value = max_value

    @property
    def max_prefix(self):
        """
        Gets the max_prefix of this PartParameter.

        :return: The max_prefix of this PartParameter.
        :rtype: UnitPrefix
        """
        return self._max_prefix

    @max_prefix.setter
    def max_prefix(self, max_prefix):
        """
        Sets the max_prefix of this PartParameter.

        :param max_prefix: The max_prefix of this PartParameter.
        :type: UnitPrefix
        """

        self._max_prefix = max_prefix

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
        if not isinstance(other, PartParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
