Summary:	gCVS is a GTK port of WinCVS, a Windows-based CVS client
Name:		gcvs
Version:	1.0a4
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://www.wincvs.org/%{name}-%{version}.tar.gz
Patch0:		gcvs-nocvsunix.patch
URL:		http://www.wincvs.org/
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
Requires:	tcl
Requires:	cvs >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gCVS is a GTK port of WinCVS, a Windows-based CVS client.

%prep
%setup -q
%patch0 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti"
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
%configure
make

cd cvsunix
%configure
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT

install cvsunix/src/cvs $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%doc GuiDoc/cvsgui*html
%attr(755,root,root) %{_bindir}/gcvs
%{_datadir}/%{name}
