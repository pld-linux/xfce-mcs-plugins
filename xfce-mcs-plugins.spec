Summary:	Plugins for multi channel settings manager
Summary(pl.UTF-8):   Wtyczki dla zarządcy ustawień wielokanałowych
Name:		xfce-mcs-plugins
Version:	4.3.90.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive//xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	4fd5b8f1f531bcc66f6aeaff76998f0c
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.10.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= %{version}
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires:	gtk+2 >= 1:2.10.0
Requires:	xfce-mcs-manager >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-plugins is a set of plugins for the multi channel settings
manager.

%description -l pl.UTF-8
xfce-mcs-plugins to zbiór wtyczek dla zarządcy ustawień
wielokanałowych.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
LDFLAGS="%{rpmldflags} -Wl,--as-needed"
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

%post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(it) %{_datadir}/xfce4/doc/it/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/*/*

%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so

%{_desktopdir}/*.desktop
