# TODO: --enable-pvr2d when ready [requires PowerVR SDK?]
#
# Conditional build:
%bcond_with	multi		# build Multi-application core (requires working /dev/fusion*)
%bcond_with	sh772x		# SH7722/SH7723 (SH-Mobile) graphics driver
%bcond_without	static_libs	# don't build static libraries
%bcond_without	one		# Linux One IPC library
#
%ifarch sh4
%define		with_sh772x	1
%endif
Summary:	DirectFB - Hardware graphics acceleration
Summary(pl.UTF-8):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	1.6.1
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Core/DirectFB-1.6/%{name}-%{version}.tar.gz
# Source0-md5:	76d3066e75664aa79204af545f2f3c65
Source1:	http://www.directfb.org/downloads/Extras/DFBTutorials-0.5.0.tar.gz
# Source1-md5:	13e443a64bddd68835b574045d9025e9
Patch0:		%{name}-am.patch
Patch1:		%{name}-pmake.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-gcc4.patch
Patch4:		%{name}-llh-ppc.patch
Patch5:		%{name}-zlib.patch
Patch6:		%{name}-update.patch
Patch7:		%{name}-external-one.patch
URL:		http://www.directfb.org/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libGLES-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.2
BuildRequires:	imlib2-devel
BuildRequires:	jasper-devel
BuildRequires:	libdrm-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	libtool
BuildRequires:	libvdpau-devel
BuildRequires:	libvncserver-devel
%{?with_multi:BuildRequires:	linux-fusion-devel >= 8.7}
%{?with_multi:BuildRequires:	linux-fusion-devel < 9}
%{?with_one:BuildRequires:	linux-one-devel >= 1.6.0}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	sysfsutils-devel >= 1.3.0-3
BuildRequires:	tslib-devel >= 1.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	zlib-devel >= 1.1.3
#BuildRequires:	pkgconfig(linotype) -- font provider???
%if %{with sh772x}
BuildRequires:	libshbeu-devel >= 1.0.2
BuildRequires:	libshjpeg-devel >= 1.3.3
BuildRequires:	libuiomux-devel >= 1.5.0
%endif
%{?with_multi:Provides:	DirectFB(multi)}
%ifnarch arm
# ARM-specific
Obsoletes:	DirectFB-input-ucb1x00
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir	%{_libdir}/directfb-1.6-0

%define		specflags	-fno-strict-aliasing

%ifarch %{ix86}
# gcc running out of registers with -O0 in generic_mmx.h
%define		debugcflags	-O1 -g
%endif

%description
DirectFB hardware graphics acceleration - libraries.

%description -l pl.UTF-8
Wspomaganie grafiki DirectFB - biblioteki.

%package devel
Summary:	DirectFB - development package
Summary(pl.UTF-8):	DirectFB - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?with_one:Requires:	linux-one-devel >= 1.6.0}
Requires:	zlib-devel >= 1.1.3

%description devel
DirectFB header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla DirectFB.

%package static
Summary:	DirectFB static libraries
Summary(pl.UTF-8):	Statyczne biblioteki DirectFB
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
DirectFB static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki DirectFB.

%package doc
Summary:	DirectFB - documentation
Summary(pl.UTF-8):	DirectFB - dokumentacja
Group:		Documentation

%description doc
DirectFB documentation and tutorials.

%description doc -l pl.UTF-8
Dokumentacja dla systemu DirectFB wraz z wprowadzeniem.

%package core-mesa
Summary:	Mesa/GLESv2 core system for DirectFB
Summary(pl.UTF-8):	System Mesa/GLESv2 dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-mesa
This package contains Mesa/GLESv2 core system module for DirectFB.

%description core-mesa -l pl.UTF-8
Ten pakiet zawiera moduł systemu Mesa/GLESv2 dla DirectFB.

%package core-sdl
Summary:	SDL core system for DirectFB
Summary(pl.UTF-8):	System SDL dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-sdl
This package contains SDL core system module for DirectFB.

%description core-sdl -l pl.UTF-8
Ten pakiet zawiera moduł systemu SDL dla DirectFB.

%package core-vdpau
Summary:	X11/VDPAU core system for DirectFB
Summary(pl.UTF-8):	System X11/VDPAU dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-vdpau
This package contains X11/VDPAU core system module for DirectFB.

%description core-vdpau -l pl.UTF-8
Ten pakiet zawiera moduł systemu X11/VDPAU dla DirectFB.

%package core-vnc
Summary:	VNC core system for DirectFB
Summary(pl.UTF-8):	System VNC dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-vnc
This package contains VNC core system module for DirectFB.

%description core-vnc -l pl.UTF-8
Ten pakiet zawiera moduł systemu VNC dla DirectFB.

