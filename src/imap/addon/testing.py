# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import imap.addon


class ImapAddonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=imap.addon)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'imap.addon:default')


IMAP_ADDON_FIXTURE = ImapAddonLayer()


IMAP_ADDON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMAP_ADDON_FIXTURE,),
    name='ImapAddonLayer:IntegrationTesting',
)


IMAP_ADDON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMAP_ADDON_FIXTURE,),
    name='ImapAddonLayer:FunctionalTesting',
)


IMAP_ADDON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IMAP_ADDON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ImapAddonLayer:AcceptanceTesting',
)
