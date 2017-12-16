'''
	Script by Rocky5
	Used to create MyPrograms.xml for different emulators styles
'''

import fileinput, os, time, xbmc, xbmcgui

#####	Start markings for the log file.
print "| _Scripts\XBMC-Emustation\menu_loader.py loaded."
	
pDialog							= xbmcgui.DialogProgress()
dialog							= xbmcgui.Dialog()
XBE_Files						= "0"
Default_Layout_XML_Path			= "0"
Layout_XML_Path					= "0"

MenuLabel = xbmc.getInfoLabel('Container(9000).ListItem.Label2')
if str(xbmcgui.getCurrentWindowId()) == "11111": MenuLabel = xbmc.getInfoLabel('Control.GetLabel(99)')
if MenuLabel == "dummy label for python script":	MenuLabel = "apps"
MyPrograms_Path					= xbmc.translatePath( 'special://skin/720p/MyPrograms.xml' )
ThemeType						= xbmc.getInfoLabel( 'Skin.CurrentTheme' )
Rom_List_Path					= xbmc.translatePath( "Special://xbmc/_scripts/XBMC-Emustation/rom lists/" )


Default_No_Layout				= xbmc.translatePath( 'special://xbmc/_layouts/default/skindefault/layout.xml' )
Default_No_Synopsis_Layout		= xbmc.translatePath( 'special://xbmc/_layouts/default/skindefault/synopsis_layout.xml' )
Default_No_Thumb_Layout			= xbmc.translatePath( 'special://xbmc/_layouts/default/skindefault/thumb_layout.xml' )
XBE_Default_No_Layout			= xbmc.translatePath( 'special://xbmc/_layouts/default/skindefault/XBE files/layout.xml' )
XBE_Default_No_Synopsis_Layout	= xbmc.translatePath( 'special://xbmc/_layouts/default/skindefault/XBE files/synopsis_layout.xml' )
XBE_Default_No_Thumb_Layout		= xbmc.translatePath( 'special://xbmc/_layouts/default/skindefault/XBE files/thumb_layout.xml' )


Default_Layout					= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/layout.xml' )
Default_Synopsis_Layout			= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/synopsis_layout.xml' )
Default_Thumb_Layout			= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/thumb_layout.xml' )
XBE_Default_Layout				= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/XBE files/layout.xml' )
XBE_Default_Synopsis_Layout		= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/XBE files/synopsis_layout.xml' )
XBE_Default_Thumb_Layout		= xbmc.translatePath( 'special://xbmc/_layouts/default/' + ThemeType + '/XBE files/thumb_layout.xml' )
Custom_Layout					= xbmc.translatePath( 'special://xbmc/_layouts/' + MenuLabel + '/' + ThemeType + '/layout.xml' )
Custom_Synopsis_Layout			= xbmc.translatePath( 'special://xbmc/_layouts/' + MenuLabel + '/' + ThemeType + '/synopsis_layout.xml' )
Custom_Thumb_Layout				= xbmc.translatePath( 'special://xbmc/_layouts/' + MenuLabel + '/' + ThemeType + '/thumb_layout.xml' )

if MenuLabel == "apps" or MenuLabel == "xbox" or MenuLabel == "homebrew" or MenuLabel == "ports": XBE_Files = "1"

xbmc.executebuiltin('Skin.SetString(emuname,' + MenuLabel + ')')
	
