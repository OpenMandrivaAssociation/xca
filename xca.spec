%define	name	xca
%define version 0.5.1
%define release %mkrel 4
%define	Summary	A GUI for handling X509 certificates, RSA keys and PKCS#10 Requests

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		System/Servers
Source0:	http://prdownloads.sourceforge.net/xca/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		xca-qfont.patch
Patch1:		xca-0.5.1-gcc.patch
Url:		http://www.hohnstaedt.de/xca/xca.html
BuildRequires:	libqt-devel >= 2.2.4
BuildRequires:	db-devel >= 3.3
BuildRequires:	openssl-devel >= 0.9.6

%description
The Program uses a Berkeley db for storage and supports RSA keys,
Certificate signing requests (PKCS#10) and Certificates (X509v3)
The signing of requests, and the creation of selfsigned certificates
is supported. Both can use templates for simplicity.
The PKI structures can be imported and exported in several formats
like PKCS#7, PKCS#12, PEM, DER, PKCS#8.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

perl -n -i -e '$/="\r\n";chomp;print;print "\n"' COPYRIGHT
perl -p -i -e 's@/lib/@/%{_lib}/@;s@/lib @/%{_lib} @' configure

%build
CFLAGS="$RPM_OPT_FLAGS" \
prefix=%{_prefix} ./configure
%make

%install
rm -rf $RPM_BUILD_ROOT
make destdir=$RPM_BUILD_ROOT prefix=%{_prefix} mandir=share/man install

rm -f $RPM_BUILD_ROOT%{_datadir}/applications/xca.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/xca.xpm

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/xca
?package(%{name}): \
	command="%{name}" \
	icon="%{name}.png" \
	needs="x11" \
	title="X-CA" \
	longtitle="%{Summary}" \
	section="System/Configuration/Other"
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root, 755)
%doc AUTHORS README COPYRIGHT debian/changelog
%doc doc/*.html
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

