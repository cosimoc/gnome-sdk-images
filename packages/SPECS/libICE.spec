Summary: X.Org X11 ICE runtime library
Name: libICE
Version: 1.0.9
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: gnome-sdk-base
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: xorg-x11-xtrans-devel

%description
The X.Org X11 ICE (Inter-Client Exchange) runtime library.

%package devel
Summary: X.Org X11 ICE development package
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The X.Org X11 ICE (Inter-Client Exchange) development package.

%prep
%setup -q

%build
autoreconf -v --install --force
%configure --disable-static
V=1 make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# adding to installed docs in order to avoid using %%doc magic
for f in AUTHORS ChangeLog COPYING ; do
    cp -p $f ${RPM_BUILD_ROOT}%{_docdir}/%{name}/${f}
done

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libICE.so.6
%{_libdir}/libICE.so.6.3.0
# not using %%doc because of side-effect (#1001256)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING

%files devel
%{_docdir}/%{name}/*.xml
%{_includedir}/X11/ICE
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc

%changelog
* Tue Nov 11 2014 Alexander Larsson <alexl@redhat.com> - 1.0.9-1
- Initial version based on f21
