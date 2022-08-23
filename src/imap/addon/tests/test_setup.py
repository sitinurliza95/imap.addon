# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from imap.addon.testing import IMAP_ADDON_INTEGRATION_TESTING  # noqa: E501

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that imap.addon is properly installed."""

    layer = IMAP_ADDON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if imap.addon is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'imap.addon'))

    def test_browserlayer(self):
        """Test that IImapAddonLayer is registered."""
        from plone.browserlayer import utils

        from imap.addon.interfaces import IImapAddonLayer
        self.assertIn(
            IImapAddonLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IMAP_ADDON_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('imap.addon')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if imap.addon is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'imap.addon'))

    def test_browserlayer_removed(self):
        """Test that IImapAddonLayer is removed."""
        from plone.browserlayer import utils

        from imap.addon.interfaces import IImapAddonLayer
        self.assertNotIn(IImapAddonLayer, utils.registered_layers())
