#
%define		snap 20040616
#
Summary:	Plugins for multi channel settings manager
Summary(pl):	Wtyczki dla zarz±dcy ustawieñ wielokana³owych
Name:		xfce-mcs-plugins
Version:	4.1.0
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	8879cc9042621a9df2ee0ead68fe8f57
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires:	gtk+2 >= 2.0.0
Requires:	xfce-mcs-manager >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-plugins is a set of plugins for the multi channel settings
manager.

%description -l pl
xfce-mcs-plugins to zbiór wtyczek dla zarz±dcy ustawieñ
wielokana³owych.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/

%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so

%{_desktopdir}/*.desktop
