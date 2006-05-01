#
# TODO:
#	- fix x86-64 int32<->ptr64 casts.
#
#	tree.c:88: warning: cast from pointer to integer of different size
#	tree.c:102: warning: cast from pointer to integer of different size
#	fonts.c:144: warning: cast to pointer from integer of different size
#	fonts.c:211: warning: cast to pointer from integer of different size
#	gfxcard.c:1451: warning: cast to pointer from integer of different size
#	fbdev.c:459: warning: cast from pointer to integer of different size
#	fbdev.c:578: warning: cast from pointer to integer of different size
#	fbdev.c:708: warning: cast from pointer to integer of different size
#	idirectfbfont_ft2.c:130: warning: cast from pointer to integer of different size
#	idirectfbfont_ft2.c:292: warning: cast from pointer to integer of different size
#	idirectfbfont_ft2.c:653: warning: cast to pointer from integer of different size
#
# Conditional build:
%bcond_with	multi		# build Multi-application core (requires working /dev/fusion*)
#
Summary:	DirectFB - Hardware graphics acceleration
Summary(pl):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	0.9.24
Release:	1.1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Core/%{name}-%{version}.tar.gz
# Source0-md5:	1f4b56b20d4e6f5c6ceb15c1c4fd2ecd
Source1:	http://www.directfb.org/downloads/Extras/DFBTutorials-0.5.0.tar.gz
# Source1-md5:	13e443a64bddd68835b574045d9025e9
Patch0:		%{name}-am.patch
Patch1:		%{name}-pmake.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-sh.patch
Patch4:		%{name}-gcc4.patch
Patch5:		%{name}-llh-ppc.patch
URL:		http://www.directfb.org/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.2
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0
BuildRequires:	libtool
BuildRequires:	libvncserver-devel
%{?with_multi:BuildRequires:	linux-fusion-devel}
BuildRequires:	sed >= 4.0
BuildRequires:	sysfsutils-devel >= 1.3.0-3
BuildRequires:	zlib-devel >= 1.1.3
%{?with_multi:Provides:	DirectFB(multi)}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir	%{_libdir}/directfb-%{version}

%define		specflags	-fno-strict-aliasing

%ifarch %{ix86}
# gcc running out of registers with -O0 in generic_mmx.h
%define		debugcflags	-O1 -g
%endif

%description
DirectFB hardware graphics acceleration - libraries.

%description -l pl
Wspomaganie grafiki DirectFB - biblioteki.

%package devel
Summary:	DirectFB - development package
Summary(pl):	DirectFB - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel >= 1.1.3

%description devel
DirectFB header files.

%description devel -l pl
Pliki nag³ówkowe dla DirectFB.

%package static
Summary:	DirectFB static libraries
Summary(pl):	Statyczne biblioteki DirectFB
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
DirectFB static libraries.

%description static -l pl
Statyczne biblioteki DirectFB.

%package doc
Summary:	DirectFB - documentation
Summary(pl):	DirectFB - dokumentacja
Group:		Documentation

%description doc
DirectFB documentation and tutorials.

%description doc -l pl
Dokumentacja dla systemu DirectFB wraz z wprowadzeniem.

%package core-sdl
Summary:	SDL core system for DirectFB
Summary(pl):	System SDL dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-sdl
This package contains SDL core system module for DirectFB.

%description core-sdl -l pl
Ten pakiet zawiera modu³ systemu SDL dla DirectFB.

%package core-vnc
Summary:	VNC core system for DirectFB
Summary(pl):	System VNC dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-vnc
This package contains VNC core system module for DirectFB.

%description core-vnc -l pl
Ten pakiet zawiera modu³ systemu VNC dla DirectFB.

%package core-x11
Summary:	X11 core system for DirectFB
Summary(pl):	System X11 dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-x11
This package contains X11 core system module for DirectFB.

%description core-x11 -l pl
Ten pakiet zawiera modu³ systemu X11 dla DirectFB.

%package font-ft2
Summary:	FreeType2 font provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca fonty poprzez FreeType2
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description font-ft2
This package contains FreeType2 font provider for DirectFB.

%description font-ft2 -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± fonty poprzez
bibliotekê FreeType2.

%package image-jpeg
Summary:	JPEG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca grafikê JPEG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-jpeg
This package contains JPEG image provider for DirectFB.

%description image-jpeg -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± grafikê JPEG.

%package image-png
Summary:	PNG image provider for DirectFB
Summary(pl):	DirectFB - wtyczka dostarczaj±ca grafikê PNG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-png
This package contains PNG image provider for DirectFB.

%description image-png -l pl
Ten pakiet zawiera wtyczkê dla DirectFB dostarczaj±c± grafikê PNG.

%package input-elo
Summary:	ELO touchscreen input driver for DirectFB
Summary(pl):	Sterownik wej¶ciowy do touchscreenów ELO dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-elo
ELO touchscreen input driver for DirectFB.

NOTE: currently it uses hardcoded /dev/ttyS0 port, so don't install it
unless you don't have ELO device connected to this port. It can mess
with other devices connected to this port (mouse, modem etc.).

%description input-elo -l pl
Sterownik wej¶ciowy do touchscreenów ELO dla DirectFB.

