# TODO: --enable-pvr2d when ready [requires PowerVR SDK?]
# - enable xine_vdpau (needs <xine/video_out_vdpau.h>)
#
# Conditional build:
%bcond_with	multi		# build Multi-application core (requires working /dev/fusion*)
%bcond_without	one		# Linux One IPC library
%bcond_without	static_libs	# don't build static libraries
%bcond_with	sh772x		# SH7722/SH7723 (SH-Mobile) graphics driver
%bcond_with	avifile		# AviFile video provider [not updated for DirectFB 1.7.0]
%bcond_without	ffmpeg		# FFmpeg music and video providers
%bcond_with	flash		# FLASH video provider [not updated for DirectFB 1.7.0]
%bcond_without	gstreamer	# GStreamer video provider
%bcond_without	mpg		# libmpeg3 MPEG video provider
%bcond_without	quicktime	# QuickTime (openquicktime) video provider
%bcond_with	swfdec		# swfdec FLASH video provider [not ready for swfdec >= 0.6]
%bcond_without	xine		# Xine video provider
%bcond_with	xine_vdpau	# Xine/VDPAU video provider
#
%ifarch sh4
%define		with_sh772x	1
%endif
%if %{without xine}
%undefine	xine_vdpau
%endif
Summary:	DirectFB - Hardware graphics acceleration
Summary(pl.UTF-8):	DirectFB - Wspomaganie grafiki
Name:		DirectFB
Version:	1.7.0
Release:	2
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Core/DirectFB-1.7/%{name}-%{version}.tar.gz
# Source0-md5:	258d3a5fda5d9af16c5cbdca671638e5
Source1:	http://www.directfb.org/downloads/Extras/DFBTutorials-0.5.0.tar.gz
# Source1-md5:	13e443a64bddd68835b574045d9025e9
Patch0:		%{name}-am.patch
Patch1:		%{name}-pmake.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-llh-ppc.patch
Patch4:		%{name}-zlib.patch
Patch5:		%{name}-update.patch
Patch6:		%{name}-gstreamer.patch
Patch7:		%{name}-sh.patch
Patch8:		%{name}-missing.patch
Patch9:		%{name}-ffmpeg.patch
Patch10:	%{name}-libmpeg3.patch
Patch11:	%{name}-format.patch
URL:		http://www.directfb.org/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libGLES-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_avifile:BuildRequires:	avifile-devel}
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	freetype-devel >= 2.0.2
%{?with_flash:BuildRequires:	gplflash-devel >= 0.4.10-5}
%{?with_gstreamer:BuildRequires:	gstreamer-plugins-base-devel >= 1.0}
BuildRequires:	imlib2-devel
BuildRequires:	jasper-devel
BuildRequires:	libcddb-devel >= 1.0.0
BuildRequires:	libdrm-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libmad-devel
BuildRequires:	libmng-devel
%{?with_mpg:BuildRequires:	libmpeg3-devel}
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtimidity-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	libvdpau-devel >= 0.3
BuildRequires:	libvncserver-devel
BuildRequires:	libvorbis-devel >= 1:1.0.0
BuildRequires:	libwebp-devel >= 0.2.1
%{?with_multi:BuildRequires:	linux-fusion-devel >= 9.0.1}
%{?with_one:BuildRequires:	linux-one-devel >= 9.0.1}
%{?with_quicktime:BuildRequires:	openquicktime-devel}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
%{?with_swfdec:BuildRequires:	swfdec-devel >= 0.5.0}
%{?with_swfdec:BuildRequires:	swfdec-devel < 0.6.0}
BuildRequires:	sysfsutils-devel >= 1.3.0-3
BuildRequires:	tslib-devel >= 1.0
%{?with_xine:BuildRequires:	xine-lib-devel >= 2:1.2.0}
%{?with_xine_vdpau:BuildRequires:	/usr/include/xine/video_out_vdpau.h}
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
Obsoletes:	DirectFB-image-bmp
Obsoletes:	DirectFB-image-mpeg2
Obsoletes:	DirectFB-image-pnm
%ifnarch arm
# ARM-specific
Obsoletes:	DirectFB-input-ucb1x00
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dfbdir	%{_libdir}/directfb-1.7-0

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
%{?with_one:Requires:	linux-one-devel >= 1.7.0}
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

