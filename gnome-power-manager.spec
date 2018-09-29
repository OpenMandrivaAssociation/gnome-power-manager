%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME Power Manager
Name:		gnome-power-manager
Version:	3.30.0
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
BuildRequires:	meson

Requires:	gnome-mime-data
Requires:	adwaita-icon-theme
Requires:	upower

%description
GNOME Power Manager uses the information and facilities provided by Upower
displaying icons and handling user callbacks in an interactive GNOME session.
GNOME Power Preferences allows authorised users to set policy and
change preferences.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

#fix desktop file (missing ; as trailing char)
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/applications/*.desktop
    
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS
%{_bindir}/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.*
%{_mandir}/man1/*
