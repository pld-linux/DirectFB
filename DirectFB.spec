Summary:	DirectFB - Hardware graphics accelration.
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.0
Release:	1
Copyright:	GPL
Group:		X11	
Group(pl):	X11
Source:		http://directfb.org/download/%{name}-%{version}.tar.gz
URL:		htt://directfs.org/
BuildRequires:	libpng >= 1.0.10
Buildrequires:	zlib >= 1.1.3
BuildRequires:	libjpeg 
BuildRequires:	freetype >= 2.0.2
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%package devel
Group:		X11
Group(pl):	X11
Summary:	DirectFB - development package.
Summary(pl):	DirectFB - pliki naglowkowe.

%description devel
DirectFB header files.

%description -l pl devel
Pliki naglowkowe dla DirectFB.

%package doc
Group:		X11
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
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%attr(755,root,root) %{_bindir}/df_*
%attr(755,root,root) %{_bindir}/directfb-config
%attr(644,root,root) %{_libdir}/directfb/*/*.so
%attr(644,root,root) %{_libdir}/pkgconfig/directfb.pc
%attr(644,root,root) %{_libdir}/*.so
%dir %{_datadir}/directfb/fonts
%attr(644,root,root) %{_datadir}/directfb/cursor.dat

%files devel
%attr(644,root,root) %{_includedir}/directfb.h
%attr(644,root,root) %{_libdir}/directfb/*/*.a
%attr(644,root,root) %{_libdir}/directfb/*/*.la
%attr(644,root,root) %{_libdir}/*.la
%attr(644,root,root) %{_libdir}/*.a

%files doc
%doc docs/html/*
%dir %{_datadir}/directfb/examples/