UWAGA: aktualnie u¿ywa zakodowanego na sta³e portu /dev/ttyS0, wiêc
nie nale¿y go instalowaæ, je¶li urz±dzenie ELO nie jest pod³±czone do
tego portu. Sterownik mo¿e utrudniæ wspó³pracê z innymi urz±dzeniami
pod³±czonymi do /dev/ttyS0 (jak mysz, modem itp.).

%package input-mutouch
Summary:	MuTouch touchscreen input driver for DirectFB
Summary(pl):	Sterownik wej¶ciowy do touchscreenów MuTouch dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-mutouch
MuTouch touchscreen input driver for DirectFB.

NOTE: it needs "mut-device" setting in directfbrc in order to work.

%description input-mutouch -l pl
Sterownik wej¶ciowy do touchscreenów MuTouch dla DirectFB.

UWAGA: do dzia³ania potrzebuje ustawienia "mut-device" w directfbrc.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# MMX and SSE are detected at runtime, so it's safe to enable
%configure \
	%{!?debug:--disable-debug} \
	--disable-maintainer-mode \
	--enable-elo-input \
	--enable-fast-install \
	--enable-linux-input \
	%{?with_multi:--enable-multi} \
	--enable-mutouch \
	--enable-sdl \
	--enable-shared \
	--enable-static \
	--enable-unique \
	--enable-video4linux2 \
	--enable-voodoo \
	--enable-x11 \
	--enable-zlib \
%ifarch %{ix86} %{x8664}
%ifnarch i386 i486
	--enable-mmx \
%endif
%ifnarch i386 i486 i586
	--enable-sse
%endif
%endif

%{__make} \
	X11_LIBS=%{_prefix}/X11R6/%{_lib}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf DFBTutorials* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

touch $RPM_BUILD_ROOT%{_sysconfdir}/directfbrc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/dfbdump
%attr(755,root,root) %{_bindir}/dfbg
%attr(755,root,root) %{_bindir}/dfbinfo
%attr(755,root,root) %{_bindir}/dfblayer
%attr(755,root,root) %{_bindir}/dfbproxy
%attr(755,root,root) %{_bindir}/dfbscreen
%attr(755,root,root) %{_bindir}/dfbsummon
%attr(755,root,root) %{_bindir}/uwmdump
%attr(755,root,root) %{_libdir}/libdirect-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libdirectfb-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libfusion-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libuniquewm-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libvoodoo-*.so.*.*.*
%dir %{dfbdir}
%dir %{dfbdir}/gfxdrivers
%attr(755,root,root) %{dfbdir}/gfxdrivers/*.so
%dir %{dfbdir}/inputdrivers
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_joystick.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_keyboard.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_linux_input.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_lirc.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_ps2mouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_serialmouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sonypi.so
%dir %{dfbdir}/interfaces
%dir %{dfbdir}/interfaces/IDirectFB
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFB/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBDataBuffer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBDataBuffer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBDisplayLayer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBDisplayLayer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBEventBuffer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBEventBuffer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBFont
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_default.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_requestor.so
%dir %{dfbdir}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_gif.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_requestor.so
%dir %{dfbdir}/interfaces/IDirectFBInputDevice
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBInputDevice/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBPalette
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBPalette/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBScreen
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBScreen/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBSurface
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBSurface/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBVideoProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.so
%dir %{dfbdir}/interfaces/IDirectFBWindow
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBWindow/lib*.so
%dir %{dfbdir}/systems
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_fbdev.so
%dir %{dfbdir}/wm
%attr(755,root,root) %{dfbdir}/wm/*.so
%{_datadir}/directfb-%{version}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/directfbrc
%{_mandir}/man1/dfbg.1*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/directfb-config
%attr(755,root,root) %{_bindir}/directfb-csource
%attr(755,root,root) %{_libdir}/libdirect.so
%attr(755,root,root) %{_libdir}/libdirectfb.so
%attr(755,root,root) %{_libdir}/libfusion.so
%attr(755,root,root) %{_libdir}/libuniquewm.so
%attr(755,root,root) %{_libdir}/libvoodoo.so
%{_libdir}/libdirect.la
%{_libdir}/libdirectfb.la
%{_libdir}/libfusion.la
%{_libdir}/libuniquewm.la
%{_libdir}/libvoodoo.la
%{_includedir}/directfb
%{_includedir}/directfb-internal
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/directfb-csource.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{dfbdir}/gfxdrivers/*.*[ao]
%{dfbdir}/inputdrivers/*.*[ao]
%{dfbdir}/interfaces/*/*.*[ao]
%{dfbdir}/systems/*.*[ao]
%{dfbdir}/wm/*.*[ao]

%files doc
%defattr(644,root,root,755)
%doc docs/html/*.{html,png}
%{_examplesdir}/%{name}-%{version}

%files core-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sdlinput.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_sdl.so

%files core-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_vncinput.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_vnc.so

%files core-x11
%defattr(644,root,root,755)
%doc systems/x11/README
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_x11input.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_x11.so

%files font-ft2
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_ft2.so

%files image-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg.so

%files image-png
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_png.so

%files input-elo
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_elo.so

%files input-mutouch
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_mutouch.so
