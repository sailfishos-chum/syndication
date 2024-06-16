%global kf5_version 5.115.0

Name:    opt-kf5-syndication
Epoch:   1
Version: 5.115.0
Release: 1%{?dist}
Summary: The Syndication Library
License: LGPLv2+ and BSD
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires:  opt-kf5-kio-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kcodecs-devel >= %{kf5_version}
BuildRequires:  opt-qt5-qtbase-devel

%{?opt_kf5_default_filter}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
  -DKDE_INSTALL_LIBEXECDIR=%{_opt_kf5_libexecdir}
%make_build

popd


%install
pushd build
make DESTDIR=%{buildroot} install
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/syndication.*
%{_opt_kf5_libdir}/libKF5Syndication.so.*

%files devel
%{_opt_kf5_includedir}/KF5/Syndication/
%{_opt_kf5_libdir}/libKF5Syndication.so
%{_opt_kf5_libdir}/cmake/KF5Syndication/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_Syndication.pri
