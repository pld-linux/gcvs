Summary:	gCVS is a GTK port of WinCVS, a Windows-based CVS client
Summary(pl):	Sportowany pod gtk WinCVS - klient CVS
Name:		gcvs
Version:	1.0a6
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	ftp://cvsgui.sourceforge.net/pub/cvsgui/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-nocvsunix.patch
URL:		http://www.wincvs.org/
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libstdc++-devel
BuildRequires:	tcl-devel
BuildRequires:	unzip
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	cvs >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gCVS is a GTK port of WinCVS, a Windows-based CVS client.

%description -l pl
gCVS jest bazowanym na Windows klientem CVS, używającym 
bibliotek GTK. Pozwala na wygodne operacje w CVS poprzez
graficzny interfejs.

%prep
%setup -q
%patch0 -p1

%build
CXXFLAGS="%{rpmcflags} %{!?debug:-fno-rtti}"
%configure2_13
%{__make}

cd cvsunix
%configure2_13
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Development

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install cvsunix/src/cvs $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development/gcvs.desktop

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%doc GuiDoc/cvsgui*html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Development/gcvs.desktop