%package core-drmkms
Summary:	DRM/KMS core system for DirectFB
Summary(pl.UTF-8):	System DRM/KMS dla DirectFB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description core-drmkms
This package contains DRM/KMS core system module for DirectFB.

%description core-drmkms -l pl.UTF-8
Ten pakiet zawiera moduł systemu DRM/KMS dla DirectFB.

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

%package image-tiff
Summary:	TIFF image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę TIFF
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libtiff >= 4

%description image-tiff
This package contains TIFF image provider for DirectFB.

%description image-tiff -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę TIFF.

%package image-webp
Summary:	WebP image provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca grafikę WebP
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libwebp >= 0.2.1

%description image-webp
This package contains WebP image provider for DirectFB.

%description image-webp -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą grafikę WebP.

%package video-avifile
Summary:	Avifile video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz Avifile 
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-avifile
DirectFB video provider using Avifile codecs.

%description video-avifile -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczajacą obraz przy
użyciu kodeków Avifile.

%package video-ffmpeg
Summary:	FFmpeg video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz FFmpeg
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-ffmpeg
DirectFB video provider using FFmpeg codecs.

%description video-ffmpeg -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczajacą obraz przy
użyciu kodeków FFmpeg.

%package video-gstreamer
Summary:	GStreamer video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz z GStreamera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-gstreamer
This package contains GStreamer video provider for DirectFB.

%description video-gstreamer -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB, dostarczającą obraz z
GStreamera.

%package video-libmpeg3
Summary:	MPEG video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz MPEG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-libmpeg3
This package contains MPEG (MPEG-1 and MPEG-2) video provider for
DirectFB. It uses libmpeg3 library.

%description video-libmpeg3 -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczajacą obraz MPEG
(MPEG-1 i MPEG-2) przy użyciu biblioteki libmpeg3.

%package video-mng
Summary:	MNG video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca animacje MNG
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-mng
This package contains MNG video provider for DirectFB.

%description video-mng -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB, dostarczającą animacje MNG.

%package video-openquicktime
Summary:	OpenQuicktime video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz OpenQuicktime
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-openquicktime
This package contains OpenQuicktime video provider for DirectFB. It
supports all RGB and YUV formats and does audio playback.

%description video-openquicktime -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz
OpenQuicktime. Obsługuje wszystkie formaty RGB i YUV oraz odtwarza
dźwięk.

%package video-swf
Summary:	ShockWave Flash video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz ShockWave Flash
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-swf
This package contains SWF (ShockWave Flash) video provider for
DirectFB. It uses flash library.

%description video-swf -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz SWF
(ShockWave Flash) przy użyciu biblioteki flash.

%package video-swfdec
Summary:	ShockWave Flash video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz ShockWave Flash
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-swfdec
This package contains SWF (ShockWave Flash) video provider for
DirectFB. It uses swfdec library.

%description video-swfdec -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz SWF
(ShockWave Flash) przy użyciu biblioteki swfdec.

%package video-xine
Summary:	XINE video provider for DirectFB
Summary(pl.UTF-8):	DirectFB - wtyczka dostarczająca obraz XINE
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%requires_eq	xine-lib

%description video-xine
This package contains video provider for DirectFB which uses XINE
library and plugins. It handles a wide range of video formats.

%description video-xine -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla DirectFB dostarczającą obraz przy
użyciu biblioteki i wtyczek XINE. Obsługuje szeroki zakres formatów
obrazu.

%package -n xine-output-video-dfb
Summary:	DirectFB video output plugin for XINE
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu DirectFB dla XINE
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%requires_eq	xine-lib

