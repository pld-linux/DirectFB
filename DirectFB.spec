#
# Conditional build:
# _without_flash	- don't build FLASH support
# _without_mpg		- don't build support for MPG/MPEG3
#
Summary:	DirectFB - Hardware graphics acceleration
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.14
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/%{name}/%{name}-%{version}.tar.gz
Source1:	http://www.directfb.org/download/DirectFB/DFBTutorials-0.5.0.tar.gz
Patch0:		%{name}-am.patch
URL:		http://www.directfb.org/
#BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_flash:BuildRequires:	flash-devel >= 0.4.10-5}
BuildRequires:	freetype-devel >= 2.0.2
BuildRequires:	libjpeg-devel >= 6b
%{!?_without_mpg:BuildRequires:	libmpeg3-devel}
BuildRequires:	libpng-devel >= 1.0
BuildRequires:	libtool
BuildRequires:	zlib-devel >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir	%{_libdir}/directfb-%{version}

%description
DirectFB hardware graphics acceleration - libraries.

%description -l pl
Wspomaganie grafiki DirectFB - biblioteki.

%package devel
Summary:	DirectFB - development package
Summary(pl):	DirectFB - pliki nag��wkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
DirectFB header files.

%description devel -l pl
Pliki nag��wkowe dla DirectFB.

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

%package font-ft2
Summary:	FreeType2 font provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj�ca fonty poprzez FreeType2
Group:		Libraries
Requires:	%{name} = %{version}

%description font-ft2
This package contains FreeType2 font provider for DirectFB.

%description font-ft2 -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczaj�c� fonty poprzez
bibliotek� FreeType2.

%package image-jpeg
Summary:	JPEG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczajaca grafik� JPEG
Group:		Libraries
Requires:	%{name} = %{version}

%description image-jpeg
This package contains JPEG image provider for DirectFB.

%description image-jpeg -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczaj�c� grafik� JPEG.

%package image-png
Summary:	PNG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczajaca grafik� PNG
Group:		Libraries
Requires:	%{name} = %{version}

%description image-png
This package contains PNG image provider for DirectFB.

%description image-png -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczaj�c� grafik� PNG.

%package video-libmpeg3
Summary:	MPEG video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj�ca obraz MPEG
Group:		Libraries
Requires:	%{name} = %{version}

%description video-libmpeg3
This package contains MPEG (MPEG-1 and MPEG-2) video provider for
DirectFB. It uses libmpeg3 library.

%description video-libmpeg3 -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczajac� obraz MPEG
(MPEG-1 i MPEG-2) przy u�yciu biblioteki libmpeg3. 

%package video-swf
Summary:	ShockWave Flash video provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj�ca obraz ShockWave Flash
Group:		Libraries
Requires:	%{name} = %{version}

%description video-swf
This package contains SWF (ShockWave Flash) video provider for
DirectFB. It uses flash library.

%description video-swf -l pl
Ten pakiet zawiera wtyczk� dla DirectFB dostarczaj�c� obraz SWF
(ShockWave Flash) przy u�yciu biblioteki flash.

%prep
%setup -q -a1
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# paths for libmpeg3 and libflash
CPPFLAGS="-I/usr/include/libmpeg3 -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
# SDL core disabled (used directly, not through plugin - too many deps)
# MMX and SSE are detected at runtime, so it's safe to enable
%configure \
	--disable-maintainer-mode \
	--enable-shared \
	--enable-static \
	--disable-fast-install \
	--disable-debug \
	%{?_without_flash:--disable-flash} \
	%{?_without_mpg:--disable-libmpeg3} \
	--disable-avifile \
	--disable-sdl \
%ifarch i586 i686 athlon
	--enable-mmx \
%endif
%ifarch i686 athlon
	--enable-sse
%endif

%{__make}

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
%dir %{dfbdir}
%dir %{dfbdir}/gfxdrivers
%attr(755,root,root) %{dfbdir}/gfxdrivers/*.??
%dir %{dfbdir}/inputdrivers
%attr(755,root,root) %{dfbdir}/inputdrivers/*.??
%dir %{dfbdir}/interfaces
%dir %{dfbdir}/interfaces/IDirectFBFont
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_default.??
%dir %{dfbdir}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_gif.??
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.??
%dir %{dfbdir}/interfaces/IDirectFBVideoProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.??
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
%{dfbdir}/gfxdrivers/*.a
%{dfbdir}/inputdrivers/*.a
%{dfbdir}/interfaces/*/*.a

%files doc
%defattr(644,root,root,755)
%doc docs/html/*
%{_examplesdir}/%{name}-%{version}

%files font-ft2
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_ft2.??

%files image-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg.??

%files image-png
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_png.??

%if %{!?_without_mpg:1}%{?_without_mpg:0}
%files video-libmpeg3
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.??
%endif

%if %{!?_without_flash:1}%{?_without_flash:0}
%files video-swf
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swf.??
%endif
