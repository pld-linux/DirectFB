Summary:	DirectFB - Hardware graphics acceleration
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.12
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.directfb.org/download/%{name}/%{name}-%{version}.tar.gz
Source1:	http://www.directfb.org/download/DirectFB/DFBTutorials-0.4.2.tar.gz
Patch0:		%{name}-am.patch
URL:		http://www.directfb.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flash-devel
BuildRequires:	freetype-devel >= 2.0.2
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libmpeg3-devel
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	zlib-devel >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectFB hardware graphics acceleration - libraries.

%description -l pl
Wspomaganie grafiki DirectFB - biblioteki.

%package devel
Summary:	DirectFB - development package
Summary(pl):	DirectFB - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
DirectFB header files.

%description devel -l pl
Pliki nag³ówkowe dla DirectFB.

%package static
Summary:	DirectFB static libraries
Summary(pl):	Statyczne biblioteki DirectFB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
DirectFB static libraries.

%description static -l pl
Statyczne biblioteki DirectFB.

%package doc
Summary:	DirectFB - documentation
Summary(pl):	DirectFB - dokumantacja
Group:		Development/Libraries

%description doc
DirectFB documentation and tutorials.

%description doc -l pl
Dokumentacja dla systemu DirectFB wraz z wprowadzeniem.

%package video-libmpeg3
Summary:	MPEG video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca obraz MPEG
Group:		Libraries
Requires:	%{name} = %{version}

%description video-libmpeg3
This package contains MPEG (MPEG-1 and MPEG-2) video provider for
DirectFB. It uses libmpeg3 library.

%description video-libmpeg3 -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczajac± obraz MPEG
(MPEG-1 i MPEG-2) przy u¿yciu biblioteki libmpeg3. 

%package video-swf
Summary:	ShockWave Flash video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca obraz ShockWave Flash
Group:		Libraries
Requires:	%{name} = %{version}

%description video-swf
This package contains SWF (ShockWave Flash) video provider for
DirectFB. It uses flash library.

%description video-swf -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± obraz SWF
(ShockWave Flash) przy u¿yciu biblioteki flash.

%prep
%setup -q -a1
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
aclocal
%{__autoconf}
%{__automake}
# paths for libmpeg3 and libflash
CPPFLAGS="-I/usr/include/libmpeg3 -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
%configure \
	--disable-maintainer-mode \
	--enable-shared \
	--enable-static \
	--disable-fast-install \
	--disable-debug \
	--disable-avifile \
%ifarch i586 i686 athlon
	--enable-mmx=on
%endif
# MMX is detected at runtime, so it's safe

%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -rf DFBTutorials* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/directfb-%{version}
%dir %{_libdir}/directfb-%{version}/gfxdrivers
%attr(755,root,root) %{_libdir}/directfb-%{version}/gfxdrivers/*.??
%dir %{_libdir}/directfb-%{version}/inputdrivers
%attr(755,root,root) %{_libdir}/directfb-%{version}/inputdrivers/*.??
%dir %{_libdir}/directfb-%{version}/interfaces
%dir %{_libdir}/directfb-%{version}/interfaces/IDirectFBFont
%attr(755,root,root) %{_libdir}/directfb-%{version}/interfaces/IDirectFBFont/*.??
%dir %{_libdir}/directfb-%{version}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{_libdir}/directfb-%{version}/interfaces/IDirectFBImageProvider/*.??
%dir %{_libdir}/directfb-%{version}/interfaces/IDirectFBVideoProvider
%attr(755,root,root) %{_libdir}/directfb-%{version}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.??
%{_datadir}/directfb-%{version}
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/directfb-config
%{_includedir}/directfb
%{_includedir}/directfb-internal
%{_pkgconfigdir}/*
%{_libdir}/*.la
%{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/directfb-%{version}/gfxdrivers/*.a
%{_libdir}/directfb-%{version}/inputdrivers/*.a
%{_libdir}/directfb-%{version}/interfaces/*/*.a

%files doc
%defattr(644,root,root,755)
%doc docs/html/*
%{_examplesdir}/%{name}-%{version}

%files video-libmpeg3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/directfb-%{version}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.??

%files video-swf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/directfb-%{version}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swf.??