%description -n xine-output-video-dfb
DirectFB video output plugin for XINE.

%description -n xine-output-video-dfb -l pl.UTF-8
Wtyczka wyjścia obrazu DirectFB dla XINE.

%package c++
Summary:	++DFB - advanced C++ binding for DirectFB
Summary(pl.UTF-8):	++DFB - zaawansowane wiązania C++ do DirectFB
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Projects%2F%2B%2BDFB
Requires:	%{name} = %{epoch}:%{version}-%{release}
# (probably) can't Obsolete ++DFB
Obsoletes:	__DFB

%description c++
++DFB - advanced C++ binding for DirectFB.

%description c++ -l pl.UTF-8
++DFB - zaawansowane wiązania C++ do DirectFB.

%package c++-devel
Summary:	Header files for ++DFB
Summary(pl.UTF-8):	Pliki nagłówkowe ++DFB
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Projects%2F%2B%2BDFB
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel
Obsoletes:	__DFB-devel

%description c++-devel
Header files for ++DFB.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe ++DFB.

%package c++-static
Summary:	Static ++DFB library
Summary(pl.UTF-8):	Statyczna biblioteka ++DFB
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Projects%2F%2B%2BDFB
Requires:	%{name}-c++-devel = %{epoch}:%{version}-%{release}
Obsoletes:	__DFB-static

%description c++-static
Static ++DFB library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka ++DFB.

%package -n DiVine
Summary:	DirectFB Virtual Input extension
Summary(pl.UTF-8):	Rozszerzenie DirectFB o wirtualne wejście
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n DiVine
DiVine consists of:
- an input driver that reads raw input events from a pipe and
  dispatches them via a virtual input device.
- a library that handles the connection to the input driver including
  helper functions for generating events.
- a tool called "spooky" to generate input events using a simple
  script featuring button or motion events, linear or circular
  automated motion and delays.

%description -n DiVine -l pl.UTF-8
DiVine składa się z:
- sterownika wejścia czytającego surowe zdarzenia wejściowe z potoku
  i przekazującego je poprzez wirtualne urządzenie wejściowe,
- biblioteki obsługującej połączenie ze sterownikiem wejściowym oraz
  zawierającej funkcje pomocnicze do generowania zdarzeń,
- narzędzia "spooky" generującego zdarzenia wejściowe przy użyciu
  prostego skryptu oferującego zdarzenia związane z przyciskami i
  ruchem, automatycznym ruchem liniowym lub cyklicznym i opóźnieniami.

%package -n DiVine-devel
Summary:	Header files for divine library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki divine
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	DiVine = %{epoch}:%{version}-%{release}

%description -n DiVine-devel
Header files for divine library.

%description -n DiVine-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki divine.

%package -n DiVine-static
Summary:	Static divine library
Summary(pl.UTF-8):	Statyczna biblioteka divine
Group:		Development/Libraries
Requires:	DiVine-devel = %{epoch}:%{version}-%{release}

%description -n DiVine-static
Static divine library.

%description -n DiVine-static -l pl.UTF-8
Statyczna biblioteka divine.

%package -n FusionDale
Summary:	FusionDale - applied Fusion, collection of services for applications
Summary(pl.UTF-8):	FusionDale, czyli Fusion stosowany - zbiór usług dla aplikacji
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionDale
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n FusionDale
FusionDale is applied Fusion and will be a collection of different
services for use by applications and other libraries (like Coma
component manager or messaging API).

%description -n FusionDale -l pl.UTF-8
FusionDale to Fusion stosowany, biblioteka mająca być zbiorem różnych
usług przeznaczonych do wykorzystywania przez aplikacje i inne
biblioteki (takich jak zarządca komponentów Coma czy API do
komunikacji).

