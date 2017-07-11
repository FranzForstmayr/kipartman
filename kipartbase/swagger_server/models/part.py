# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.part_category import PartCategory
from swagger_server.models.part_data import PartData
from swagger_server.models.part_manufacturer import PartManufacturer
from swagger_server.models.part_parameter import PartParameter
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Part(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, octopart=None, updated=None, id=None, category=None, has_childs=None, childs=None, parameters=None, distributors=None):
        """
        Part - a model defined in Swagger

        :param name: The name of this Part.
        :type name: str
        :param description: The description of this Part.
        :type description: str
        :param comment: The comment of this Part.
        :type comment: str
        :param octopart: The octopart of this Part.
        :type octopart: str
        :param updated: The updated of this Part.
        :type updated: datetime
        :param id: The id of this Part.
        :type id: int
        :param category: The category of this Part.
        :type category: PartCategory
        :param has_childs: The has_childs of this Part.
        :type has_childs: int
        :param childs: The childs of this Part.
        :type childs: List[Part]
        :param parameters: The parameters of this Part.
        :type parameters: List[PartParameter]
        :param distributors: The distributors of this Part.
        :type distributors: List[PartManufacturer]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'octopart': str,
            'updated': datetime,
            'id': int,
            'category': PartCategory,
            'has_childs': int,
            'childs': List[Part],
            'parameters': List[PartParameter],
            'distributors': List[PartManufacturer]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'octopart': 'octopart',
            'updated': 'updated',
            'id': 'id',
            'category': 'category',
            'has_childs': 'has_childs',
            'childs': 'childs',
            'parameters': 'parameters',
            'distributors': 'distributors'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._octopart = octopart
        self._updated = updated
        self._id = id
        self._category = category
        self._has_childs = has_childs
        self._childs = childs
        self._parameters = parameters
        self._distributors = distributors

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Part of this Part.
        :rtype: Part
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this Part.

        :return: The name of this Part.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Part.

        :param name: The name of this Part.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Part.

        :return: The description of this Part.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Part.

        :param description: The description of this Part.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this Part.

        :return: The comment of this Part.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Part.

        :param comment: The comment of this Part.
        :type comment: str
        """

        self._comment = comment

    @property
    def octopart(self):
        """
        Gets the octopart of this Part.

        :return: The octopart of this Part.
        :rtype: str
        """
        return self._octopart

    @octopart.setter
    def octopart(self, octopart):
        """
        Sets the octopart of this Part.

        :param octopart: The octopart of this Part.
        :type octopart: str
        """

        self._octopart = octopart

    @property
    def updated(self):
        """
        Gets the updated of this Part.

        :return: The updated of this Part.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Part.

        :param updated: The updated of this Part.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this Part.

        :return: The id of this Part.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Part.

        :param id: The id of this Part.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def category(self):
        """
        Gets the category of this Part.

        :return: The category of this Part.
        :rtype: PartCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Part.

        :param category: The category of this Part.
        :type category: PartCategory
        """

        self._category = category

    @property
    def has_childs(self):
        """
        Gets the has_childs of this Part.

        :return: The has_childs of this Part.
        :rtype: int
        """
        return self._has_childs

    @has_childs.setter
    def has_childs(self, has_childs):
        """
        Sets the has_childs of this Part.

        :param has_childs: The has_childs of this Part.
        :type has_childs: int
        """

        self._has_childs = has_childs

    @property
    def childs(self):
        """
        Gets the childs of this Part.

        :return: The childs of this Part.
        :rtype: List[Part]
        """
        return self._childs

    @childs.setter
    def childs(self, childs):
        """
        Sets the childs of this Part.

        :param childs: The childs of this Part.
        :type childs: List[Part]
        """

        self._childs = childs

    @property
    def parameters(self):
        """
        Gets the parameters of this Part.

        :return: The parameters of this Part.
        :rtype: List[PartParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Part.

        :param parameters: The parameters of this Part.
        :type parameters: List[PartParameter]
        """

        self._parameters = parameters

    @property
    def distributors(self):
        """
        Gets the distributors of this Part.

        :return: The distributors of this Part.
        :rtype: List[PartManufacturer]
        """
        return self._distributors

    @distributors.setter
    def distributors(self, distributors):
        """
        Sets the distributors of this Part.

        :param distributors: The distributors of this Part.
        :type distributors: List[PartManufacturer]
        """

        self._distributors = distributors

