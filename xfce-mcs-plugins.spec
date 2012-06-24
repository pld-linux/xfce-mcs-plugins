Summary:	Plugins for multi channel settings manager
Summary(pl):	Wtyczki dla zarz�dcy ustawie� wielokana�owych
Name:		xfce-mcs-plugins
Version:	3.99.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce4-rc4/src/%{name}-%{version}.tar.gz
# Source0-md5:	6efd37806454a10820b97df62355de4a
URL:		http://www.xfce.org/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	intltool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 3.99.4
Requires:	gtk+2 >= 2.0.0
Requires:	xfce-mcs-manager >= 3.99.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-plugins is a set of plugins for the multi channel settings
manager.

%description -l pl
xfce-mcs-plugins to zbi�r wtyczek dla zarz�dcy ustawie�
wielokana�owych.

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