%package -n FusionDale-devel
Summary:	Header files for the FusionDale
Summary(pl.UTF-8):	Pliki nagłówkowe dla FusionDale
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionDale
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	FusionDale = %{epoch}:%{version}-%{release}

%description -n FusionDale-devel
Header files required for development using FusionDale.

%description -n FusionDale-devel -l pl.UTF-8
Pliki nagłówkowe wymagane do tworzenia programów z użyciem
FusionDale.

%package -n FusionDale-static
Summary:	Static FusionDale library
Summary(pl.UTF-8):	Statyczna biblioteka FusionDale
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionDale
Requires:	FusionDale-devel = %{epoch}:%{version}-%{release}

%description -n FusionDale-static
Static FusionDale library.

%description -n FusionDale-static -l pl.UTF-8
Statyczna biblioteka FusionDale.

%package -n FusionSound
Summary:	Audio sub system for multiple applications
Summary(pl.UTF-8):	Dźwiękowy podsystem dla złożonych aplikacji
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n FusionSound
FusionSound supports multiple applications using Fusion IPC. It
provides streams, static sound buffers and control over any number of
concurrent playbacks. Sample data is always stored in shared memory,
starting a playback simply adds an entry to the playlist of the mixer
thread in the master application.

%description -n FusionSound -l pl.UTF-8
FusionSound wspiera złożone aplikacje używające Fusion IPC. Dostarcza
strumieni, statyczny bufor dźwiękowy i kontrolę poprzez każdą ilość
konkurencyjnych odtwarzaczy. Próbkowana dana jest zawsze przechowywana
w pamięci dzielonej. Rozpoczynając odtwarzanie dodaje wejście do listy
odtwarzania miksera w nadrzędnej aplikacji.

%package -n FusionSound-devel
Summary:	Development files for the FusionSound
Summary(pl.UTF-8):	Pliki rozwojowe dla FusionSound
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	FusionSound = %{epoch}:%{version}-%{release}

%description -n FusionSound-devel
Header files required for development using FusionSound.

%description -n FusionSound-devel -l pl.UTF-8
Pliki nagłówkowe wymagane do tworzenia programów z użyciem
FusionSound.

%package -n FusionSound-static
Summary:	Static FusionSound library
Summary(pl.UTF-8):	Statyczna biblioteka FusionSound
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	FusionSound-devel = %{epoch}:%{version}-%{release}

%description -n FusionSound-static
Static FusionSound library.

%description -n FusionSound-static -l pl.UTF-8
Statyczna biblioteka FusionSound.

%package -n FusionSound-musicprovider-cdda
Summary:	CD-DA music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę CD-DA
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	FusionSound = %{epoch}:%{version}-%{release}

%description -n FusionSound-musicprovider-cdda
CD-DA music provider module for FusionSound.

%description -n FusionSound-musicprovider-cdda -l pl.UTF-8
Moduł FusionSound dostarczający muzykę CD-DA.

%package -n FusionSound-musicprovider-ffmpeg
Summary:	ffmpeg music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę przez ffmpeg
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	FusionSound = %{epoch}:%{version}-%{release}

%description -n FusionSound-musicprovider-ffmpeg
ffmpeg music provider module for FusionSound.

%description -n FusionSound-musicprovider-ffmpeg -l pl.UTF-8
Moduł FusionSound dostarczający muzykę przez ffmpeg.

%package -n FusionSound-musicprovider-mad
Summary:	MP3 libmad music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę MP3 przez libmad
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	FusionSound = %{epoch}:%{version}-%{release}

%description -n FusionSound-musicprovider-mad
MP3 music provider module for FusionSound.

%description -n FusionSound-musicprovider-mad -l pl.UTF-8
Moduł FusionSound dostarczający muzykę MP3 przez libmad.

%package -n FusionSound-musicprovider-timidity
Summary:	MIDI libtimidity music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę MIDI przez libtimidity
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	FusionSound = %{epoch}:%{version}-%{release}

