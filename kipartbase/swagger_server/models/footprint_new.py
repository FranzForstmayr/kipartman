# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.footprint_category_ref import FootprintCategoryRef
from swagger_server.models.footprint_data import FootprintData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class FootprintNew(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, snapeda=None, category=None):
        """
        FootprintNew - a model defined in Swagger

        :param name: The name of this FootprintNew.
        :type name: str
        :param description: The description of this FootprintNew.
        :type description: str
        :param comment: The comment of this FootprintNew.
        :type comment: str
        :param snapeda: The snapeda of this FootprintNew.
        :type snapeda: str
        :param category: The category of this FootprintNew.
        :type category: FootprintCategoryRef
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'snapeda': str,
            'category': FootprintCategoryRef
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'snapeda': 'snapeda',
            'category': 'category'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._snapeda = snapeda
        self._category = category

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FootprintNew of this FootprintNew.
        :rtype: FootprintNew
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this FootprintNew.

        :return: The name of this FootprintNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FootprintNew.

        :param name: The name of this FootprintNew.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FootprintNew.

        :return: The description of this FootprintNew.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FootprintNew.

        :param description: The description of this FootprintNew.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this FootprintNew.

        :return: The comment of this FootprintNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this FootprintNew.

        :param comment: The comment of this FootprintNew.
        :type comment: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this FootprintNew.

        :return: The snapeda of this FootprintNew.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this FootprintNew.

        :param snapeda: The snapeda of this FootprintNew.
        :type snapeda: str
        """

        self._snapeda = snapeda

    @property
    def category(self):
        """
        Gets the category of this FootprintNew.

        :return: The category of this FootprintNew.
        :rtype: FootprintCategoryRef
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this FootprintNew.

        :param category: The category of this FootprintNew.
        :type category: FootprintCategoryRef
        """

        self._category = category
