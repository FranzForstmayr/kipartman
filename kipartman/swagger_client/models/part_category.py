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


class PartCategory(object):
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
        'name': 'str',
        'description': 'str',
        'id': 'int',
        'parent': 'PartCategoryRef',
        'childs': 'list[PartCategory]',
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'parent': 'parent',
        'childs': 'childs',
        'path': 'path'
    }

    def __init__(self, name=None, description=None, id=None, parent=None, childs=None, path=None):
        """
        PartCategory - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._id = None
        self._parent = None
        self._childs = None
        self._path = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        self.id = id
        if parent is not None:
          self.parent = parent
        if childs is not None:
          self.childs = childs
        if path is not None:
          self.path = path

    @property
    def name(self):
        """
        Gets the name of this PartCategory.

        :return: The name of this PartCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PartCategory.

        :param name: The name of this PartCategory.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PartCategory.

        :return: The description of this PartCategory.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PartCategory.

        :param description: The description of this PartCategory.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this PartCategory.

        :return: The id of this PartCategory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartCategory.

        :param id: The id of this PartCategory.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def parent(self):
        """
        Gets the parent of this PartCategory.

        :return: The parent of this PartCategory.
        :rtype: PartCategoryRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this PartCategory.

        :param parent: The parent of this PartCategory.
        :type: PartCategoryRef
        """

        self._parent = parent

    @property
    def childs(self):
        """
        Gets the childs of this PartCategory.

        :return: The childs of this PartCategory.
        :rtype: list[PartCategory]
        """
        return self._childs

    @childs.setter
    def childs(self, childs):
        """
        Sets the childs of this PartCategory.

        :param childs: The childs of this PartCategory.
        :type: list[PartCategory]
        """

        self._childs = childs

    @property
    def path(self):
        """
        Gets the path of this PartCategory.

        :return: The path of this PartCategory.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this PartCategory.

        :param path: The path of this PartCategory.
        :type: str
        """

        self._path = path

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
        if not isinstance(other, PartCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
