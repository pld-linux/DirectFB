#
# Conditional build:
# _without_mpg		- don't build support for MPG/MPEG3
#
Summary:	DirectFB - Hardware graphics acceleration
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.19
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8af7f3b5d2c3cc2cb7aba4662ec0b73f
Source1:	http://www.directfb.org/download/DirectFB/DFBTutorials-0.5.0.tar.gz
# Source1-md5:	13e443a64bddd68835b574045d9025e9
Patch0:		%{name}-am.patch
Patch1:         %{name}-pmake.patch
Patch2:         %{name}-i810.patch
URL:		http://www.directfb.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
Summary(pl):	DirectFB - dokumentacja
Group:		Development/Libraries

%description doc
DirectFB documentation and tutorials.

%description doc -l pl
Dokumentacja dla systemu DirectFB wraz z wprowadzeniem.

%package core-sdl
Summary:	SDL core system for DirectFB
Summary(pl):	System SDL dla DirectFB
Group:		Libraries
Requires:	%{name} = %{version}

%description core-sdl
This package contains SDL core system module for DirectFB.

%description core-sdl -l pl
Ten pakiet zawiera modu³ systemu SDL dla DirectFB.

%package font-ft2
Summary:	FreeType2 font provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca fonty poprzez FreeType2
Group:		Libraries
Requires:	%{name} = %{version}

%description font-ft2
This package contains FreeType2 font provider for DirectFB.

%description font-ft2 -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± fonty poprzez
bibliotekê FreeType2.

%package image-jpeg
Summary:	JPEG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca grafikê JPEG
Group:		Libraries
Requires:	%{name} = %{version}

%description image-jpeg
This package contains JPEG image provider for DirectFB.

%description image-jpeg -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± grafikê JPEG.

%package image-png
Summary:	PNG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca grafikê PNG
Group:		Libraries
Requires:	%{name} = %{version}

%description image-png
This package contains PNG image provider for DirectFB.

%description image-png -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± grafikê PNG.

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

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/libmpeg3"
# MMX and SSE are detected at runtime, so it's safe to enable
%configure \
	--disable-maintainer-mode \
	--enable-shared \
	--enable-static \
	--enable-fast-install \
	--disable-debug \
	%{?_without_mpg:--disable-libmpeg3} \
	--enable-sdl \
%ifarch i586 i686 athlon
	--enable-mmx \
%endif
%ifarch i686 athlon
	--enable-sse
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf DFBTutorials* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# dbfdump and dfbg require multi-application core - useless now
%attr(755,root,root) %{_bindir}/dfbinfo
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{dfbdir}
%dir %{dfbdir}/gfxdrivers
%attr(755,root,root) %{dfbdir}/gfxdrivers/*.so
%dir %{dfbdir}/inputdrivers
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_joystick.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_keyboard.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_lirc.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_ps2mouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_serialmouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sonypi.so
%dir %{dfbdir}/interfaces
%dir %{dfbdir}/interfaces/IDirectFBFont
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_default.so
%dir %{dfbdir}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_gif.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.so
%dir %{dfbdir}/interfaces/IDirectFBVideoProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.so
%dir %{dfbdir}/systems
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_fbdev.so
%{_datadir}/directfb-%{version}
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/directfb-config
%attr(755,root,root) %{_bindir}/directfb-csource
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/directfb
%{_includedir}/directfb-internal
%{_pkgconfigdir}/*
%{_mandir}/man1/directfb-csource.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{dfbdir}/gfxdrivers/*.*a
%{dfbdir}/inputdrivers/*.*a
%{dfbdir}/interfaces/*/*.*a
%{dfbdir}/systems/*.*a

%files doc
%defattr(644,root,root,755)
%doc docs/html/*
%{_examplesdir}/%{name}-%{version}

%files core-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sdlinput.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_sdl.so

%files font-ft2
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_ft2.so

%files image-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg.so

%files image-png
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_png.so

%if 0%{!?_without_mpg:1}
%files video-libmpeg3
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.so
%endif
