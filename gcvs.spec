Summary:	gCVS is a GTK port of WinCVS, a Windows-based CVS client.	
Name:		gcvs
Version:	1.0a4
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://www.wincvs.org/%{name}-%{version}.tar.gz
Source1:	http://www.wincvs.org/howto/wincvs-howto.zip
Patch0:		gcvs-nocvsunix.patch
URL:		http://www.wincvs.org
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	unzip
Requires:	tcl
Requires:	cvs >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gCVS is a GTK port of WinCVS, a Windows-based CVS client.

%package howto
Summary:	gCVS is a GTK port of WinCVS, a Windows-based CVS client.	
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
URL:		http://www.computas.com/pub/wincvs-howto/

%description howto
This document describes day to day usage of the WinCvs 1.0.x client.
It is not an introduction to version control systems, not an
introduction to CVS, and not an introduction to WinCvs. It is more
like a place you may turn to when you know approximately what you want
to do, but don't quite remember how to do it.

%prep
%setup -q
%patch0 -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure
make

cd cvsunix
%configure
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Utilities

install cvsunix/src/cvs $RPM_BUILD_ROOT/%{_bindir}

install -d $RPM_BUILD_ROOT/%{_docdir}/howto/%{name}-%{version}
unzip %{SOURCE1} -d $RPM_BUILD_ROOT/%{_docdir}/howto/%{name}-%{version}

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%doc GuiDoc/cvsgui*html
%attr(755,root,root) %{_bindir}/gcvs
%attr(755,root,root) %{_bindir}/cvs
%{_datadir}/%{name}/

%files howto
%defattr(644,root,root,755)
%{_docdir}/howto/%{name}-%{version}
