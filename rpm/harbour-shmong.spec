Name: harbour-shmong
Version: 0.1.0
Release:	1%{?dist}
Summary: Shmong - XMPP Client for Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://github.com/ron282/shmong
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(sailfishapp) >= 1.0.2

BuildRequires:  libiphb-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  sqlite-devel
BuildRequires:  libqxmpp-devel

Requires:   sailfishsilica-qt5
Requires:   qt5-qtdeclarative-import-xmllistmodel
Requires:   libqxmpp

%description
XMPP Client for Sailfish OS


%prep
%setup -q


%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lipstick/notificationcategories/%{name}-message.conf
%{_datadir}/%{name}/qml
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/translations
%{_datadir}/icons/hicolor/86x86/apps
%{_bindir}/%{name}
# >> files
# << files


%changelog

