%define	name	gnome-power-manager
%define version	2.27.1
%define	release	%mkrel 1

Name:		%name
Version:	%version
Release:	%release
Summary:	GNOME Power Manager
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/projects/gnome-power-manager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-power-manager/%{name}-%{version}.tar.bz2
# (fc) 2.23.91-2mdv lock screensaver when running suspend / hibernate (needed since we don't auto-lock screensaver by default)
Patch0:		gnome-power-manager-2.23.91-lock.patch
# (pt) Claim org.freedesktop.Policy.Power so that other scripts and apps know that some power management tool is running
Patch1:		gnome-power-manager-powerpolicy.patch
# (pt) Use gnome-session-save to get the shutdown dialog, else we get the logout one
# We should use dbus directly but the dialog needs to ask us canHibernate and canSuspend
Patch2:		gnome-power-manager-shutdown.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	gtk2-devel >= 2.6.0
BuildRequires:	libgnomeui2-devel >= 2.10.0
BuildRequires:	libglade2.0-devel >= 2.5.0
BuildRequires:	libwnck-devel >= 2.10.0
BuildRequires:	hal-devel >= 0.5.6
BuildRequires:	dbus-devel >= 0.50
BuildRequires:	libcanberra-devel
BuildRequires:	autoconf2.5
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
BuildRequires:	libgstreamer-devel
BuildRequires:  intltool
BuildRequires:  policykit-gnome-devel
BuildRequires:  libdevkit-gobject-devel
BuildRequires:  devicekit-power-devel
BuildRequires:	unique-devel >= 0.9.4
Requires:	gnome-mime-data
Requires:	gnome-icon-theme
Requires:	hal >= 0.5.6
Requires(pre):	GConf2
Requires(post):	GConf2
Requires(post): scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper
Requires:	policykit-gnome
Requires:	devicekit-power

%description
GNOME Power Manager uses the information and facilities provided by HAL 
displaying icons and handling user callbacks in an interactive GNOME session. 
GNOME Power Preferences allows authorised users to set policy and 
change preferences.

%prep
%setup -q
%patch0 -p1 -b .lock
%patch1 -p1 -b .powerpolicy
#%patch2 -p0 -b .logout

%build
%configure2_5x --enable-legacy-buttons \
	--enable-policykit \
	--with-doc-dir=%{buildroot}%{_datadir}/doc \
	--with-dbus-services=%{buildroot}%{_datadir}/dbus-1/services
make

%install
rm -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall _ENABLE_SK=false

rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

desktop-file-install --vendor="" \
	--add-category="DesktopSettings" \
	--add-category="GTK" \
	--add-category="GNOME" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/gnome-power-preferences.desktop

%find_lang %name
 
mv %{buildroot}%{_docdir}/*/spec/dbus-interface.html .

%clean
rm -rf %{buildroot}

%define schemas %name

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README dbus-interface.html
%{_sysconfdir}/xdg/autostart/gnome-power-manager.desktop
%{_bindir}/*
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

