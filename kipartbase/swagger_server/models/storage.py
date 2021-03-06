# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.storage_category import StorageCategory
from swagger_server.models.storage_data import StorageData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Storage(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, id=None, category=None):
        """
        Storage - a model defined in Swagger

        :param name: The name of this Storage.
        :type name: str
        :param description: The description of this Storage.
        :type description: str
        :param comment: The comment of this Storage.
        :type comment: str
        :param id: The id of this Storage.
        :type id: int
        :param category: The category of this Storage.
        :type category: StorageCategory
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'id': int,
            'category': StorageCategory
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'id': 'id',
            'category': 'category'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._id = id
        self._category = category

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Storage of this Storage.
        :rtype: Storage
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this Storage.

        :return: The name of this Storage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Storage.

        :param name: The name of this Storage.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Storage.

        :return: The description of this Storage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Storage.

        :param description: The description of this Storage.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this Storage.

        :return: The comment of this Storage.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Storage.

        :param comment: The comment of this Storage.
        :type comment: str
        """

        self._comment = comment

    @property
    def id(self):
        """
        Gets the id of this Storage.

        :return: The id of this Storage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Storage.

        :param id: The id of this Storage.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def category(self):
        """
        Gets the category of this Storage.

        :return: The category of this Storage.
        :rtype: StorageCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Storage.

        :param category: The category of this Storage.
        :type category: StorageCategory
        """

        self._category = category