Header_Data_EMU					= '<window id="1">\n\
		<onunload condition="Player.HasVideo">Stop</onunload>\n\
		<defaultcontrol always="true">9000</defaultcontrol>\n\
		<allowoverlay>no</allowoverlay>\n\
		<view>50</view>\n\
		<layout>%s</layout>\n\
		<controls>\n\
		<include>CommonBackground</include>\n\
		<control type="group">\n\
		<animation effect="fade" time="150">WindowOpen</animation>\n\
		<animation effect="fade" time="150">WindowClose</animation>\n\
		<control type="image">\n\
			<posx>0</posx>\n\
			<posy>0</posy>\n\
			<width>1280</width>\n\
			<height>720</height>\n\
			<aspectratio>stretch</aspectratio>\n\
			<texture background="false" fallback="layouts/%s/menu_background.png">Special://xbmc/_layouts/%s/%s/menu_background.png</texture>\n\
		</control>\n\
		<!-- Used to run the script and stop folk moving the list forward or backwards -->\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
			<onfocus>RunScript(Special://XBMC/_scripts/XBMC-Emustation/play_preview.py)</onfocus>\n\
		</control>\n\
		<!-- Used to stop playback if one of the direction buttons are pressed or the (A) button -->\n\
		<control type="button" id="9100">\n\
			<posx>-500</posx>\n\
			<onup>setfocus(9000)</onup>\n\
			<onup>stop</onup>\n\
			<onup>Control.Move(9000,-1)</onup>\n\
			<ondown>setfocus(9000)</ondown>\n\
			<ondown>stop</ondown>\n\
			<ondown>Control.Move(9000,1)</ondown>\n\
			<onclick>setfocus(9000)</onclick>\n\
			<onclick>stop</onclick>\n\
		</control>\n\
	'
Footer_Data_EMU					= '\n\
	</control>\n\
	<control type="group" id="jump section">\n\
		<visible allowhiddenfocus="true">!Control.HasFocus(9999) + !Control.HasFocus(9000) + !Control.HasFocus(9100)</visible>\n\
		<posy>90</posy>\n\
		<control type="image">\n\
			<description>background image</description>\n\
			<posx>320</posx>\n\
			<posy>108</posy>\n\
			<width>640</width>\n\
			<height>250</height>\n\
			<texture border="20,20,20,20">menu_back.png</texture>\n\
		</control>\n\
		<control type="label">\n\
			<description>heading label</description>\n\
			<posx>320</posx>\n\
			<posy>130</posy>\n\
			<width>640</width>\n\
			<height>50</height>\n\
			<align>center</align>\n\
			<aligny>center</aligny>\n\
			<font>size_50</font>\n\
			<label>$LOCALIZE[33063]</label>\n\
			<textcolor>menu_header_label</textcolor>\n\
		</control>\n\
		<control type="grouplist" id="9998">\n\
			<posx>320</posx>\n\
			<posy>201</posy>\n\
			<width>640</width>\n\
			<height>50</height>\n\
			<onleft>9998</onleft>\n\
			<onright>9998</onright>\n\
			<onup>-</onup>\n\
			<ondown>-</ondown>\n\
			<itemgap>-1</itemgap>\n\
			<scrolltime>0</scrolltime>\n\
			<orientation>horizontal</orientation>\n\
	<!-- jumpcode -->\n\
	</control>\n\
	</control>\n\
	</controls>\n\
	</window>'

Header_Data_XBE					= '<window id="1">\n\
		<onunload condition="Player.HasVideo">Stop</onunload>\n\
		<defaultcontrol always="true">50</defaultcontrol>\n\
		<allowoverlay>no</allowoverlay>\n\
		<view>50</view>\n\
		<layout>%s</layout>\n\
		<controls>\n\
		<include>CommonBackground</include>\n\
		<control type="group">\n\
		<animation effect="fade" time="150">WindowOpen</animation>\n\
		<animation effect="fade" time="150">WindowClose</animation>\n\
		<control type="image">\n\
			<posx>0</posx>\n\
			<posy>0</posy>\n\
			<width>1280</width>\n\
			<height>720</height>\n\
			<aspectratio>stretch</aspectratio>\n\
			<texture background="false" fallback="layouts/%s/menu_background.png">Special://xbmc/_layouts/%s/%s/menu_background.png</texture>\n\
		</control>\n\
		<!-- Used to run the script and stop folk moving the list forward or backwards -->\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
			<onfocus>RunScript(Special://XBMC/_scripts/XBMC-Emustation/play_preview.py)</onfocus>\n\
		</control>\n\
		<!-- Used to stop playback if one of the direction buttons are pressed or the (A) button -->\n\
		<control type="button" id="9100">\n\
			<posx>-500</posx>\n\
			<onup>setfocus(50)</onup>\n\
			<onup>stop</onup>\n\
			<onup>Control.Move(50,-1)</onup>\n\
			<ondown>setfocus(50)</ondown>\n\
			<ondown>stop</ondown>\n\
			<ondown>Control.Move(50,1)</ondown>\n\
			<onclick>setfocus(50)</onclick>\n\
			<onclick>stop</onclick>\n\
		</control>\n\
	'
Footer_Data_XBE					= '\n\
	</control>\n\
	</controls>\n\
	</window>'

if XBE_Files == "0":

	if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
		if os.path.isfile( Custom_Synopsis_Layout ):
			Layout_XML_Path				= Custom_Synopsis_Layout
		else:
			if os.path.isfile( Default_Synopsis_Layout ):
				Layout_XML_Path			= Default_Synopsis_Layout
			else:
				Layout_XML_Path			= Default_No_Synopsis_Layout
	elif xbmc.getCondVisibility( 'Skin.HasSetting(thumblayout)' ):
		if os.path.isfile( Custom_Thumb_Layout ):
			Layout_XML_Path				= Custom_Thumb_Layout
		else:
			if os.path.isfile( Default_Thumb_Layout ):
				Layout_XML_Path			= Default_Thumb_Layout
			else:
				Layout_XML_Path			= Default_No_Thumb_Layout
	else:
		if os.path.isfile( Custom_Layout ):
			Layout_XML_Path				= Custom_Layout
		elif os.path.isfile( Default_Layout ):
			Default_Layout_XML_Path		= Default_Layout
		else:
			Default_Layout_XML_Path		= Default_No_Layout
			

	if os.path.isfile( os.path.join( Rom_List_Path,MenuLabel + '.xml' ) ):
		## this is here so not to mess with the actual menulabel
		if not os.path.isfile( Layout_XML_Path ):
			MenuLabel_XML = "default"
		else:
			MenuLabel_XML = MenuLabel

		Header_Data = Header_Data_EMU % ( MenuLabel_XML, MenuLabel_XML, MenuLabel_XML, ThemeType  )
			
		if os.path.isfile( Layout_XML_Path ):
			try:
				with open( Layout_XML_Path ) as layoutfile:
					with open(MyPrograms_Path, "w") as inputfile:
						inputfile.write( Header_Data )
						for code in layoutfile:
							inputfile.write( code )
						inputfile.write( Footer_Data_EMU )
						inputfile.close()

				with open( Rom_List_Path + MenuLabel + '.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
						if '</focusedlayout>' in line:
							line = line.replace(line,line+countfile)
						print line,
				with open( Rom_List_Path + MenuLabel + '_jump.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
						if '<!-- jumpcode -->' in line:
							line = line.replace(line,line+countfile)
						print line,
					countfile.close()
			except:
				pass

			xbmc.executebuiltin( 'ActivateWindow(Programs,Static_Menu,return)' )

		elif os.path.isfile( Default_Layout_XML_Path ):
			try:
				with open( Default_Layout_XML_Path ) as layoutfile:
					with open(MyPrograms_Path, "w") as inputfile:
						inputfile.write( Header_Data )
						for code in layoutfile:
							inputfile.write( code )
						inputfile.write( Footer_Data_EMU )	
						inputfile.close()

				with open( Rom_List_Path + MenuLabel + '.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
						if '</focusedlayout>' in line:
							line = line.replace(line,line+countfile)
						print line,
				with open( Rom_List_Path + MenuLabel + '_jump.xml' ) as countfile:
					countfile = countfile.read()
					for line in fileinput.FileInput(MyPrograms_Path,inplace=1):
						if '<!-- jumpcode -->' in line:
							line = line.replace(line,line+countfile)
						print line,
					countfile.close()
			except:
				pass
			xbmc.executebuiltin( 'ActivateWindow(Programs,Static_Menu,return)' )

		else:	# default layout is missing so error!
			xbmc.executebuiltin('SetFocus(9000)')
			dialog.ok( "ERROR","Default layout file is missing.",Default_Layout_XML_Path )

	else:	# default layout is missing so error!
		xbmc.executebuiltin('SetFocus(9000)')
		dialog.ok("ERROR","No rom list found","Rescan this emulator for roms to fix.",os.path.join( Rom_List_Path,MenuLabel + '.xml' ))
else:		
	pass

if XBE_Files == "1":
	
	if xbmc.getCondVisibility( 'Skin.HasSetting(synopsislayout)' ):
		if os.path.isfile( Custom_Synopsis_Layout ):
			Layout_XML_Path				= Custom_Synopsis_Layout
		else:
			if os.path.isfile( XBE_Default_Synopsis_Layout ):
				Default_Layout_XML_Path	= XBE_Default_Synopsis_Layout
			else:
				Default_Layout_XML_Path	= XBE_Default_No_Synopsis_Layout
	elif xbmc.getCondVisibility( 'Skin.HasSetting(thumblayout)' ):
		if os.path.isfile( Custom_Thumb_Layout ):
			Layout_XML_Path				= Custom_Thumb_Layout
		else:
			if os.path.isfile( XBE_Default_Thumb_Layout ):
				Default_Layout_XML_Path	= XBE_Default_Thumb_Layout
			else:
				Default_Layout_XML_Path	= XBE_Default_No_Thumb_Layout
	else:
		if os.path.isfile( Custom_Layout ):
			Layout_XML_Path				= Custom_Layout
		elif os.path.isfile( XBE_Default_Layout ):
			Default_Layout_XML_Path		= XBE_Default_Layout
		else:
			Default_Layout_XML_Path		= XBE_Default_No_Layout
		
		
		
	## this is here so not to mess with the actual menulabel
	if not os.path.isfile( Layout_XML_Path ):
		MenuLabel_XML = "default"
	else:
		MenuLabel_XML = MenuLabel
	
	Header_Data = Header_Data_XBE % ( MenuLabel_XML, MenuLabel_XML, MenuLabel_XML, ThemeType  )
	
	if os.path.isfile( Layout_XML_Path ):
		with open( Layout_XML_Path	) as layoutfile:
			with open(MyPrograms_Path, "w") as inputfile:
				inputfile.write( Header_Data )		
				for code in layoutfile:
					inputfile.write( code )			
				inputfile.write( Footer_Data_XBE )
				xbmc.executebuiltin( 'ActivateWindow(Programs,'+ MenuLabel +',return)' )
				
	elif os.path.isfile( Default_Layout_XML_Path ):
		with open( Default_Layout_XML_Path ) as layoutfile:
			with open(MyPrograms_Path, "w") as inputfile:
				inputfile.write( Header_Data )		
				for code in layoutfile:
					inputfile.write( code )			
				inputfile.write( Footer_Data_XBE )
				xbmc.executebuiltin( 'ActivateWindow(Programs,'+ MenuLabel +',return)' )
				
	else:	# default layout is missing so error!
		xbmc.executebuiltin('SetFocus(9000)')
		dialog.ok( "ERROR","Default layout file is missing.",Default_Layout_XML_Path )
else:
	xbmc.executebuiltin('SetFocus(9000)')