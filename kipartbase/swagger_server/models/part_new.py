# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.footprint_ref import FootprintRef
from swagger_server.models.model_ref import ModelRef
from swagger_server.models.part_category_ref import PartCategoryRef
from swagger_server.models.part_data import PartData
from swagger_server.models.part_distributor import PartDistributor
from swagger_server.models.part_manufacturer import PartManufacturer
from swagger_server.models.part_parameter import PartParameter
from swagger_server.models.part_ref import PartRef
from swagger_server.models.part_storage import PartStorage
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PartNew(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, comment=None, octopart=None, updated=None, category=None, childs=None, footprint=None, model=None, parameters=None, distributors=None, manufacturers=None, storages=None):
        """
        PartNew - a model defined in Swagger

        :param name: The name of this PartNew.
        :type name: str
        :param description: The description of this PartNew.
        :type description: str
        :param comment: The comment of this PartNew.
        :type comment: str
        :param octopart: The octopart of this PartNew.
        :type octopart: str
        :param updated: The updated of this PartNew.
        :type updated: datetime
        :param category: The category of this PartNew.
        :type category: PartCategoryRef
        :param childs: The childs of this PartNew.
        :type childs: List[PartRef]
        :param footprint: The footprint of this PartNew.
        :type footprint: FootprintRef
        :param model: The model of this PartNew.
        :type model: ModelRef
        :param parameters: The parameters of this PartNew.
        :type parameters: List[PartParameter]
        :param distributors: The distributors of this PartNew.
        :type distributors: List[PartDistributor]
        :param manufacturers: The manufacturers of this PartNew.
        :type manufacturers: List[PartManufacturer]
        :param storages: The storages of this PartNew.
        :type storages: List[PartStorage]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'comment': str,
            'octopart': str,
            'updated': datetime,
            'category': PartCategoryRef,
            'childs': List[PartRef],
            'footprint': FootprintRef,
            'model': ModelRef,
            'parameters': List[PartParameter],
            'distributors': List[PartDistributor],
            'manufacturers': List[PartManufacturer],
            'storages': List[PartStorage]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'comment': 'comment',
            'octopart': 'octopart',
            'updated': 'updated',
            'category': 'category',
            'childs': 'childs',
            'footprint': 'footprint',
            'model': 'model',
            'parameters': 'parameters',
            'distributors': 'distributors',
            'manufacturers': 'manufacturers',
            'storages': 'storages'
        }

        self._name = name
        self._description = description
        self._comment = comment
        self._octopart = octopart
        self._updated = updated
        self._category = category
        self._childs = childs
        self._footprint = footprint
        self._model = model
        self._parameters = parameters
        self._distributors = distributors
        self._manufacturers = manufacturers
        self._storages = storages

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PartNew of this PartNew.
        :rtype: PartNew
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this PartNew.

        :return: The name of this PartNew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PartNew.

        :param name: The name of this PartNew.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PartNew.

        :return: The description of this PartNew.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PartNew.

        :param description: The description of this PartNew.
        :type description: str
        """

        self._description = description

    @property
    def comment(self):
        """
        Gets the comment of this PartNew.

        :return: The comment of this PartNew.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this PartNew.

        :param comment: The comment of this PartNew.
        :type comment: str
        """

        self._comment = comment

    @property
    def octopart(self):
        """
        Gets the octopart of this PartNew.

        :return: The octopart of this PartNew.
        :rtype: str
        """
        return self._octopart

    @octopart.setter
    def octopart(self, octopart):
        """
        Sets the octopart of this PartNew.

        :param octopart: The octopart of this PartNew.
        :type octopart: str
        """

        self._octopart = octopart

    @property
    def updated(self):
        """
        Gets the updated of this PartNew.

        :return: The updated of this PartNew.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this PartNew.

        :param updated: The updated of this PartNew.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def category(self):
        """
        Gets the category of this PartNew.

        :return: The category of this PartNew.
        :rtype: PartCategoryRef
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this PartNew.

        :param category: The category of this PartNew.
        :type category: PartCategoryRef
        """

        self._category = category

    @property
    def childs(self):
        """
        Gets the childs of this PartNew.

        :return: The childs of this PartNew.
        :rtype: List[PartRef]
        """
        return self._childs

    @childs.setter
    def childs(self, childs):
        """
        Sets the childs of this PartNew.

        :param childs: The childs of this PartNew.
        :type childs: List[PartRef]
        """

        self._childs = childs

    @property
    def footprint(self):
        """
        Gets the footprint of this PartNew.

        :return: The footprint of this PartNew.
        :rtype: FootprintRef
        """
        return self._footprint

    @footprint.setter
    def footprint(self, footprint):
        """
        Sets the footprint of this PartNew.

        :param footprint: The footprint of this PartNew.
        :type footprint: FootprintRef
        """

        self._footprint = footprint

    @property
    def model(self):
        """
        Gets the model of this PartNew.

        :return: The model of this PartNew.
        :rtype: ModelRef
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this PartNew.

        :param model: The model of this PartNew.
        :type model: ModelRef
        """

        self._model = model

    @property
    def parameters(self):
        """
        Gets the parameters of this PartNew.

        :return: The parameters of this PartNew.
        :rtype: List[PartParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this PartNew.

        :param parameters: The parameters of this PartNew.
        :type parameters: List[PartParameter]
        """

        self._parameters = parameters

    @property
    def distributors(self):
        """
        Gets the distributors of this PartNew.

        :return: The distributors of this PartNew.
        :rtype: List[PartDistributor]
        """
        return self._distributors

    @distributors.setter
    def distributors(self, distributors):
        """
        Sets the distributors of this PartNew.

        :param distributors: The distributors of this PartNew.
        :type distributors: List[PartDistributor]
        """

        self._distributors = distributors

    @property
    def manufacturers(self):
        """
        Gets the manufacturers of this PartNew.

        :return: The manufacturers of this PartNew.
        :rtype: List[PartManufacturer]
        """
        return self._manufacturers

    @manufacturers.setter
    def manufacturers(self, manufacturers):
        """
        Sets the manufacturers of this PartNew.

        :param manufacturers: The manufacturers of this PartNew.
        :type manufacturers: List[PartManufacturer]
        """

        self._manufacturers = manufacturers

    @property
    def storages(self):
        """
        Gets the storages of this PartNew.

        :return: The storages of this PartNew.
        :rtype: List[PartStorage]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        """
        Sets the storages of this PartNew.

        :param storages: The storages of this PartNew.
        :type storages: List[PartStorage]
        """

        self._storages = storages