%description -n FusionSound-musicprovider-timidity
MIDI libtimidity music provider module for FusionSound.

%description -n FusionSound-musicprovider-timidity -l pl.UTF-8
Moduł FusionSound dostarczający muzykę MIDI przez libtimidity.

%package -n FusionSound-musicprovider-vorbis
Summary:	Ogg Vorbis music provider module for FusionSound
Summary(pl.UTF-8):	Moduł FusionSound dostarczający muzykę Ogg Vorbis
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/FusionSound
Requires:	FusionSound = %{epoch}:%{version}-%{release}

%description -n FusionSound-musicprovider-vorbis
Ogg Vorbis music provider module for FusionSound.

%description -n FusionSound-musicprovider-vorbis -l pl.UTF-8
Moduł FusionSound dostarczający muzykę Ogg Vorbis.

%package -n SaWMan
Summary:	Shared application and Window Manager
Summary(pl.UTF-8):	Zarządca współdzielonych aplikacji i okien
Group:		Libraries
URL:		http://www.directfb.org/index.php?path=Platform/SaWMan
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n SaWMan
SaWMan is a new window manager module for use with DirectFB. Its main
difference to the default module is that it allows one process to be
an application and window manager, implementing all kinds of
diversity, while SaWMan is only the working horse.

%description -n SaWMan -l pl.UTF-8
SaWMan to nowy moduł zarządcy okien dla DirectFB. Główną różnicą w
stosunku do domyślnego modułu jest to, że pozwala jednemu procesowi
być aplikacją i zarządcą okien, implementując wszystkie urozmaicenia,
podczas gdy SaWMan jest tylko silnikiem.

%package -n SaWMan-devel
Summary:	Header files for sawman library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sawman
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Platform/SaWMan
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	SaWMan = %{epoch}:%{version}-%{release}

%description -n SaWMan-devel
Header files for sawman library.

%description -n SaWMan-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sawman.

%package -n SaWMan-static
Summary:	Static sawman library
Summary(pl.UTF-8):	Statyczna biblioteka sawman
Group:		Development/Libraries
URL:		http://www.directfb.org/index.php?path=Platform/SaWMan
Requires:	SaWMan-devel = %{epoch}:%{version}-%{release}

%description -n SaWMan-static
Static sawman library.

%description -n SaWMan-static -l pl.UTF-8
Statyczna biblioteka sawman.

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
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

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
%{?with_mpg:CPPFLAGS="%{rpmcppflags} -I/usr/include/libmpeg3"}
# MMX and SSE are detected at runtime, so it's safe to enable
%configure \
	%{!?debug:--disable-debug} \
	--disable-maintainer-mode \
	--disable-silent-rules \
	%{?with_avifile:--enable-avifile} \
	--enable-divine \
	--enable-fast-install \
	%{?with_ffmpeg:--enable-ffmpeg} \
	%{?with_flash:--enable-flash} \
	--enable-fusiondale \
	--enable-fusionsound \
	%{?with_gstreamer:--enable-gstreamer} \
	--enable-imlib2 \
	%{?with_mpg:--enable-libmpeg3} \
	--enable-mng \
	%{?with_multi:--enable-multi} \
	%{?with_one:--enable-one} \
	%{?with_quicktime:--enable-openquicktime} \
	--enable-sawman \
	--enable-sdl \
	--enable-shared \
	--enable-static \
	--enable-svg \
	%{?with_swfdec:--enable-swfdec} \
	--enable-unique \
	--enable-video4linux2 \
	--enable-voodoo \
	%{?with_xine:--enable-xine} \
	%{?with_xine_vdpau:--enable-xine-vdpau} \
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

%if %{with xine}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xine/plugins/*/*.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/xine/plugins/*/*.a}
%endif

