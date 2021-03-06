Summary:  Thai language support routines
Name: libthai
Version: 0.1.21
Release: 1%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
Source: ftp://linux.thai.net/pub/thailinux/software/libthai/libthai-%{version}.tar.xz
URL: http://linux.thai.net

BuildRequires: gnome-sdk-base
BuildRequires: libdatrie-devel

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package devel
Summary:  Thai language support routines
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The libthai-devel package includes the header files and developer docs 
for the libthai package.

Install libthai-devel if you want to develop programs which will use
libthai.

%prep
%setup -q

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/lib*.so.*
%{_datadir}/libthai

%files devel
%defattr(-, root, root)
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Wed Nov 12 2014 Alexander Larsson <alexl@redhat.com> - 0.1.21-1
- Initial version based on F21
