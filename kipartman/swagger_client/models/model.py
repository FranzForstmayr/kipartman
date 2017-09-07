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


class Model(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, snapeda=None, id=None, category=None, image=None, model=None):
        """
        Model - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'comment': 'str',
            'snapeda': 'str',
            'id': 'int',
            'category': 'ModelCategory',
            'image': 'UploadFile',
            'model': 'UploadFile'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'snapeda': 'snapeda',
            'id': 'id',
            'category': 'category',
            'image': 'image',
            'model': 'model'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._snapeda = snapeda
        self._id = id
        self._category = category
        self._image = image
        self._model = model

    @property
    def name(self):
        """
        Gets the name of this Model.

        :return: The name of this Model.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Model.

        :param name: The name of this Model.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Model.

        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Model.

        :param description: The description of this Model.
        :type: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this Model.

        :return: The comment of this Model.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Model.

        :param comment: The comment of this Model.
        :type: str
        """

        self._comment = comment

    @property
    def snapeda(self):
        """
        Gets the snapeda of this Model.

        :return: The snapeda of this Model.
        :rtype: str
        """
        return self._snapeda

    @snapeda.setter
    def snapeda(self, snapeda):
        """
        Sets the snapeda of this Model.

        :param snapeda: The snapeda of this Model.
        :type: str
        """

        self._snapeda = snapeda

    @property
    def id(self):
        """
        Gets the id of this Model.

        :return: The id of this Model.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Model.

        :param id: The id of this Model.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def category(self):
        """
        Gets the category of this Model.

        :return: The category of this Model.
        :rtype: ModelCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Model.

        :param category: The category of this Model.
        :type: ModelCategory
        """

        self._category = category

    @property
    def image(self):
        """
        Gets the image of this Model.

        :return: The image of this Model.
        :rtype: UploadFile
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Model.

        :param image: The image of this Model.
        :type: UploadFile
        """

        self._image = image

    @property
    def model(self):
        """
        Gets the model of this Model.

        :return: The model of this Model.
        :rtype: UploadFile
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Model.

        :param model: The model of this Model.
        :type: UploadFile
        """

        self._model = model

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
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other