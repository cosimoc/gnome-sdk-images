Name:           libxshmfence
Version:        1.1
Release:        1%{?dist}
Summary:        X11 shared memory fences

License:        MIT
URL:            http://www.x.org/
Source0:        http://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: gnome-sdk-base
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel

%description
Shared memory fences for X11, as used in DRI3.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -v -i -f
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc
%{_libdir}/libxshmfence.so.1*

%files devel
%doc
%{_includedir}/*
%{_libdir}/pkgconfig/xshmfence.pc
%{_libdir}/*.so

%changelog
* Tue Nov 11 2014 Alexander Larsson <alexl@redhat.com> - 1.1-1
- Initial version based on f21
