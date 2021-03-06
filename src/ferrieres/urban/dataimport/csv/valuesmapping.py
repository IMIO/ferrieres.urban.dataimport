# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

    'division_map': {
        '1ère': '1',
        '2ème': '2',
        '3ème': '3',
        '4ème': '4',
        '5ème': '5',
        '5me': '5',
    },

    'eventtype_id_map': table({
        'header'             : ['decision_event'],
        'BuildLicence'       : ['delivrance-du-permis-octroi-ou-refus'],
        'ParcelOutLicence'   : ['delivrance-du-permis-octroi-ou-refus'],
        'Declaration'        : ['deliberation-college'],
        'UrbanCertificateOne': ['octroi-cu1'],
        'UrbanCertificateTwo': ['octroi-cu2'],
        'MiscDemand'         : ['deliberation-college'],
        'EnvClassOne'        : ['decision'],
        'EnvClassTwo'        : ['desision'],
        'EnvClassThree'      : ['acceptation-de-la-demande'],
    }),
}