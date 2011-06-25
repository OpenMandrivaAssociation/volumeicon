%define	name	volumeicon
%define	version	0.4.1
%define	release	%mkrel	2

Summary:	Lightweight volume control
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphical desktop/Other
License:	GPLv3
URL:		http://www.softwarebakery.com/maato/home.html
Source:         http://www.softwarebakery.com/maato/home.html/%{name}-%{version}.tar.gz
Patch0:		volumeicon_lxde.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk2-devel
%if %mdvver >= 201100 
Buildrequires: 	%{_lib}alsa-devel
%else
Buildrequires:	%{_lib}alsa2-devel
%endif

Obsoletes: %name < %version

%description
Volume Icon aims to be a lightweight volume control that sits in your systray.
Features

* Change volume by scrolling on the systray icon
* Ability to choose which channel to control
* Configurable stepsize (percentage of volume increase/decrease per scrollwheel step)
* Several icon themes (with gtk theme as default)
* Configurable external mixer
* Volume Slider

%prep
%setup -q 
%patch0 -p0

%build
%configure2_5x 
       
%make 

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%_sysconfdir/xdg/autostart/
cat > %{buildroot}%_sysconfdir/xdg/autostart/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=volumeicon
Comment=Volume Icon
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/gui/appicon.svg
Categories=AudioVideo;Audio;X-MandrivaLinux-Multimedia-Sound
EOF

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%_sysconfdir/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}


