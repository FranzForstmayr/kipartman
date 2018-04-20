# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class SymbolCategoryRef(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None):
        """
        SymbolCategoryRef - a model defined in Swagger

        :param id: The id of this SymbolCategoryRef.
        :type id: int
        """
        self.swagger_types = {
            'id': int
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SymbolCategoryRef of this SymbolCategoryRef.
        :rtype: SymbolCategoryRef
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self):
        """
        Gets the id of this SymbolCategoryRef.

        :return: The id of this SymbolCategoryRef.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SymbolCategoryRef.

        :param id: The id of this SymbolCategoryRef.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