touch $RPM_BUILD_ROOT%{_sysconfdir}/directfbrc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/dfbdump
%attr(755,root,root) %{_bindir}/dfbdumpinput
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
%attr(755,root,root) %{_libdir}/libdirect-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdirect-1.7.so.0
%attr(755,root,root) %{_libdir}/libdirectfb-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdirectfb-1.7.so.0
%attr(755,root,root) %{_libdir}/libfusion-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfusion-1.7.so.0
%if %{with one}
%attr(755,root,root) %{_libdir}/libone-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libone-1.7.so.0
%endif
%attr(755,root,root) %{_libdir}/libuniquewm-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuniquewm-1.7.so.0
%attr(755,root,root) %{_libdir}/libvoodoo-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvoodoo-1.7.so.0
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
%attr(755,root,root) %{dfbdir}/wm/libdirectfbwm_default.so
%attr(755,root,root) %{dfbdir}/wm/libdirectfbwm_unique.so
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
%{_includedir}/One
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
%{dfbdir}/wm/libdirectfbwm_default.[alo]*
%{dfbdir}/wm/libdirectfbwm_unique.[alo]*
%endif

%files doc
%defattr(644,root,root,755)
%doc docs/html/*.{html,png}
%{_examplesdir}/%{name}-%{version}

%files core-drmkms
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/systems/libdirectfb_drmkms_system.so

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
   
%files image-tiff
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_tiff.so

%files image-webp
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBImageProvider/libidirectfbimageprovider_webp.so

%if %{with avifile}
%files video-avifile
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_avifile.so
%endif

%if %{with ffmpeg}
%files video-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_ffmpeg.so
%endif

%if %{with gstreamer}
%files video-gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_gstreamer.so
%endif

%if %{with mpg}
%files video-libmpeg3
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_libmpeg3.so
%endif

%files video-mng
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_mng.so

%if %{with quicktime}
%files video-openquicktime
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_openquicktime.so
%endif

%if %{with flash}
%files video-swf
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swf.so
%endif

%if %{with swfdec}
%files video-swfdec
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_swfdec.so
%endif

%if %{with xine}
%files video-xine
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_xine.so
%if %{with xine_vdpau}
%attr(755,root,root) %{dfbdir}/interfaces/IDirectFBVideoProvider/libidirectfbvideoprovider_xine_vdpau.so
%endif

%files -n xine-output-video-dfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xine/plugins/2.*/xineplug_vo_out_dfb.so
%endif

%files c++
%defattr(644,root,root,755)
# ++DFB based utilities
%attr(755,root,root) %{_bindir}/dfbplay
%attr(755,root,root) %{_bindir}/dfbshow
%attr(755,root,root) %{_bindir}/dfbswitch
# library itself
%attr(755,root,root) %{_libdir}/lib++dfb-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib++dfb-1.7.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib++dfb.so
%{_libdir}/lib++dfb.la
%{_includedir}/++dfb
%{_pkgconfigdir}/++dfb.pc

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/lib++dfb.a

%files -n DiVine
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spooky
%attr(755,root,root) %{_libdir}/libdivine-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdivine-1.7.so.0
%attr(755,root,root) %{dfbdir}/inputdrivers/libdirectfb_divine.so
%dir %{dfbdir}/interfaces/IDiVine
%attr(755,root,root) %{dfbdir}/interfaces/IDiVine/libidivine_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IDiVine/libidivine_requestor.so

%files -n DiVine-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdivine.so
%{_libdir}/libdivine.la
%{_includedir}/divine
%{_pkgconfigdir}/divine.pc

%files -n DiVine-static
%defattr(644,root,root,755)
%{_libdir}/libdivine.a

%files -n FusionDale
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fddump
%attr(755,root,root) %{_bindir}/fdmaster
%attr(755,root,root) %{_libdir}/libfusiondale-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfusiondale-1.7.so.0
%dir %{dfbdir}/interfaces/IComa
%attr(755,root,root) %{dfbdir}/interfaces/IComa/libicoma_*.so
%dir %{dfbdir}/interfaces/IComaComponent
%attr(755,root,root) %{dfbdir}/interfaces/IComaComponent/libicomacomponent_*.so
%dir %{dfbdir}/interfaces/IFusionDale
%attr(755,root,root) %{dfbdir}/interfaces/IFusionDale/libifusiondale_*.so
%dir %{dfbdir}/interfaces/IFusionDaleMessenger
%attr(755,root,root) %{dfbdir}/interfaces/IFusionDaleMessenger/libifusiondalemessenger_one.so

