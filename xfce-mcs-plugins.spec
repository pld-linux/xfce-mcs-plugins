Summary: 	Plugins for multi channel settings manager
Summary(pl):	Wtyczki dla zarz±dcy ustawieñ wielokana³owych
Name: 		xfce-mcs-plugins
Version: 	3.90.0
Release: 	0.1
License:	GPL
Group: 		X11/Applications
Source0: 	http://dl.sourceforge.net/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	b7c0cca24b59f7ea937cd2ac35bbce87
URL: 		http://www.xfce.org/
BuildRequires: 	gtk+2-devel >= 2.0.0
BuildRequires:	intltool
BuildRequires:	xfce-mcs-manager-devel >= 0.2.0
Requires:	gtk+2 >= 2.0.0
Requires:	xfce-mcs-manager >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-plugins is a set of plugins for the multi channel settings
manager.

%description -l pl
xfce-mcs-plugins to zbiór wtyczek dla zarz±dcy ustawieñ
wielokana³owych.

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
%{_datadir}/xfce4/doc/*/*.html
%{_datadir}/xfce4/doc/*/images/*.png
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/mcs-plugins
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
