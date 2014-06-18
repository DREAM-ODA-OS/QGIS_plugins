# -*- coding: utf-8 -*- 
#-------------------------------------------------------------------------------
#                                                                               
#  EO-WMS plugin
#                                                                               
# Project: Q-GIS EO-WMS/EO-WCS plugins
# Author:  Martin Paces <martin.paces@eox.at>                                   
#                                                                               
#-------------------------------------------------------------------------------
# Copyright (C) 2014 EOX IT Services GmbH                                       
#                                                                               
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     
# copies of the Software, and to permit persons to whom the Software is         
# furnished to do so, subject to the following conditions:                      
#                                                                               
# The above copyright notice and this permission notice shall be included in
# all
# copies of this Software or works derived from this Software.                  
#                                                                               
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN     
# THE SOFTWARE.                                                                 
#-------------------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.utils import *

# initialize Qt resources from file resouces.py
import resources

class EOWMSPlugin:

    CLIENT_LABEL="EO-WMS Client"
    ABOUT_LABEL="About"
    MENU_ITEM="EO-W&MS Client"
    WHATS_THIS="EO-WMS Client (whatsThis)"
    STATUS_TIP="EO-WMS Client (statusTip)"

    def __init__(self,iface): 
        
        # reference to the Q-GIS interface 
        self.iface = iface 

    def initGui(self): 

        # creating activation action
        self.actionClient = QAction(QIcon(":/plugins/eowms/img/eowms.png"),
                            self.CLIENT_LABEL,self.iface.mainWindow()) 
        self.actionClient.setWhatsThis(self.WHATS_THIS)
        self.actionClient.setStatusTip(self.STATUS_TIP)

        QObject.connect(self.actionClient,SIGNAL("triggered()"),self.client)

        # insert toolbar button and menu item 
        self.iface.addToolBarIcon(self.actionClient)
        self.iface.addPluginToWebMenu(self.MENU_ITEM,self.actionClient) 

        # creating the about action 

        self.actionAbout = QAction(QIcon(":/plugins/QuickWKT/about_icon.png"),
                            self.ABOUT_LABEL,self.iface.mainWindow()) 
        self.iface.addPluginToWebMenu(self.MENU_ITEM,self.actionAbout) 

        QObject.connect(self.actionAbout,SIGNAL("triggered()"),self.about)

        # insert toolbar button and menu item 
        #self.iface.addPluginToRasterMenu(self.MENU_ITEM,self.action) 
        #self.iface.addPluginToWebMenu(self.MENU_ITEM,self.action) 

        # register canvas painter to listen to the draw signal 
        #QObject.connect( self.iface.mapCanvas(),
        #        SIGNAL("renderComplete(QPainter *)"), self.renderer )

    def unload(self): 

        # remove toolbar button and menu item 
        self.iface.removePluginWebMenu(self.MENU_ITEM,self.actionClient)
        self.iface.removePluginWebMenu(self.MENU_ITEM,self.actionAbout) 
        self.iface.removeToolBarIcon(self.actionClient)

        # unregister canvas painter 
        #QObject.disconnect (self.iface.mapCanvas(),
        #        SIGNAL("renderComplete(QPainter *)"), self.renderer )

    
    def about(self): 
        """ Open the 'About' information box. """ 

        info = QCoreApplication.translate('EO-WMS',
        """
        <strong>EO-WMS Client plugin</strong><br />
        This plugin opens and controlls the WMS layers with 
        the time-dimension and implements some of the features 
        of the WMS-EO OGC best practice document.<br />
        Licence: EOxServer Open License (MIT style)<br />
        Copyright: &copy; 2014 EOX IT Service GmbH<br />
        Author: Martin Paces 
        (<a href=\"mailto:martin.paces@eox.at\">martin.paces@eox.at</a>) <br />
        Web: <a href=\"http://www.eox.at\">www.eox.at</a>
        """ )

        QMessageBox.information(self.iface.mainWindow(),"About EO-WMS",info)
        print "EOWMSPlugin.about()"


    def client(self): 
        """ Open the 'Client' GUI. """ 
        print "EOWMSPlugin.client()"


    def renderer(self,paniter):
        print "EOWMSPlugin.renderer()"