%package core-x11
Summary:	X11 core system for DirectFB
Summary(pl.UTF-8):	System X11 dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-x11
This package contains X11 core system module for DirectFB.

%description core-x11 -l pl.UTF-8
Ten pakiet zawiera moduł systemu X11 dla DirectFB.

%package font-ft2
Summary:	FreeType2 font provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca fonty poprzez FreeType2
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description font-ft2
This package contains FreeType2 font provider for DirectFB.

%description font-ft2 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą fonty poprzez
bibliotekę FreeType2.

%package gfx-sh772x
Summary:	SH7722/SH7723 graphics driver for DirectFB
Summary(pl.UTF-8):	Sterownik graficzny SH7722/7723 dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libshbeu >= 1.0.2
Requires:	libshjpeg >= 1.3.3
Requires:	libuiomux >= 1.5.0

%description gfx-sh772x
SH7722/SH7723 graphics (SH-Mobile devices) driver for DirectFB.

%description gfx-sh772x -l pl.UTF-8
Sterownik graficzny SH7722/7723 (SH-Mobile) dla DirectFB.

%package input-dynapro
Summary:	Dynapro touchscreen input driver for DirectFB
Summary(pl.UTF-8):	Sterownik wejściowy do touchscreenów Dynapro dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-dynapro
Dynapro touchscreen input driver for DirectFB.

NOTE: currently it uses hardcoded /dev/ttyS0 port, so don't install it
unless you don't have Dynapro device connected to this port. It can
mess with other devices connected to this port (mouse, modem etc.).

%description input-dynapro -l pl.UTF-8
Sterownik wejściowy do touchscreenów Dynapro dla DirectFB.

UWAGA: aktualnie używa zakodowanego na stałe portu /dev/ttyS0, więc
nie należy go instalować, jeśli urządzenie Dynapro nie jest podłączone
do tego portu. Sterownik może utrudnić współpracę z innymi
urządzeniami podłączonymi do /dev/ttyS0 (jak mysz, modem itp.).

%package input-elo
Summary:	ELO touchscreen input driver for DirectFB
Summary(pl.UTF-8):	Sterownik wejściowy do touchscreenów ELO dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-elo
ELO touchscreen input driver for DirectFB.

NOTE: currently it uses hardcoded /dev/ttyS0 port, so don't install it
unless you have ELO device connected to this port. It can mess with
other devices connected to this port (mouse, modem etc.).

%description input-elo -l pl.UTF-8
Sterownik wejściowy do touchscreenów ELO dla DirectFB.

UWAGA: aktualnie używa zakodowanego na stałe portu /dev/ttyS0, więc
nie należy go instalować, jeśli urządzenie ELO nie jest podłączone do
tego portu. Sterownik może utrudnić współpracę z innymi urządzeniami
podłączonymi do /dev/ttyS0 (jak mysz, modem itp.).

%package input-gunze
Summary:	Gunze touchscreen input driver for DirectFB
Summary(pl.UTF-8):	Sterownik wejściowy do touchscreenów Gunze dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-gunze
Gunze touchscreen input driver for DirectFB.

NOTE: currently it uses hardcoded /dev/ttyS0 port, so don't install it
unless you don't have Gunze device connected to this port. It can mess
with other devices connected to this port (mouse, modem etc.).

%description input-gunze -l pl.UTF-8
Sterownik wejściowy do touchscreenów Gunze dla DirectFB.

UWAGA: aktualnie używa zakodowanego na stałe portu /dev/ttyS0, więc
nie należy go instalować, jeśli urządzenie Gunze nie jest podłączone
do tego portu. Sterownik może utrudnić współpracę z innymi
urządzeniami podłączonymi do /dev/ttyS0 (jak mysz, modem itp.).

%package input-mutouch
Summary:	MuTouch touchscreen input driver for DirectFB
Summary(pl.UTF-8):	Sterownik wejściowy do touchscreenów MuTouch dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-mutouch
MuTouch touchscreen input driver for DirectFB.

NOTE: it needs "mut-device" setting in directfbrc in order to work.

%description input-mutouch -l pl.UTF-8
Sterownik wejściowy do touchscreenów MuTouch dla DirectFB.

UWAGA: do działania potrzebuje ustawienia "mut-device" w directfbrc.

%package input-tslib
Summary:	tslib-based touchscreen input driver for DirectFB
Summary(pl.UTF-8):	Oparty na tslib sterownik wejściowy do touchscreenów dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	tslib >= 1.0

%description input-tslib
tslib-based touchscreen input driver for DirectFB

%description input-tslib -l pl.UTF-8
Oparty na tslib sterownik wejściowy do touchscreenów dla DirectFB.

%package input-ucb1x00
Summary:	UCB1x00 touchscreen input driver for DirectFB
Summary(pl.UTF-8):	Sterownik wejściowy do touchscreenów UCB1x00 dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-ucb1x00
UCB1x00 touchscreen input driver for DirectFB.

