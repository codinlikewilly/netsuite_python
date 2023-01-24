# coding: utf-8

# flake8: noqa

"""
    NetSuite REST API

    NetSuite REST Record API generated 2023-01-18 at 19:40:11 UTC for account 472052, user will@theapiguys.com with role Keap Integration.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@netsuite.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from netsuite.swagger_client.api.contact_api import ContactApi
from netsuite.swagger_client.api.customer_api import CustomerApi
# import ApiClient
from netsuite.swagger_client.api_client import ApiClient
from netsuite.swagger_client.configuration import Configuration
# import models into sdk package
from netsuite.swagger_client.models.contact import Contact
from netsuite.swagger_client.models.contact_collection import ContactCollection
from netsuite.swagger_client.models.contact_custom_form import ContactCustomForm
from netsuite.swagger_client.models.customer import Customer
from netsuite.swagger_client.models.customer_address_book_address_book_address import CustomerAddressBookAddressBookAddress
from netsuite.swagger_client.models.customer_address_book_collection import CustomerAddressBookCollection
from netsuite.swagger_client.models.customer_address_book_element import CustomerAddressBookElement
from netsuite.swagger_client.models.customer_alcohol_recipient_type import CustomerAlcoholRecipientType
from netsuite.swagger_client.models.customer_campaigns_collection import CustomerCampaignsCollection
from netsuite.swagger_client.models.customer_campaigns_element import CustomerCampaignsElement
from netsuite.swagger_client.models.customer_collection import CustomerCollection
from netsuite.swagger_client.models.customer_contact_roles_collection import CustomerContactRolesCollection
from netsuite.swagger_client.models.customer_contact_roles_element import CustomerContactRolesElement
from netsuite.swagger_client.models.customer_custom_form import CustomerCustomForm
from netsuite.swagger_client.models.customer_email_preference import CustomerEmailPreference
from netsuite.swagger_client.models.customer_global_subscription_status import CustomerGlobalSubscriptionStatus
from netsuite.swagger_client.models.customer_group_pricing_collection import CustomerGroupPricingCollection
from netsuite.swagger_client.models.customer_group_pricing_element import CustomerGroupPricingElement
from netsuite.swagger_client.models.customer_item_pricing_collection import CustomerItemPricingCollection
from netsuite.swagger_client.models.customer_item_pricing_element import CustomerItemPricingElement
from netsuite.swagger_client.models.customer_language import CustomerLanguage
from netsuite.swagger_client.models.customer_negative_number_format import CustomerNegativeNumberFormat
from netsuite.swagger_client.models.customer_number_format import CustomerNumberFormat
from netsuite.swagger_client.models.customer_shipping_carrier import CustomerShippingCarrier
from netsuite.swagger_client.models.customer_symbol_placement import CustomerSymbolPlacement
from netsuite.swagger_client.models.customer_third_party_carrier import CustomerThirdPartyCarrier
from netsuite.swagger_client.models.customeraddress_bookaddress_book_address_country import CustomeraddressBookaddressBookAddressCountry
from netsuite.swagger_client.models.ns_error import NsError
from netsuite.swagger_client.models.ns_error_oerror_details import NsErrorOerrorDetails
from netsuite.swagger_client.models.ns_link import NsLink
from netsuite.swagger_client.models.ns_resource import NsResource
from netsuite.swagger_client.models.ns_resource_collection import NsResourceCollection
from netsuite.swagger_client.models.one_ofcontact_company import OneOfcontactCompany
from netsuite.swagger_client.models.one_ofcontact_custentity_course_attended import OneOfcontactCustentityCourseAttended
from netsuite.swagger_client.models.one_ofcontact_custentity_energy_eff_attended import OneOfcontactCustentityEnergyEffAttended
from netsuite.swagger_client.models.one_ofcontact_custentity_hitachi_course_attended import OneOfcontactCustentityHitachiCourseAttended
from netsuite.swagger_client.models.one_ofcontact_custentity_hp_course_attended import OneOfcontactCustentityHpCourseAttended
from netsuite.swagger_client.models.one_ofcontact_custentity_pv_course_atteneded import OneOfcontactCustentityPvCourseAtteneded
from netsuite.swagger_client.models.one_ofcontact_custentity_sol_course_attended import OneOfcontactCustentitySolCourseAttended
from netsuite.swagger_client.models.one_ofcontact_custentity_unvent_hot_water_g3 import OneOfcontactCustentityUnventHotWaterG3
from netsuite.swagger_client.models.one_ofcontact_custentity_water_regulations1999 import OneOfcontactCustentityWaterRegulations1999
from netsuite.swagger_client.models.one_ofcustomer_custentity_course_attended import OneOfcustomerCustentityCourseAttended
from netsuite.swagger_client.models.one_ofcustomer_custentity_energy_eff_attended import OneOfcustomerCustentityEnergyEffAttended
from netsuite.swagger_client.models.one_ofcustomer_custentity_hitachi_course_attended import OneOfcustomerCustentityHitachiCourseAttended
from netsuite.swagger_client.models.one_ofcustomer_custentity_hp_course_attended import OneOfcustomerCustentityHpCourseAttended
from netsuite.swagger_client.models.one_ofcustomer_custentity_pv_course_atteneded import OneOfcustomerCustentityPvCourseAtteneded
from netsuite.swagger_client.models.one_ofcustomer_custentity_sol_course_attended import OneOfcustomerCustentitySolCourseAttended
from netsuite.swagger_client.models.one_ofcustomer_custentity_unvent_hot_water_g3 import OneOfcustomerCustentityUnventHotWaterG3
from netsuite.swagger_client.models.one_ofcustomer_custentity_water_regulations1999 import OneOfcustomerCustentityWaterRegulations1999
from netsuite.swagger_client.models.one_ofcustomer_item_pricing_element_item import OneOfcustomerItemPricingElementItem
