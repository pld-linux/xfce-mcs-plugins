
%define		_snap 20040806

Summary:	Plugins for multi channel settings manager
Summary(pl):	Wtyczki dla zarządcy ustawień wielokanałowych
Name:		xfce-mcs-plugins
Version:	4.2.0
Release:	0.%{_snap}
License:	GPL
Group:		X11/Applications
Source0:	http://wp09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	fed9b98156a08fc40aedfd8993100081
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.0.0
Requires:	gtk+2 >= 2.0.6
Requires:	xfce-mcs-manager >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-plugins is a set of plugins for the multi channel settings
manager.

%description -l pl
xfce-mcs-plugins to zbiór wtyczek dla zarządcy ustawień
wielokanałowych.

%prep
%setup -q -n %{name}
%patch0 -p1

mv -f po/{fa_IR,fa}.po
mv -f po/{pt_PT,pt}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
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
%lang(it) %{_datadir}/xfce4/doc/it/
%{_iconsdir}/hicolor/*/*/*

%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so

%{_desktopdir}/*.desktop
