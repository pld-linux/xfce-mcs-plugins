Summary:	Plugins for multi channel settings manager
Summary(pl):	Wtyczki dla zarz±dcy ustawieñ wielokana³owych
Name:		xfce-mcs-plugins
Version:	4.1.99.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	41034a32a0f57e7fd2ba6e3bc80ac7b2
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.1.2
Requires:	gtk+2 >= 1:2.2.0
Requires:	xfce-mcs-manager >= 4.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-plugins is a set of plugins for the multi channel settings
manager.

%description -l pl
xfce-mcs-plugins to zbiór wtyczek dla zarz±dcy ustawieñ
wielokana³owych.

%prep
%setup -q
%patch0 -p1

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
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/images/*.png
%lang(it) %{_datadir}/xfce4/doc/it/*.html
%lang(it) %{_datadir}/xfce4/doc/it/images/*.png
%{_iconsdir}/hicolor/*/*/*

%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so

%{_desktopdir}/*.desktop
