%define major 4

#define snapshot 20220106
%define libname %mklibname MauiKitArchiver
%define devname %mklibname -d MauiKitArchiver

Name:		mauikit-archiver
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Maui plugin for online archived/compressed files management
Url:		https://invent.kde.org/maui/mauikit-archiver/
Source0:	https://invent.kde.org/maui/mauikit-archiver/-/archive/%{?snapshot:master/mauikit-archiver-master.tar.bz2#/mauikit-archiver-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-archiver-v%{version}.tar.bz2}

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Network)

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)

%description
%{summary}.

%package -n %{libname}
Summary:	Library files for Maui Archiver

%description -n %{libname}
Library files for mauikit-archiver


%package -n %{devname}
Summary:	Development files for mauikit-archiver
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for mauikit-archiver

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

#find_lang mauikitarchiver

%files -n %{libname} 
#-f mauikitarchiver.lang
#{_libdir}/libMauiKitTerminal4.so.%{major}*
#{_libdir}/qt6/qml/org/mauikit/

%files -n %{devname}
#{_includedir}/MauiKit4/Terminal/
#{_libdir}/cmake/MauiKitTerminal4/
#{_libdir}/libMauiKitTerminal4.so
