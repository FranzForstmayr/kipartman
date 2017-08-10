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


class Part(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, octopart=None, updated=None, id=None, category=None, has_childs=None, childs=None, footprint=None, model=None, parameters=None, distributors=None, manufacturers=None):
        """
        Part - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'comment': 'str',
            'octopart': 'str',
            'updated': 'datetime',
            'id': 'int',
            'category': 'PartCategory',
            'has_childs': 'int',
            'childs': 'list[Part]',
            'footprint': 'Footprint',
            'model': 'Model',
            'parameters': 'list[PartParameter]',
            'distributors': 'list[PartDistributor]',
            'manufacturers': 'list[PartManufacturer]'
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
            'footprint': 'footprint',
            'model': 'model',
            'parameters': 'parameters',
            'distributors': 'distributors',
            'manufacturers': 'manufacturers'
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
        self._footprint = footprint
        self._model = model
        self._parameters = parameters
        self._distributors = distributors
        self._manufacturers = manufacturers

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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: datetime
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
        :type: int
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
        :type: PartCategory
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
        :type: int
        """

        self._has_childs = has_childs

    @property
    def childs(self):
        """
        Gets the childs of this Part.

        :return: The childs of this Part.
        :rtype: list[Part]
        """
        return self._childs

    @childs.setter
    def childs(self, childs):
        """
        Sets the childs of this Part.

        :param childs: The childs of this Part.
        :type: list[Part]
        """

        self._childs = childs

    @property
    def footprint(self):
        """
        Gets the footprint of this Part.

        :return: The footprint of this Part.
        :rtype: Footprint
        """
        return self._footprint

    @footprint.setter
    def footprint(self, footprint):
        """
        Sets the footprint of this Part.

        :param footprint: The footprint of this Part.
        :type: Footprint
        """

        self._footprint = footprint

    @property
    def model(self):
        """
        Gets the model of this Part.

        :return: The model of this Part.
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Part.

        :param model: The model of this Part.
        :type: Model
        """

        self._model = model

    @property
    def parameters(self):
        """
        Gets the parameters of this Part.

        :return: The parameters of this Part.
        :rtype: list[PartParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Part.

        :param parameters: The parameters of this Part.
        :type: list[PartParameter]
        """

        self._parameters = parameters

    @property
    def distributors(self):
        """
        Gets the distributors of this Part.

        :return: The distributors of this Part.
        :rtype: list[PartDistributor]
        """
        return self._distributors

    @distributors.setter
    def distributors(self, distributors):
        """
        Sets the distributors of this Part.

        :param distributors: The distributors of this Part.
        :type: list[PartDistributor]
        """

        self._distributors = distributors

    @property
    def manufacturers(self):
        """
        Gets the manufacturers of this Part.

        :return: The manufacturers of this Part.
        :rtype: list[PartManufacturer]
        """
        return self._manufacturers

    @manufacturers.setter
    def manufacturers(self, manufacturers):
        """
        Sets the manufacturers of this Part.

        :param manufacturers: The manufacturers of this Part.
        :type: list[PartManufacturer]
        """

        self._manufacturers = manufacturers

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
        if not isinstance(other, Part):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
