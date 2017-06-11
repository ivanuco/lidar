; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "loadLiDAR"
#define MyAppVersion "0.1"
#define MyAppPublisher "Iv�n del Viejo Garc�a"
#define MyAppURL "https://github.com/ivanuco/lidar"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{2012448A-5089-4045-978A-DA917E52FCB2}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=C:\lidar\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=C:\LiClipse Workspace\lidar\LICENSE
InfoBeforeFile=C:\LiClipse Workspace\lidar\README.md
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes
ChangesEnvironment=true

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Files]
Source: "C:\LiClipse Workspace\lidar\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

[Tasks]
Name: modifypath; Description: Add application directory to your environmental path; Flags: unchecked

[Code]
const 
 ModPathName = 'modifypath'; 
 ModPathType = 'user'; 

function ModPathDir(): TArrayOfString; 
begin 
 setArrayLength(Result, 1) 
 Result[0] := ExpandConstant('{app}'); 
end; 
#include "modpath.iss"
