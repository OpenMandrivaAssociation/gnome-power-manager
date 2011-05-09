%define	name	gnome-power-manager
%define version	2.32.0
%define	release	%mkrel 3

Name:		%name
Version:	%version
Release:	%release
Summary:	GNOME Power Manager
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/projects/gnome-power-manager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-power-manager/%{name}-%{version}.tar.bz2
# (pt) Use gnome-session-save to get the shutdown dialog, else we get the logout one
# We should use dbus directly but the dialog needs to ask us canHibernate and canSuspend
Patch2:		gnome-power-manager-shutdown.patch
Patch3:		gnome-power-manager-2.27.1-dont-run-in-xfce.patch
Patch4:		gnome-power-manager-2.32.0-bug644143.patch
Patch5:		gnome-power-manager-2.32.0-libnotify0.7.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	glib2-devel >= 2.25
BuildRequires:	gtk+2-devel
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libgnome-window-settings-devel
BuildRequires:	libbonobo-activation-devel
BuildRequires:	libwnck-devel
BuildRequires:	libGConf2-devel GConf2
BuildRequires:	autoconf
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	libnotify-devel
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	xmlto
BuildRequires:	libxslt-proc
BuildRequires:  libtool
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	libpanel-applet-devel
BuildRequires:  intltool
BuildRequires:  UPower-devel
BuildRequires:	unique-devel >= 0.9.4
Requires:	gnome-mime-data
Requires:	gnome-icon-theme
Requires(preun):  GConf2
Requires:	upower

%description
GNOME Power Manager uses the information and facilities provided by Upower
displaying icons and handling user callbacks in an interactive GNOME session. 
GNOME Power Preferences allows authorised users to set policy and 
change preferences.

%prep
%setup -q
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure2_5x --disable-schemas-install --disable-scrollkeeper \
	--with-doc-dir=%{_datadir}/doc \
	--with-dbus-services=%{_datadir}/dbus-1/services
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

desktop-file-install --vendor="" \
	--add-category="DesktopSettings" \
	--add-category="GTK" \
	--add-category="GNOME" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/gnome-power-preferences.desktop

%find_lang %name
 
%clean
rm -rf %{buildroot}

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README 
%{_sysconfdir}/xdg/autostart/gnome-power-manager.desktop
%{_bindir}/*
%_sbindir/gnome-power-backlight-helper
%_datadir/polkit-1/actions/org.gnome.power.policy
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/*
%{_datadir}/gnome-power-manager
%{_datadir}/gnome/help/gnome-power-manager
%{_datadir}/omf/gnome-power-manager
%{_mandir}/man1/*
%{_datadir}/icons/hicolor/*/apps/gnome-*
%{_datadir}/gnome-2.0/ui/*.xml
%{_libdir}/bonobo/servers/*.server
%_libexecdir/gnome-brightness-applet
%_libexecdir/gnome-inhibit-applet
%{_sysconfdir}/gconf/schemas/*.schemas
