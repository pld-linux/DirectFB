#
# Conditional build:
# _without_mpg		- don't build support for MPG/MPEG3
#
Summary:	DirectFB - Hardware graphics acceleration
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.17
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	d373fa1d604ab5ea4e8fdcb875876cfd
Source1:	http://www.directfb.org/download/DirectFB/DFBTutorials-0.5.0.tar.gz
# Source1-md5:	13e443a64bddd68835b574045d9025e9
Patch0:		%{name}-am.patch
Patch1:         %{name}-pmake.patch
URL:		http://www.directfb.org/
#BuildRequires:	SDL-devel
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

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/libmpeg3"
# SDL core disabled (used directly, not through plugin - too many deps)
# MMX and SSE are detected at runtime, so it's safe to enable
%configure \
	--disable-maintainer-mode \
	--enable-shared \
	--enable-static \
	--disable-fast-install \
	--disable-debug \
	%{?_without_mpg:--disable-libmpeg3} \
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
%attr(755,root,root) %{dfbdir}/gfxdrivers/*.so
%{dfbdir}/gfxdrivers/*.la
%dir %{dfbdir}/inputdrivers
%attr(755,root,root) %{dfbdir}/inputdrivers/*.so
%{dfbdir}/inputdrivers/*.la
%dir %{dfbdir}/interfaces
%dir %{dfbdir}/interfaces/IDirectFBFont
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_default.so
%{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_default.la
%dir %{dfbdir}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_gif.so
%{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_gif.la
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.so
%{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.la
%dir %{dfbdir}/interfaces/IDirectFBVideoProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.so
%{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.la
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
%{dfbdir}/gfxdrivers/*.a
%{dfbdir}/inputdrivers/*.a
%{dfbdir}/interfaces/*/*.a

%files doc
%defattr(644,root,root,755)
%doc docs/html/*
%{_examplesdir}/%{name}-%{version}

%files font-ft2
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_ft2.so
%{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_ft2.la

%files image-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg.so
%{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg.la

%files image-png
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_png.so
%{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_png.la

%if 0%{!?_without_mpg:1}
%files video-libmpeg3
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.so
%{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.la
%endif
