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


class StorageCategory(object):
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
        'parent': 'StorageCategoryRef',
        'childs': 'list[StorageCategory]',
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
        StorageCategory - a model defined in Swagger
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
        Gets the name of this StorageCategory.

        :return: The name of this StorageCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StorageCategory.

        :param name: The name of this StorageCategory.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this StorageCategory.

        :return: The description of this StorageCategory.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StorageCategory.

        :param description: The description of this StorageCategory.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this StorageCategory.

        :return: The id of this StorageCategory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StorageCategory.

        :param id: The id of this StorageCategory.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def parent(self):
        """
        Gets the parent of this StorageCategory.

        :return: The parent of this StorageCategory.
        :rtype: StorageCategoryRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageCategory.

        :param parent: The parent of this StorageCategory.
        :type: StorageCategoryRef
        """

        self._parent = parent

    @property
    def childs(self):
        """
        Gets the childs of this StorageCategory.

        :return: The childs of this StorageCategory.
        :rtype: list[StorageCategory]
        """
        return self._childs

    @childs.setter
    def childs(self, childs):
        """
        Sets the childs of this StorageCategory.

        :param childs: The childs of this StorageCategory.
        :type: list[StorageCategory]
        """

        self._childs = childs

    @property
    def path(self):
        """
        Gets the path of this StorageCategory.

        :return: The path of this StorageCategory.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this StorageCategory.

        :param path: The path of this StorageCategory.
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
        if not isinstance(other, StorageCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
