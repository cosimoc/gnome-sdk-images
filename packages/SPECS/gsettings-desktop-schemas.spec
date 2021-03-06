%global release_version %%(echo %{version} | awk -F. '{print $1"."$2}')
%global debug_package %{nil}

Name:           gsettings-desktop-schemas
Version:        3.15.4
Release:        1%{?dist}
Summary:        A collection of GSettings schemas

Group:          System Environment/Libraries
License:        LGPLv2+
# no homepage exists for this component
URL:            http://bugzilla.gnome.org/enter_bug.cgi?product=gsettings-desktop-schemas
#VCS: git:git://git.gnome.org/gsettings-desktop-schemas
Source:         http://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz

BuildRequires: gnome-sdk-base
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel

Requires: glib2

%description
gsettings-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries
and header files for developing applications that use %{name}.


%prep
%setup -q

%build
%configure --disable-schemas-compile --enable-introspection=yes
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{name} --with-gnome

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files -f %{name}.lang
%doc AUTHORS COPYING MAINTAINERS NEWS README
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/GConf/gsettings/gsettings-desktop-schemas.convert
%{_datadir}/GConf/gsettings/wm-schemas.convert
%{_libdir}/girepository-1.0/GDesktopEnums-3.0.typelib

%files devel
%doc HACKING
%{_includedir}/*
%{_datadir}/pkgconfig/*
%{_datadir}/gir-1.0/GDesktopEnums-3.0.gir


%changelog
* Mon Nov 24 2014 Alexander Larsson <alexl@redhat.com> - 3.14.1-1
- Initial version, based on F21

