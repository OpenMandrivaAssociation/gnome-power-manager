%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME Power Manager
Name:		gnome-power-manager
Version:	3.14.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/projects/gnome-power-manager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-power-manager/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	intltool
BuildRequires:	xmlto
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(upower-glib)
Requires:	gnome-mime-data
Requires:	gnome-icon-theme
Requires:	upower

%description
GNOME Power Manager uses the information and facilities provided by Upower
displaying icons and handling user callbacks in an interactive GNOME session. 
GNOME Power Preferences allows authorised users to set policy and 
change preferences.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std
%find_lang %{name}
 
%files -f %{name}.lang
%doc AUTHORS COPYING INSTALL NEWS README 
%{_bindir}/*
%{_datadir}/appdata/gnome-power-statistics.appdata.xml
%{_datadir}/applications/gnome-power-statistics.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_iconsdir}/hicolor/*/apps/gnome-*
%{_iconsdir}/HighContrast/*/apps/gnome-*
%{_mandir}/man1/*

