# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.agorawin.importer import AgorawinDataImporter
from ferrieres.urban.dataimport.interfaces import IFerrieresDataImporter


class FerrieresDataImporter(AgorawinDataImporter):
    """ """

    implements(IFerrieresDataImporter)
