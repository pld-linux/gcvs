Summary:	gCVS is a GTK+ port of WinCVS, a Windows-based CVS client
Summary(pl):	Sportowany pod GTK+ WinCVS - klient CVS
Name:		gcvs
Version:	1.0
Release:	4
Epoch:		2
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/cvsgui/%{name}-%{version}.tar.bz2
# Source0-md5:	063b5805eda434f47251af9278168adb
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-nocvsunix.patch
Patch1:		%{name}-ambiguous.patch
Patch2:		%{name}-types.patch
URL:		http://www.wincvs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libstdc++-devel
BuildRequires:	tcl-devel
BuildRequires:	unzip
Requires:	cvs >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gCVS is a GTK+ port of WinCVS, a Windows-based CVS client.

%description -l pl
gCVS jest bazowanym na Windows klientem CVS, u¿ywaj±cym bibliotek GTK+.
Pozwala na wygodne operacje w CVS poprzez graficzny interfejs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/gcvs.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc GuiDoc/cvsgui*html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/gcvs.desktop
%{_pixmapsdir}/gcvs.png
