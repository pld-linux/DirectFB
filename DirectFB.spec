Summary:	DirectFB - Hardware graphics accelration.
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11
Group(de):	X11
Group(pl):	X11
Source0:	http://directfb.org/download/%{name}-%{version}.tar.gz
URL:		htt://directfs.org/
BuildRequires:	libpng >= 1.0.10
Buildrequires:	zlib >= 1.1.3
BuildRequires:	libjpeg 
BuildRequires:	freetype >= 2.0.2
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package devel
Group:		X11
Group(de):	X11
Group(pl):	X11
Summary:	DirectFB - development package.
Summary(pl):	DirectFB - pliki naglowkowe.

%description devel
DirectFB header files.

%description -l pl devel
Pliki naglowkowe dla DirectFB.

%package doc
Group:		X11
Group(de):	X11
Group(pl):	X11
Summary:	DirectFB - documentation.
Summary(pl):	DirectFB - dokumantacja.

%description doc
DirectFB documentation

%description -l pl doc
Dokumentacja dla systemu DirectFB

%prep
%setup -q

#%patch

%build
%configure --prefix=%{_prefix} \
	--disable-maintainer-mode \
	--enable-static \
	--enable-shared \
	--disable-fast-install \
	--disable-debug \
	--enable-mmx 

%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/df_*
%attr(755,root,root) %{_bindir}/directfb-config
%dir %{_libdir}/directfb
%dir %{_libdir}/directfb/*
%attr(755,root,root) %{_libdir}/directfb/*/*.so
%attr(755,root,root) %{_libdir}/*.so
%{_pkgconfigdir}/directfb.pc
%dir %{_datadir}/directfb
%dir %{_datadir}/directfb/fonts
%{_datadir}/directfb/cursor.dat

%files devel
%defattr(644,root,root,755)
%{_includedir}/directfb.h
%{_libdir}/directfb/*/*.a
%{_libdir}/directfb/*/*.la
%{_libdir}/*.la
%{_libdir}/*.a

%files doc
%defattr(644,root,root,755)
%doc docs/html/*
%dir %{_datadir}/directfb/examples