%description input-ucb1x00 -l pl.UTF-8
Sterownik wejściowy do touchscreenów UCB1x00 dla DirectFB.

%package input-wm97xx
Summary:	WM97xx touchscreen input driver for DirectFB
Summary(pl.UTF-8):	Sterownik wejściowy do touchscreenów WM97xx dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description input-wm97xx
WM97xx touchscreen input driver for DirectFB.

%description input-wm97xx -l pl.UTF-8
Sterownik wejściowy do touchscreenów WM97xx dla DirectFB.

%package image-imlib2
Summary:	Imlib2 image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę Imlib2
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-imlib2
This package contains Imlib2 image provider for DirectFB.

%description image-imlib2 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę Imlib2.

%package image-jpeg
Summary:	JPEG image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę JPEG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-jpeg
This package contains JPEG image provider for DirectFB.

%description image-jpeg -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę JPEG.

%package image-jpeg2000
Summary:	JPEG2000 image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę JPEG2000
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-jpeg2000
This package contains JPEG2000 image provider for DirectFB (based on
jasper library).

%description image-jpeg2000 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB, opartą na bibliotece jasper,
dostarczającą grafikę JPEG2000.

%package image-png
Summary:	PNG image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę PNG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libpng >= 2:1.4.0

%description image-png
This package contains PNG image provider for DirectFB.

%description image-png -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę PNG.

%package image-svg
Summary:	SVG image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę SVG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libsvg-cairo >= 0.1.6

%description image-svg
This package contains SVG image provider for DirectFB, based on Cairo
library.

%description image-svg -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB, opartą na bibliotece Cairo,
dostarczającą grafikę SVG.

%package video-mng
Summary:	MNG video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca animacje MNG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-mng
This package contains MNG video provider for DirectFB.

%description video-mng -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB, dostarczającą animacje MNG.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# video drivers
%{__sed} -i -e 's/checkfor_\(cle266\|cyber5k\|radeon\|savage\|unichrome\|vmware\)=no/checkfor_\1=yes/' configure.in
# input drivers
%{__sed} -i -e 's/checkfor_\(dynapro\|elo\|gunze\)=no/checkfor_\1=yes/' configure.in

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# MMX and SSE are detected at runtime, so it's safe to enable
%configure \
	%{!?debug:--disable-debug} \
	--disable-maintainer-mode \
	--disable-silent-rules \
	--enable-fast-install \
	%{?with_multi:--enable-multi} \
	%{?with_one:--enable-one} \
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
	--enable-sse \
%endif
%endif
	--with-smooth-scaling \
	%{!?with_static_libs:--disable-static}

%{__make} -j1 \
	X11_CFLAGS= \
	X11_LIBS="-lX11 -lXext"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}}

