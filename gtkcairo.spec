Summary:	GtkCairo - a Cairo surface widget for GTK+
Summary(pl):	GtkCairo - widget powierzchni Cairo dla GTK+
Name:		gtkcairo
Version:	0.3
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
# Source0-md5:	d5d51cdef855edf7829c1cdf7e7e312f
URL:		http://cairographics.org/cairo/GtkCairo
BuildRequires:	cairo-devel >= 0.1.1
BuildRequires:	glitz-devel >= 0.1.3
BuildRequires:	gtk+2-devel >= 2.0.0
Requires:	cairo >= 0.1.1
Requires:	glitz >= 0.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkCairo provides a widget with a custom redraw handler, that can be
extended for other widgets using cairo, it currently supports the
xlib/xrender and glitz backends.

%description -l pl
GtkCairo dostarcza widget z w³asn± procedur± obs³ugi przerysowania,
który mo¿e rozszerzaæ inne widgety przy u¿yciu cairo. Aktualnie
obs³uguje backendy xlib/xrender i glitz.

%package devel
Summary:	Header files for GtkCairo library
Summary(pl):	Pliki nag³ówkowe biblioteki GtkCairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 0.1.1
Requires:	glitz-devel >= 0.1.3
Requires:	gtk+2-devel >= 2.0.0

%description devel
Header files for GtkCairo library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GtkCairo.

%package static
Summary:	Static GtkCairo library
Summary(pl):	Statyczna biblioteka GtkCairo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GtkCairo library.

%description static -l pl
Statyczna biblioteka GtkCairo.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gtkcairo.h
%{_pkgconfigdir}/gtkcairo.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
