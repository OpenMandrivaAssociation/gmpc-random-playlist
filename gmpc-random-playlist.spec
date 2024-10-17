Summary:	A random playlist plugin for gmpc
Name:		gmpc-random-playlist
Version:	0.15.5.0
Release:	7
License:	GPLv2+
Group:		Sound
Url:		https://www.sarine.nl/
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libmpd)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	libglade2.0-devel
BuildRequires:	gmpc-devel
Requires:	gmpc

%description
A random playlist plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_datadir}/gmpc/plugins/librandomplaylist.so


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.5.0-4mdv2011.0
+ Revision: 618977
- the mass rebuild of 2010.0 packages

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246319
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160418
- add spec file
- add source
- Created package structure for gmpc-random-playlist.