%{__make} -j1 install \
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
%attr(755,root,root) %{_bindir}/dfbfx
%attr(755,root,root) %{_bindir}/dfbg
%attr(755,root,root) %{_bindir}/dfbinfo
%attr(755,root,root) %{_bindir}/dfbinput
%attr(755,root,root) %{_bindir}/dfbinspector
%attr(755,root,root) %{_bindir}/dfblayer
%attr(755,root,root) %{_bindir}/dfbmaster
%attr(755,root,root) %{_bindir}/dfbpenmount
%attr(755,root,root) %{_bindir}/dfbproxy
%attr(755,root,root) %{_bindir}/dfbscreen
%attr(755,root,root) %{_bindir}/mkdfiff
%attr(755,root,root) %{_bindir}/mkdgiff
%attr(755,root,root) %{_bindir}/mkdgifft
%attr(755,root,root) %{_bindir}/pxa3xx_dump
%attr(755,root,root) %{_bindir}/uwmdump
%attr(755,root,root) %{_bindir}/voodooplay
%attr(755,root,root) %{_bindir}/voodooplay_client
%attr(755,root,root) %{_bindir}/voodooplay_server
%attr(755,root,root) %{_libdir}/libdirect-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdirect-1.6.so.0
%attr(755,root,root) %{_libdir}/libdirectfb-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdirectfb-1.6.so.0
%attr(755,root,root) %{_libdir}/libfusion-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfusion-1.6.so.0
%if %{with one}
%attr(755,root,root) %{_libdir}/libone-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libone-1.6.so.0
%endif
%attr(755,root,root) %{_libdir}/libuniquewm-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuniquewm-1.6.so.0
%attr(755,root,root) %{_libdir}/libvoodoo-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvoodoo-1.6.so.0
%dir %{dfbdir}
%dir %{dfbdir}/gfxdrivers
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_ati128.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_cle266.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_cyber5k.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_ep9x.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_gl.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_i810.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_i830.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_mach64.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_matrox.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_neomagic.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_nsc.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_nvidia.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_pxa3xx.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_radeon.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_savage.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_sdlgraphics.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_sis315.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_tdfx.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_unichrome.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_vmware.so
%ifarch arm
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_davinci.so
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_omap.so
%endif
%dir %{dfbdir}/inputdrivers
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_input_hub.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_joystick.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_keyboard.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_linux_input.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_lirc.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_penmount.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_ps2mouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_serialmouse.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sonypi.so
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_zytronic.so
%dir %{dfbdir}/interfaces
%dir %{dfbdir}/interfaces/ICoreResourceManager
%attr(755,root,root) %{dfbdir}/interfaces/ICoreResourceManager/libicoreresourcemanager_test.so
%dir %{dfbdir}/interfaces/IDirectFB
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFB/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBDataBuffer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBDataBuffer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBDisplayLayer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBDisplayLayer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBEventBuffer
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBEventBuffer/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBFont
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_dgiff.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_requestor.so
%dir %{dfbdir}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_bmp.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_dfiff.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_gif.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_mpeg2.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_pnm.so
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
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_gif.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_v4l.so
%dir %{dfbdir}/interfaces/IDirectFBWindow
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBWindow/lib*.so
%dir %{dfbdir}/interfaces/IDirectFBWindows
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBWindows/lib*.so
%dir %{dfbdir}/interfaces/IWater
%attr(755,root,root) %{dfbdir}/interfaces/IWater/lib*.so
%dir %{dfbdir}/systems
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_devmem.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_dummy.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_fbdev.so
%dir %{dfbdir}/wm
%attr(755,root,root) %{dfbdir}/wm/lib*.so
%{_datadir}/directfb-%{version}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/directfbrc
%{_mandir}/man1/dfbg.1*
%{_mandir}/man5/directfbrc.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/directfb-config
%attr(755,root,root) %{_bindir}/directfb-csource
%attr(755,root,root) %{_libdir}/libdirect.so
%attr(755,root,root) %{_libdir}/libdirectfb.so
%attr(755,root,root) %{_libdir}/libfusion.so
%{?with_one:%attr(755,root,root) %{_libdir}/libone.so}
%attr(755,root,root) %{_libdir}/libuniquewm.so
%attr(755,root,root) %{_libdir}/libvoodoo.so
%{_libdir}/libdirect.la
%{_libdir}/libdirectfb.la
%{_libdir}/libfusion.la
%{?with_one:%{_libdir}/libone.la}
%{_libdir}/libuniquewm.la
%{_libdir}/libvoodoo.la
%{_includedir}/directfb
%{_includedir}/directfb-internal
%{_pkgconfigdir}/direct.pc
%{_pkgconfigdir}/directfb-internal.pc
%{_pkgconfigdir}/directfb.pc
%{_pkgconfigdir}/fusion.pc
%{?with_one:%{_pkgconfigdir}/one.pc}
%{_pkgconfigdir}/voodoo.pc
%{_mandir}/man1/directfb-csource.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdirect.a
%{_libdir}/libdirectfb.a
%{_libdir}/libfusion.a
%{?with_one:%{_libdir}/libone.a}
%{_libdir}/libuniquewm.a
%{_libdir}/libvoodoo.a
%{dfbdir}/gfxdrivers/*.[alo]*
%{dfbdir}/inputdrivers/*.[alo]*
%{dfbdir}/interfaces/*/*.[alo]*
%{dfbdir}/systems/*.[alo]*
%{dfbdir}/wm/*.[alo]*
%endif

%files doc
%defattr(644,root,root,755)
%doc docs/html/*.{html,png}
%{_examplesdir}/%{name}-%{version}

%files core-mesa
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_gles2.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_mesa_system.so

%files core-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_sdlinput.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_sdl.so

%files core-vdpau
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_vdpau.so
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_x11vdpau.so

%files core-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_vnc.so

%files core-x11
%defattr(644,root,root,755)
%doc systems/x11/README
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_x11.so

%files font-ft2
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_ft2.so

%if %{with sh772x}
%files gfx-sh772x
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/gfxdrivers/libdirectfb_sh772x.so
%endif

%files input-dynapro
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_dynapro.so

%files input-elo
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_elo.so

%files input-gunze
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_gunze.so

%files input-mutouch
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_mutouch.so

%files input-tslib
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_tslib.so

%ifarch arm
%files input-ucb1x00
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_ucb1x00_ts.so
%endif

%files input-wm97xx
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_wm97xx_ts.so

%files image-imlib2
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_imlib2.so

%files image-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg.so

%files image-jpeg2000
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_jpeg2000.so

%files image-png
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_png.so

%files image-svg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_svg.so

%files video-mng
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_mng.so
