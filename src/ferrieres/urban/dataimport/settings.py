# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.access.settings import AccessImporterFromImportSettings


class FerrieresImporterSettingsForm(ImporterSettingsForm):
    """ """

class FerrieresImporterSettings(ImporterSettings):
    """ """
    form = FerrieresImporterSettingsForm


class FerrieresImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = FerrieresImporterSettings


