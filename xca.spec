Summary:	GUI for handling X509 certificates, RSA keys and PKCS#10 requests
Name:		xca
Version:	2.6.0
Release:	1
License:	BSD
Group:		System/Servers
URL:		https://www.hohnstaedt.de/xca/xca.html
Source0:	https://github.com/chris2511/xca/releases/download/RELEASE.%{version}/xca-%{version}.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png

BuildRequires:	cmake
BuildRequires:  qmake5
BuildRequires:  qt5-assistant
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	qt5-qttools
BuildRequires:	db-devel
BuildRequires:	pkgconfig(openssl) >= 1.1
BuildRequires:	linuxdoc-tools
BuildRequires:	libltdl-devel

%description
XCA uses a Berkeley DB for storage and supports RSA keys,
certificate signing requests (PKCS#10) and Certificates (X509v3)
The signing of requests, and the creation of selfsigned certificates
is supported. Both can use templates for simplicity.
The PKI structures can be imported and exported in several formats
like PKCS#7, PKCS#12, PEM, DER, PKCS#8.

%prep
%setup -q
%autopatch -p1

perl -n -i -e '$/="\r\n";chomp;print;print "\n"' COPYRIGHT

%build
%cmake
%make_build

%install
export TOPDIR=%{buildroot}
export destdir=%{buildroot}
%make_install -C build

rm -f %{buildroot}%{_datadir}/pixmaps/xca.xpm

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m644 %{SOURCE11} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%files
%doc AUTHORS COPYRIGHT
%doc doc/*.html
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%{_datadir}/mime/packages/xca.xml


%changelog
* Tue Nov 08 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.9.1-1mdv2011.0
+ Revision: 729068
- 0.9.1
  P3 dropped
- trying to keep sync with mageia, more easy for me

* Wed Mar 16 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.9.0-1
+ Revision: 645675
- 0.9.0
  P0 reddiffed
  P1 & P2 dropped
  P3 fix GCC issues

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2mdv2011.0
+ Revision: 615493
- the mass rebuild of 2010.1 packages

* Sat Apr 24 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.8.1-1mdv2010.1
+ Revision: 538405
- 0.8.1

  + Funda Wang <fwang@mandriva.org>
    - rebuild

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 484988
- Fix BuildRequires
- update to new version 0.8.0

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 443217
- Update to new version 0.7.0
- Add 2 Fedora build patches

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.6.4-4mdv2009.0
+ Revision: 262272
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.6.4-3mdv2009.0
+ Revision: 256633
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 28 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.4-1mdv2008.1
+ Revision: 138707
- restore parallel build, the failure anssi saw was not parallel build related
- buildrequires qt4-linguist
- add lib64.patch to fix x86-64 build
- rebuild for new era
- fd.o icons
- XDG menu
- disable parallel build, Anssi saw it break once
- need to build with -fpermissive due to a casting issue
- need to explictly add -I%%{qt4include}/Qt to the build flags because of this thing's wacky broken build scripts
- need to specify QTDIR
- slightly improve description
- update buildrequires
- drop both patches (merged or superseded upstream)
- new release 0.6.4
- spec clean

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Apr 15 2006 Luca Berra <bluca@vodka.it> 0.5.1-4mdk
- rebuild for new openssl
- fixes for new gcc complaining on casts
- mkrel

* Fri May 06 2005 Luca Berra <bluca@vodka.it> 0.5.1-3mdk 
- fix build on biarches

* Wed Mar 30 2005 Luca Berra <bluca@vodka.it> 0.5.1-2mdk 
- rebuild

* Sun Aug 01 2004 Luca Berra <bluca@mandrakesoft.com> 0.5.1-1mdk
- New release 0.5.1

* Fri Jun 04 2004 Luca Berra <bluca@vodka.it> 0.5.0-1mdk 
- 0.5.0
- drop gcc patch, add qfont patch

* Thu Feb 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.4.6-2mdk
- cleanups!
- fix summary/longtitle
- don't bzip2 icons
- fix invalid-menu-section

* Fri Jan 02 2004 Luca Berra <bluca@vodka.it> 0.4.6-1mdk
- initial cooker contrib

