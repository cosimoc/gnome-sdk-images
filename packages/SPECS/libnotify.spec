%global release_version %%(echo %{version} | awk -F. '{print $1"."$2}')

Summary: Desktop notification library
Name: libnotify
Version: 0.7.6
Release: 1%{?dist}
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/libnotify/%{release_version}/%{name}-%{version}.tar.xz
License: LGPLv2+
Group: System Environment/Libraries

BuildRequires: gnome-sdk-base
BuildRequires: glib2-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gtk3-devel
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: gobject-introspection-devel

Requires: glib2

%description
libnotify is a library for sending desktop notifications to a notification
daemon, as defined in the freedesktop.org Desktop Notifications spec. These
notifications can be used to inform the user about an event or display some
form of information without getting in the user's way.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel
Requires:       dbus-devel
Requires:       dbus-glib-devel

%description devel
This package contains libraries and header files needed for
development of programs using %{name}.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING NEWS AUTHORS

%{_bindir}/notify-send
%{_libdir}/libnotify.so.*
%{_libdir}/girepository-1.0/Notify-0.7.typelib

%files devel
%dir %{_includedir}/libnotify
%{_includedir}/libnotify/*
%{_libdir}/libnotify.so
%{_libdir}/pkgconfig/libnotify.pc
%dir %{_datadir}/gtk-doc/html/libnotify
%{_datadir}/gtk-doc/html/libnotify/*
%{_datadir}/gir-1.0/Notify-0.7.gir

%changelog
* Tue Nov 25 2014 Alexander Larsson <alexl@redhat.com> - 0.7.6-1
- Initial version, based on F21
