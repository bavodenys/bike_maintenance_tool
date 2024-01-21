; Define variables
!define APP_NAME "Bike_maintenance_tool"
!define APP_EXECUTABLE_NAME "bike_maintenance_tool.exe"

Outfile "${APP_NAME}_Windows_Installer.exe"
InstallDir $PROGRAMFILES\${APP_NAME}

Page components
Page directory
Page instfiles

Section
  SetOutPath $INSTDIR
  File "dist\${APP_EXECUTABLE_NAME}"
SectionEnd

Section "Start Menu Shortcuts"
  CreateDirectory "$SMPROGRAMS\${APP_NAME}"
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\Uninstall.lnk" "$INSTDIR\uninstall.exe"
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk" "$INSTDIR\${APP_EXECUTABLE_NAME}"
SectionEnd

Section "Uninstall"
  Delete "$SMPROGRAMS\${APP_NAME}\Uninstall.lnk"
  Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk"
  RMDir "$SMPROGRAMS\${APP_NAME}"
  Delete "$INSTDIR\${APP_EXECUTABLE_NAME}"
SectionEnd