%files -n FusionDale-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfusiondale.so
%{_libdir}/libfusiondale.la
%{_includedir}/fusiondale
%{_pkgconfigdir}/fusiondale.pc

%files -n FusionDale-static
%defattr(644,root,root,755)
%{_libdir}/libfusiondale.a

%files -n FusionSound
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fsdump
%attr(755,root,root) %{_bindir}/fsmaster
%attr(755,root,root) %{_bindir}/fsplay
%attr(755,root,root) %{_bindir}/fsproxy
%attr(755,root,root) %{_bindir}/fsvolume
%attr(755,root,root) %{_libdir}/libfusionsound-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfusionsound-1.7.so.0
%dir %{dfbdir}/interfaces/IFusionSound
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSound/libifusionsound.so
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSound/libifusionsound_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSound/libifusionsound_requestor.so
%dir %{dfbdir}/interfaces/IFusionSoundBuffer
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundBuffer/libifusionsoundbuffer_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundBuffer/libifusionsoundbuffer_requestor.so
%dir %{dfbdir}/interfaces/IFusionSoundMusicProvider
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_playlist.so
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_wave.so
%dir %{dfbdir}/interfaces/IFusionSoundPlayback
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundPlayback/libifusionsoundplayback_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundPlayback/libifusionsoundplayback_requestor.so
%dir %{dfbdir}/interfaces/IFusionSoundStream
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundStream/libifusionsoundstream_dispatcher.so
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundStream/libifusionsoundstream_requestor.so
%dir %{dfbdir}/snddrivers
%attr(755,root,root) %{dfbdir}/snddrivers/libfusionsound_alsa.so
%attr(755,root,root) %{dfbdir}/snddrivers/libfusionsound_dummy.so
%attr(755,root,root) %{dfbdir}/snddrivers/libfusionsound_oss.so
%attr(755,root,root) %{dfbdir}/snddrivers/libfusionsound_wave.so

%files -n FusionSound-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfusionsound.so
%{_libdir}/libfusionsound.la
%{_includedir}/fusionsound
%{_includedir}/fusionsound-internal
%{_pkgconfigdir}/fusionsound.pc
%{_pkgconfigdir}/fusionsound-internal.pc

%files -n FusionSound-static
%defattr(644,root,root,755)
%{_libdir}/libfusionsound.a
# .la makes no sense in -devel (it's module); here for DFB static linking hacks
%{dfbdir}/snddrivers/libfusionsound_*.[la]*

%files -n FusionSound-musicprovider-cdda
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_cdda.so

%if %{with ffmpeg}
%files -n FusionSound-musicprovider-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_ffmpeg.so
%endif

%files -n FusionSound-musicprovider-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_mad.so

%files -n FusionSound-musicprovider-timidity
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_timidity.so

%files -n FusionSound-musicprovider-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{dfbdir}/interfaces/IFusionSoundMusicProvider/libifusionsoundmusicprovider_vorbis.so

%files -n SaWMan
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/swmdump
%attr(755,root,root) %{_libdir}/libsawman-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsawman-1.7.so.0
%attr(755,root,root) %{dfbdir}/wm/libdirectfbwm_sawman.so

%files -n SaWMan-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsawman.so
%{_libdir}/libsawman.la
%{_includedir}/sawman
%{_pkgconfigdir}/sawman.pc

%files -n SaWMan-static
%defattr(644,root,root,755)
%{_libdir}/libsawman.a
%{dfbdir}/wm/libdirectfbwm_sawman.[alo]*
