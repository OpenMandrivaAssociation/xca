Summary:	GUI for handling X509 certificates, RSA keys and PKCS#10 requests
Name:		xca
Version:	0.8.0
Release:	%mkrel 1
License:	BSD
Group:		System/Servers
Source0:	http://prdownloads.sourceforge.net/xca/%{name}-%{version}.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		xca-0.6.4-lib64.patch
# Fedora patches
Patch1:		xca-0.6.4-includes.patch
Patch2:		xca-0.6.4-openssl10.patch
URL:		http://www.hohnstaedt.de/xca/xca.html
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	db-devel
BuildRequires:	openssl-devel
BuildRequires:	linuxdoc-tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
XCA uses a Berkeley DB for storage and supports RSA keys,
certificate signing requests (PKCS#10) and Certificates (X509v3)
The signing of requests, and the creation of selfsigned certificates
is supported. Both can use templates for simplicity.
The PKI structures can be imported and exported in several formats
like PKCS#7, PKCS#12, PEM, DER, PKCS#8.

%prep
%setup -q
%patch0 -p1 -b .lib64
%patch1 -p1 -b .includes
%patch2 -p1 -b .openssl10

perl -n -i -e '$/="\r\n";chomp;print;print "\n"' COPYRIGHT
perl -pi -e 's,\/usr\/lib\/,%{_libdir},g' configure

%build
CFLAGS="$RPM_OPT_FLAGS -I%{qt4include}/Qt -fpermissive" \
QTDIR="%{qt4dir}" \
prefix=%{_prefix} ./configure
%make

%install
rm -rf %{buildroot}
make destdir=%{buildroot} prefix=%{_prefix} mandir=share/man install

rm -f %{buildroot}%{_datadir}/pixmaps/xca.xpm

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m644 %{SOURCE11} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%files
%defattr(-,root,root, 755)
%doc AUTHORS COPYRIGHT
%doc doc/*.html
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/xca-32x32.xpm
%{_datadir}/applications/*.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

