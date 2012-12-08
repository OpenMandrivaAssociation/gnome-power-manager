Name:		gnome-power-manager
Version:	3.6.0
Release:	1
Summary:	GNOME Power Manager
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/projects/gnome-power-manager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-power-manager/3.6/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	intltool
BuildRequires:	xmlto
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	pkgconfig(libnotify)
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

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}
 
%files -f %{name}.lang
%doc AUTHORS COPYING INSTALL NEWS README 
%{_datadir}/applications/gnome-power-statistics.desktop
%{_bindir}/*
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_datadir}/gnome-power-manager
%{_datadir}/icons/hicolor/*/apps/gnome-*
%{_mandir}/man1/*



%changelog
* Fri Oct  5 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Tue May 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.0-1
+ Revision: 798927
- version update 3.4.0

* Thu Mar 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 783221
- new version 3.2.1
- cleaned up spec

* Tue Jan 31 2012 Alexander Barakin <abarakin@mandriva.org> 2.32.0-4
+ Revision: 770000
- corrected buildreq
- bug #64657 gnome-power-manager shows phantom battery after resume
  patch from: https://bugs.launchpad.net/ubuntu/+source/gnome-power-manager/+bug/675108

* Mon May 09 2011 Götz Waschk <waschk@mandriva.org> 2.32.0-3
+ Revision: 673065
- depend on upower

* Mon Apr 11 2011 Funda Wang <fwang@mandriva.org> 2.32.0-2
+ Revision: 652533
- add back libwnck br
- add upstream patch to fix gnome bug#644143
- add upstream patch to build with libnotify 0.7

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581671
- new version

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 579013
- update to new version 2.31.92

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574899
- update to new version 2.31.91

* Wed Aug 18 2010 Götz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 571158
- update to new version 2.31.90

* Fri Aug 06 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 566923
- new version
- drop patch
- update deps

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 538924
- update to new version 2.30.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528779
- update to new version 2.30.0

  + Funda Wang <fwang@mandriva.org>
    - update BR's name

* Mon Mar 01 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 512965
- update to new version 2.29.91

* Mon Feb 01 2010 Götz Waschk <waschk@mandriva.org> 2.29.2-1mdv2010.1
+ Revision: 499216
- update to new version 2.29.2

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 475486
- update to new version 2.29.1

* Mon Dec 07 2009 Götz Waschk <waschk@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 474501
- update to new version 2.28.2

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458727
- Release 2.28.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446549
- update to new version 2.28.0

* Fri Sep 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437908
- new version

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420293
- update to new version 2.27.91

* Mon Aug 03 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 408262
- new version
- drop merged patches 1,4
- update build deps

* Tue Jul 21 2009 Colin Guthrie <cguthrie@mandriva.org> 2.27.2-3mdv2010.0
+ Revision: 398349
- Fix segv on 64 bit full charge (mdv#52298, gnome#588259)

* Tue Jul 07 2009 Frederik Himpe <fhimpe@mandriva.org> 2.27.2-2mdv2010.0
+ Revision: 393075
- Rebuild for devicekit-power 009

* Mon Jul 06 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 392899
- update to new version 2.27.2

* Tue Jun 23 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-2mdv2010.0
+ Revision: 388457
- don't run in xfce (bug #48710)

* Wed Jun 03 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 382440
- new version
- update deps

* Mon Jun 01 2009 Götz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 381859
- update to new version 2.26.2

* Wed Apr 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.26.1-1mdv2009.1
+ Revision: 368649
- Release 2.26.1
- Regenerate patch1

* Wed Apr 15 2009 Frederic Crozat <fcrozat@mandriva.com> 2.26.0-2mdv2009.1
+ Revision: 367343
- enable legacy buttons, fix Mdv bug #48741
- enable policykit support explicitly

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355711
- update to new version 2.26.0

* Mon Mar 09 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-3mdv2009.1
+ Revision: 353140
- new version
- drop patch 3

* Thu Mar 05 2009 Frederic Crozat <fcrozat@mandriva.com> 2.25.91-3mdv2009.1
+ Revision: 349072
- Patch3 (SVN): don't register in session manager

* Thu Feb 26 2009 Frederic Crozat <fcrozat@mandriva.com> 2.25.91-2mdv2009.1
+ Revision: 345254
- Rebuild with latest x11-proto

* Wed Feb 11 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 339486
- new version
- drop patch 3
- update file list

* Thu Feb 05 2009 Pascal Terjan <pterjan@mandriva.org> 2.25.3-2mdv2009.1
+ Revision: 337822
- Add fedora patch for #47556

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 336482
- BR unique

  + Götz Waschk <waschk@mandriva.org>
    - new version
    - update build deps

* Thu Jan 29 2009 Pascal Terjan <pterjan@mandriva.org> 2.25.2-3mdv2009.1
+ Revision: 335045
- Require devicekit-power

* Wed Jan 07 2009 Götz Waschk <waschk@mandriva.org> 2.25.2-2mdv2009.1
+ Revision: 326586
- update to new version 2.25.2

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 315958
- update build deps
- new version
- update patch 1
- disable patch 2

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Nov 17 2008 Götz Waschk <waschk@mandriva.org> 2.24.2-1mdv2009.1
+ Revision: 303958
- new version
- drop patch 3

* Mon Oct 27 2008 Pascal Terjan <pterjan@mandriva.org> 2.24.1-2mdv2009.1
+ Revision: 297703
- Backport upstream patch to avoid duplicate events from X+Hal
- Allow setting and alternate logout command in gconf

* Wed Oct 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 296486
- update to new version 2.24.1

* Tue Sep 30 2008 Pascal Terjan <pterjan@mandriva.org> 2.24.0-3mdv2009.0
+ Revision: 290244
- Prompt the Shutdown dialog and not the Logout one when pressing power button

* Fri Sep 26 2008 Pascal Terjan <pterjan@mandriva.org> 2.24.0-2mdv2009.0
+ Revision: 288601
- Restore gnome-power-manager-powerpolicy.patch (else shutdown will occur immediatly when pressing the button)

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287267
- new version

* Tue Sep 16 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.91-2mdv2009.0
+ Revision: 285148
- Patch0: lock screensaver when doing suspend / hibernate (needed since we don't autolock screensaver by default)

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278391
- new version

* Wed Aug 06 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 264261
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.3-1mdv2009.0
+ Revision: 231413
- enable policykit
- fix buildrequires
- new version
- update license
- drop patch

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.22.1-1mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Mar 29 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2008.1
+ Revision: 191139
- new version
- drop patch 2

* Thu Mar 27 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.0-2mdv2008.1
+ Revision: 190629
- Fix buildrequires
- Remove patch2 (no longer needed)
- Patch2 (SVN): lot of bug fixes from upstream

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183914
- new version

* Fri Feb 15 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 168766
- new version
- update file list

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 128682
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Pascal Terjan <pterjan@mandriva.org> 2.20.2-1mdv2008.1
+ Revision: 120585
- update to new version 2.20.2
- update to new version 2.20.2

  + Thierry Vignaud <tv@mandriva.org>
    - do not package big ChangeLog

* Tue Dec 11 2007 Colin Guthrie <cguthrie@mandriva.org> 2.20.1-3mdv2008.1
+ Revision: 117178
- Disable PolicyKit support for now as it's based on an old implementation.

* Fri Dec 07 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.1-2mdv2008.1
+ Revision: 116339
- Fix buildrequires
- Enable PolicyKit support for cooker

* Wed Nov 14 2007 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 108695
- new version

* Wed Oct 17 2007 Pascal Terjan <pterjan@mandriva.org> 2.20.0-2mdv2008.1
+ Revision: 99585
- Add P3 by David Zeuthen to get the errors (Upstream #486138)

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89332
- new version

* Mon Sep 10 2007 Pascal Terjan <pterjan@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 83982
- 2.19.92
- Drop P5 (fixed in popt)

* Fri Sep 07 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.6-2mdv2008.0
+ Revision: 81780
- Fix menu entry to only appear in GNOME preference menu

  + Thierry Vignaud <tv@mandriva.org>
    - replace %%{_datadir}/man by %%{_mandir}!

* Thu Aug 02 2007 Pascal Terjan <pterjan@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 58159
- update to new version 2.19.6
- Update P0 for 2.19.6
- Have a complete Source URL to allow mdvsys update to work

* Wed Jul 04 2007 Pascal Terjan <pterjan@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 48179
- Drop Patch4, g-p-m no longer uses gst-launch
- 2.19.5
  drop Patch6

* Thu Jun 28 2007 Pascal Terjan <pterjan@mandriva.org> 2.19.3-2mdv2008.0
+ Revision: 45570
- Add upstream patch that should fix #444240

* Fri Jun 15 2007 Pascal Terjan <pterjan@mandriva.org> 2.19.3-1mdv2008.0
+ Revision: 39811
- BuildRequires libgstreamer-devel as we now use it
- Fix build with new popt
- package new doc dbus-interface.html
- 2.19.3

  + Michael Scherer <misc@mandriva.org>
    - /usr/share/dbus/services is already owned by dbus

* Wed May 23 2007 Pascal Terjan <pterjan@mandriva.org> 2.19.2-1mdv2008.0
+ Revision: 29945
- 2.19.2

* Thu May 03 2007 Pascal Terjan <pterjan@mandriva.org> 2.19.1-1mdv2008.0
+ Revision: 22078
- dbus config file is no longer shipped
- Drop P1, merged upstream
- 2.19.1

* Tue Apr 17 2007 Pascal Terjan <pterjan@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 14022
- 2.18.2
- Drop patch3

