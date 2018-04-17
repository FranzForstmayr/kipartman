# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.footprint_category_data import FootprintCategoryData
from swagger_server.models.footprint_category_ref import FootprintCategoryRef
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class FootprintCategoryNew(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, parent=None):
        """
        FootprintCategoryNew - a model defined in Swagger

        :param name: The name of this FootprintCategoryNew.
        :type name: str
        :param description: The description of this FootprintCategoryNew.
        :type description: str
        :param parent: The parent of this FootprintCategoryNew.
        :type parent: FootprintCategoryRef
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'parent': FootprintCategoryRef
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'parent': 'parent'
        }

        self._name = name
        self._description = description
        self._parent = parent

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FootprintCategoryNew of this FootprintCategoryNew.
        :rtype: FootprintCategoryNew
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this FootprintCategoryNew.

        :return: The name of this FootprintCategoryNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FootprintCategoryNew.

        :param name: The name of this FootprintCategoryNew.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FootprintCategoryNew.

        :return: The description of this FootprintCategoryNew.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FootprintCategoryNew.

        :param description: The description of this FootprintCategoryNew.
        :type description: str
        """

        self._description = description

    @property
    def parent(self):
        """
        Gets the parent of this FootprintCategoryNew.

        :return: The parent of this FootprintCategoryNew.
        :rtype: FootprintCategoryRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this FootprintCategoryNew.

        :param parent: The parent of this FootprintCategoryNew.
        :type parent: FootprintCategoryRef
        """

        self._parent = parent

