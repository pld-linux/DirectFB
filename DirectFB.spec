Summary:	DirectFB - Hardware graphics accelration.
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.4
Release:	1
License:	GPL
Group:		System/Graphics
Group(pl):	System/Grafika
Source0:	http://www.directfb.org/download/%{name}/%{name}-%{version}.tar.gz
URL:		htt://www.directfb.org/
BuildRequires:	libpng-devel >= 1.0.10
BuildRequires:	zlib-devel >= 1.1.3
BuildRequires:	libjpeg-devel
BuildRequires:	freetype-devel >= 2.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package devel
Group:		System/Development
Group(pl):	System/Programowanie
Summary:	DirectFB - development package.
Summary(pl):	DirectFB - pliki naglowkowe.

%description devel
DirectFB header files.

%description -l pl devel
Pliki naglowkowe dla DirectFB.

%package doc
Group:		System/Documentation
Group(pl):	System/Dokumantacja
Summary:	DirectFB - documentation.
Summary(pl):	DirectFB - dokumantacja.

%description doc
DirectFB documentation and examples

%description -l pl doc
Dokumentacja dla systemu DirectFB wraz z przykladami

%prep
%setup -q

%build
aclocal
autoconf
automake -a -c
%configure --prefix=%{_prefix} \
	--disable-maintainer-mode \
	--enable-shared \
	--disable-fast-install \
	--disable-debug \
    --disable-avifile \
	--enable-mmx 

%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/directfb/*/*.so
%attr(755,root,root) %{_libdir}/*.so
%{_pkgconfigdir}/directfb.pc
%dir %{_datadir}/directfb
%dir %{_datadir}/directfb/fonts
%{_datadir}/directfb/cursor.dat

%files devel
%defattr(644,root,root,755)
%{_includedir}/directfb.h
%{_libdir}/directfb/*/*.la
%{_libdir}/*.la
%{_libdir}/lib*.so.*

%files doc
%defattr(644,root,root,755)
%doc docs/html/*
%dir %{_datadir}/directfb/examples
