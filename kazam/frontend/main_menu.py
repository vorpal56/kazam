# -*- coding: utf-8 -*-
#
#       main_menu.py
#
#       Copyright 2012 David Klasinc <bigwhale@lubica.net>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from gettext import gettext as _

from gi.repository import Gtk, GObject

MENUBAR = """
<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.38.2 -->
<interface>
  <requires lib="gtk+" version="3.24"/>
  <object class="GtkMenuBar" id="MenuBar">
    <property name="visible">True</property>
    <property name="can-focus">False</property>
    <child>
      <object class="GtkMenuItem">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <property name="label" translatable="yes">_File</property>
        <property name="use-underline">True</property>
        <child type="submenu">
          <object class="GtkMenu">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <child>
              <object class="GtkMenuItem" id="FilePreferences">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <property name="label">_Preferences</property>
                <property name="use-underline">True</property>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="FileQuit">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <property name="label">_Quit</property>
                <property name="use-underline">True</property>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <property name="label" translatable="yes">_Help</property>
        <property name="use-underline">True</property>
        <child type="submenu">
          <object class="GtkMenu">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <child>
              <object class="GtkMenuItem" id="HelpAbout">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <property name="label">_About</property>
                <property name="use-underline">True</property>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="HelpHelp">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <property name="label">_Help</property>
                <property name="use-underline">True</property>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
"""


class MainMenu(GObject.GObject):
    __gsignals__ = {
        "file-preferences" : (GObject.SIGNAL_RUN_LAST,
                              None,
                              (),
                             ),
        "file-quit" : (GObject.SIGNAL_RUN_LAST,
                           None,
                           (),
                           ),
        "help-help" : (GObject.SIGNAL_RUN_LAST,
                             None,
                             (),
                             ),
        "help-about" : (GObject.SIGNAL_RUN_LAST,
                             None,
                             (),
                             ),
    }

    def __init__(self):
        GObject.GObject.__init__(self)

        self.builder = Gtk.Builder()
        self.builder.add_from_string(MENUBAR)
        self.builder.get_object('HelpHelp').connect('activate', self.cb_help_help)
        self.builder.get_object('HelpAbout').connect('activate', self.cb_help_about)
        self.builder.get_object('FilePreferences').connect('activate', self.cb_file_preferences)
        self.builder.get_object('FileQuit').connect('activate', self.cb_file_quit)
        self.menubar = self.builder.get_object("MenuBar")


    def cb_file_quit(self, action):
        self.emit("file-quit")

    def cb_file_preferences(self, action):
        self.emit("file-preferences")

    def cb_help_help(self, action):
        self.emit("help-help")

    def cb_help_about(self, action):
        self.emit("help-about")
