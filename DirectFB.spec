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
Summary(pl.UTF-8):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	1.0.0
Release:	4
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Core/%{name}-%{version}.tar.gz
# Source0-md5:	ad746c49dc89ba6f99df71b17bbb1dc8
Source1:	http://www.directfb.org/downloads/Extras/DFBTutorials-0.5.0.tar.gz
# Source1-md5:	13e443a64bddd68835b574045d9025e9
Patch0:		%{name}-am.patch
Patch1:		%{name}-pmake.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-gcc4.patch
Patch4:		%{name}-llh-ppc.patch
Patch5:		%{name}-link.patch
URL:		http://www.directfb.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.2
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0
BuildRequires:	libtool
BuildRequires:	libvncserver-devel
%{?with_multi:BuildRequires:	linux-fusion-devel >= 3.0}
BuildRequires:	sed >= 4.0
BuildRequires:	sysfsutils-devel >= 1.3.0-3
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel >= 1.1.3
%{?with_multi:Provides:	DirectFB(multi)}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir	%{_libdir}/directfb-1.0-0

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

%package core-sdl
Summary:	SDL core system for DirectFB
Summary(pl.UTF-8):	System SDL dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-sdl
This package contains SDL core system module for DirectFB.

%description core-sdl -l pl.UTF-8
Ten pakiet zawiera moduł systemu SDL dla DirectFB.

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

%package image-jpeg
Summary:	JPEG image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę JPEG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-jpeg
This package contains JPEG image provider for DirectFB.

%description image-jpeg -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę JPEG.

%package image-png
Summary:	PNG image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę PNG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description image-png
This package contains PNG image provider for DirectFB.

%description image-png -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę PNG.

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
	--enable-fast-install \
	%{?with_multi:--enable-multi} \
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
	--with-inputdrivers=dynapro,elo-input,gunze,joystick,keyboard,linuxinput,lirc,mutouch,penmount,ps2mouse,serialmouse,sonypijogdial,ucb1x00,wm97xx

%{__make} \
	X11_CFLAGS= \
	X11_LIBS="-lX11 -lXext"

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
%attr(755,root,root) %{_bindir}/dfbinput
%attr(755,root,root) %{_bindir}/dfblayer
%attr(755,root,root) %{_bindir}/dfbpenmount
%attr(755,root,root) %{_bindir}/dfbproxy
%attr(755,root,root) %{_bindir}/dfbscreen
%attr(755,root,root) %{_bindir}/dfbsummon
%attr(755,root,root) %{_bindir}/mkdfiff
%attr(755,root,root) %{_bindir}/mkdgiff
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
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_penmount.so
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
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_dgiff.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBFont/libidirectfbfont_requestor.so
%dir %{dfbdir}/interfaces/IDirectFBImageProvider
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_dfiff.so
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
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_gif.so
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
%{dfbdir}/gfxdrivers/*.[alo]*
%{dfbdir}/inputdrivers/*.[alo]*
%{dfbdir}/interfaces/*/*.[alo]*
%{dfbdir}/systems/*.[alo]*
%{dfbdir}/wm/*.[alo]*

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

%files input-ucb1x00
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_ucb1x00_ts.so

%files input-wm97xx
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_wm97xx_ts.so
