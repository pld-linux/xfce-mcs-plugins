Summary: 	Plugins for multi channel settings manager
Name: 		xfce-mcs-plugins
Version: 	3.90.0
Release: 	0.1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	b7c0cca24b59f7ea937cd2ac35bbce87
Group: 		X11/Applications
Requires:	gtk+2 >= 2.0.0
Requires:	xfce-mcs-manager >= 0.2.0
BuildRequires: 	gtk+2-devel >= 2.0.0
BuildRequires:	xfce-mcs-manager-devel >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-plugins is a set of plugins for the multi channel settings manager

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL TODO COPYING AUTHORS
%{_datadir}/xfce4/doc
%{_datadir}/locale/
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_libdir}/xfce4/mcs-plugins/*.la
%{_libdir}/xfce4/mcs-plugins/*.a
