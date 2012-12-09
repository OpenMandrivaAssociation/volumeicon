Summary:	Lightweight volume control
Name:		volumeicon
Version:	0.4.3
Release:	3
Group:		Graphical desktop/Other
License:	GPLv3
URL:		http://http://code.google.com/p/mandriva-lxde/
Source0:         http://mandriva-lxde.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		volumeicon_lxde.patch
Patch1:		volumeicon-0.4.3-rosa-glib.patch
BuildRequires:	gtk2-devel intltool pkgconfig(libnotify)
BuildRequires:	pkgconfig(alsa)

%description
Volume Icon aims to be a lightweight volume control that sits in your systray.
Features

* Change volume by scrolling on the systray icon
* Ability to choose which channel to control
* Configurable stepsize (percentage of volume increase/decrease per scrollwheel
  step)
* Several icon themes (with gtk theme as default)
* Configurable external mixer
* Volume Slider

This is localized fork from Mandriva LXDE project

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
       
%make 

%install
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
Categories=AudioVideo;Audio;X-MandrivaLinux-Multimedia-Sound;
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%config(noreplace) %_sysconfdir/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Fri Dec 23 2011 Александр Казанцев <kazancas@mandriva.org> 0.4.3-3mdv2011.0
+ Revision: 744725
- enable hotkey by default
- fix url and version for fork by Mandriva LXDE projects

* Sat Aug 06 2011 Александр Казанцев <kazancas@mandriva.org> 0.4.3-1
+ Revision: 693411
- new version 0.4.3

* Tue Jul 19 2011 Александр Казанцев <kazancas@mandriva.org> 0.4.1-4
+ Revision: 690605
- change left mouse button action to view volume slider by default

* Sat Jun 25 2011 Александр Казанцев <kazancas@mandriva.org> 0.4.1-3
+ Revision: 687151
- add localized version. You may now translate it.
- fix backports buildrequires issue

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.4.1-1
+ Revision: 684445
- new version 0.4.1
- import volumeicon


* Tue Apr 06 2010 slick50 <lxgator@gmail.com> 0.2.1-1pclos2010
- initial pkg

