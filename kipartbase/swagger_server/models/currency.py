# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Currency(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, symbol=None, base=None, ratio=None):
        """
        Currency - a model defined in Swagger

        :param name: The name of this Currency.
        :type name: str
        :param symbol: The symbol of this Currency.
        :type symbol: str
        :param base: The base of this Currency.
        :type base: str
        :param ratio: The ratio of this Currency.
        :type ratio: float
        """
        self.swagger_types = {
            'name': str,
            'symbol': str,
            'base': str,
            'ratio': float
        }

        self.attribute_map = {
            'name': 'name',
            'symbol': 'symbol',
            'base': 'base',
            'ratio': 'ratio'
        }

        self._name = name
        self._symbol = symbol
        self._base = base
        self._ratio = ratio

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Currency of this Currency.
        :rtype: Currency
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this Currency.

        :return: The name of this Currency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Currency.

        :param name: The name of this Currency.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def symbol(self):
        """
        Gets the symbol of this Currency.

        :return: The symbol of this Currency.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this Currency.

        :param symbol: The symbol of this Currency.
        :type symbol: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")

        self._symbol = symbol

    @property
    def base(self):
        """
        Gets the base of this Currency.

        :return: The base of this Currency.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """
        Sets the base of this Currency.

        :param base: The base of this Currency.
        :type base: str
        """
        if base is None:
            raise ValueError("Invalid value for `base`, must not be `None`")

        self._base = base

    @property
    def ratio(self):
        """
        Gets the ratio of this Currency.

        :return: The ratio of this Currency.
        :rtype: float
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """
        Sets the ratio of this Currency.

        :param ratio: The ratio of this Currency.
        :type ratio: float
        """
        if ratio is None:
            raise ValueError("Invalid value for `ratio`, must not be `None`")

        self._ratio = ratio

