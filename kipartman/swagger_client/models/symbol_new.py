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


class SymbolNew(object):
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
        'comment': 'str',
        'snapeda': 'str',
        'snapeda_uid': 'str',
        'updated': 'datetime',
        'category': 'SymbolCategoryRef',
        'image': 'UploadFileRef',
        'symbol': 'UploadFileRef'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'comment': 'comment',
        'snapeda': 'snapeda',
        'snapeda_uid': 'snapeda_uid',
        'updated': 'updated',
        'category': 'category',
        'image': 'image',
        'symbol': 'Symbol'
    }

    def __init__(self, name=None, description=None, comment=None, snapeda=None, snapeda_uid=None, updated=None, category=None, image=None, symbol=None):
        """
        SymbolNew - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._comment = None
        self._snapeda = None
        self._snapeda_uid = None
        self._updated = None
        self._category = None
        self._image = None
        self._symbol = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if comment is not None:
          self.comment = comment
        if snapeda is not None:
          self.snapeda = snapeda
        if snapeda_uid is not None:
          self.snapeda_uid = snapeda_uid
        if updated is not None:
          self.updated = updated
        if category is not None:
          self.category = category
        if image is not None:
          self.image = image
        if symbol is not None:
          self.symbol = symbol

    @property
    def name(self):
        """
        Gets the name of this SymbolNew.

        :return: The name of this SymbolNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SymbolNew.

        :param name: The name of this SymbolNew.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SymbolNew.

        :return: The description of this SymbolNew.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SymbolNew.

        :param description: The description of this SymbolNew.
        :type: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this SymbolNew.

        :return: The comment of this SymbolNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this SymbolNew.

        :param comment: The comment of this SymbolNew.
        :type: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this SymbolNew.

        :return: The snapeda of this SymbolNew.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this SymbolNew.

        :param snapeda: The snapeda of this SymbolNew.
        :type: str
        """

        self._snapeda = snapeda

    @property
    def snapeda_uid(self):
        """
        Gets the snapeda_uid of this SymbolNew.

        :return: The snapeda_uid of this SymbolNew.
        :rtype: str
        """
        return self._snapeda_uid

    @snapeda_uid.setter
    def snapeda_uid(self, snapeda_uid):
        """
        Sets the snapeda_uid of this SymbolNew.

        :param snapeda_uid: The snapeda_uid of this SymbolNew.
        :type: str
        """

        self._snapeda_uid = snapeda_uid

    @property
    def updated(self):
        """
        Gets the updated of this SymbolNew.

        :return: The updated of this SymbolNew.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this SymbolNew.

        :param updated: The updated of this SymbolNew.
        :type: datetime
        """

        self._updated = updated

    @property
    def category(self):
        """
        Gets the category of this SymbolNew.

        :return: The category of this SymbolNew.
        :rtype: SymbolCategoryRef
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this SymbolNew.

        :param category: The category of this SymbolNew.
        :type: SymbolCategoryRef
        """

        self._category = category

    @property
    def image(self):
        """
        Gets the image of this SymbolNew.

        :return: The image of this SymbolNew.
        :rtype: UploadFileRef
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this SymbolNew.

        :param image: The image of this SymbolNew.
        :type: UploadFileRef
        """

        self._image = image

    @property
    def symbol(self):
        """
        Gets the symbol of this SymbolNew.

        :return: The symbol of this SymbolNew.
        :rtype: UploadFileRef
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this SymbolNew.

        :param symbol: The symbol of this SymbolNew.
        :type: UploadFileRef
        """

        self._symbol = symbol

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
        if not isinstance(other, SymbolNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other