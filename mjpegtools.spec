Summary:	Tools for recording, editing, playing back and MPEG-encoding video under Linux
Name:		mjpegtools
Version:	2.0.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	903e1e3b967eebcc5fe5626d7517dc46
Patch0:		%{name}-gcc.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-link.patch
URL:		http://mjpeg.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to MPEG) video under Linux. Recording can
be done with Zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into MPEG 1/2 or DivX video.

%package libs
Summary:	MJPEG-tools shared libraries
Group:		Libraries

%description libs
MJPEG-tools shared libraries.

%package devel
Summary:	Development headers for the mjpegtools
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains C system header files needed to compile
applications that use part of the libraries of the mjpegtools package.

%package glav
Summary:	GUI for the mjpegtools
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description glav
GUI for the mjpegtools.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f aclocal.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PTHREAD_LIBS="-lpthread" \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lav*
%attr(755,root,root) %{_bindir}/yuv*
%attr(755,root,root) %{_bindir}/jpeg2yuv
%attr(755,root,root) %{_bindir}/y4m*
%attr(755,root,root) %{_bindir}/pgm*
%attr(755,root,root) %{_bindir}/png2yuv
%attr(755,root,root) %{_bindir}/ppm*
%attr(755,root,root) %{_bindir}/ypipe
%attr(755,root,root) %{_bindir}/mp*
%attr(755,root,root) %{_bindir}/*.flt
%attr(755,root,root) %{_bindir}/anytovcd.sh
%attr(755,root,root) %{_bindir}/mjpeg_simd_helper
%attr(755,root,root) %{_bindir}/pnmtoy4m
%attr(755,root,root) %{_bindir}/yuyvtoy4m
%{_mandir}/man1/*
%{_infodir}/mjpeg-howto*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES HINTS PLANS README TODO
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/mjpegtools
%{_pkgconfigdir}/*.pc

%files glav
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glav

