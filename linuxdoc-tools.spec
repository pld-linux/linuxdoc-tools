# TODO: replace sgml-tools?
Summary:	A text formatting package based on SGML
Summary(pl.UTF-8):	Pakiet do formatowania tektu w oparciu o SGML
Name:		linuxdoc-tools
Version:	0.9.82
Release:	1
License:	MIT
Group:		Applications/Publishing/SGML
#Source0Download: https://gitlab.com/agmartin/linuxdoc-tools/-/tags
Source0:	https://gitlab.com/agmartin/linuxdoc-tools/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	d2b7c338fa84144cc29658205ec13aaa
Patch0:		%{name}-catalogs.patch
URL:		https://gitlab.com/agmartin/linuxdoc-tools
BuildRequires:	autoconf >= 2.50
BuildRequires:	flex
BuildRequires:	gawk
BuildRequires:	groff
BuildRequires:	jade
BuildRequires:	perl-base >= 1:5.10.1
BuildRequires:	rpm-perlprov
BuildRequires:	sgml-common
BuildRequires:	texinfo
Requires:	jade
Requires:	gawk
Requires:	groff
Requires:	sgml-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linuxdoc-tools is a text formatting suite based on SGML (Standard
Generalized Markup Language), using the LinuxDoc document type.
Linuxdoc-tools allows you to produce LaTeX, HTML, GNU info, LyX, RTF,
plain text (via groff), and other format outputs from a single SGML
source. Linuxdoc-tools is intended for writing technical software
documentation.

%description -l pl.UTF-8
Linuxdoc-tools to pakiet do formatowania tekstu oparty na SGML-u
(Standard Generalized Markup Language), wykorzystujący typ dokumentu
LinuxDoc. Pozwala tworzyć wyjście w formacie LaTeX, HTML, GNU info,
LyX, RTF, czystego tekstu (poprzez groff) i innych z pojedynczego
źródła SGML. Przeznaczony jest do pisania technicznej dokumentacji
oprogramowania.

%prep
%setup -q
%patch -P0 -p1

%build
%{__autoconf}
%configure \
	--with-installed-nsgmls \
	--with-installed-iso-entities \
	--disable-docs

cd entity-map
%{__autoconf}
%configure
cd ..

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# belong to sgml-tools
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{rtf2rtf,sgml2*,sgmlcheck,sgmlpre}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{rtf2rtf,sgml2*,sgmlcheck,sgmlpre}.1*
%{__rm} $RPM_BUILD_ROOT%{_datadir}/entity-map/0.1.0/{ISOdia,ISOlat1,ISOlat2,ISOnum,ISOpub,ISOtech,lat1.2sdata,*.{2ab,2as,2html,2l1b,2l1s,2l1tr,2rtf,2tex,2texi,2tr}}
# belong to nsgmls
%{__rm} $RPM_BUILD_ROOT%{_bindir}/sgmlsasp
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/sgmlsasp.1*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/linuxdoc
%{_datadir}/%{name}
# additional files (there are some differences in few common ones...)
%{_datadir}/entity-map/0.1.0/GFextra.2u8b
%{_datadir}/entity-map/0.1.0/ISOdia.2u8b
%{_datadir}/entity-map/0.1.0/ISOlat1.2u8b
%{_datadir}/entity-map/0.1.0/ISOlat1.2u8s
%{_datadir}/entity-map/0.1.0/ISOlat1.2u8tr
%{_datadir}/entity-map/0.1.0/ISOnum.2u8b
%{_datadir}/entity-map/0.1.0/ISOpub.2u8b
%{_datadir}/entity-map/0.1.0/ISOtech.2u8b
%{_mandir}/man1/linuxdoc.1*
