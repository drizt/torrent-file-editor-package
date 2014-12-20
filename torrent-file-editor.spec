Name:           torrent-file-editor
Version:        0.1.0
Release:        2%{?dist}
Summary:        Qt based GUI tool designed to create and edit .torrent files

License:        GPLv3+
URL:            http://sf.net/projects/%{name}
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QJson)
BuildRequires:  desktop-file-utils

# Package puts icons to hicolor-icon-theme folders
Requires:       hicolor-icon-theme

%description
Qt based GUI tool designed to create and edit .torrent files.

Features
 - create .torrent file from scratch
 - edit .torrent file in user-friendly way
 - edit .torrent file in tree format
 - edit .torrent file in JSON format
 - add, remove and interchange files in .torrent file
 - support for codings


%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%make_install

%check
# Menu file is being installed when make install
# so it need only to check this allready installed file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sat Dec 20 2014 Ivan Romanov <drizt@land.ru> - 0.1.0-2
- Corrected sf source path
- Corrected project url
- Added hicolor-icon-theme to requires
- Improved description
- Use check section for desktop file validation

* Sat Dec 20 2014 Ivan Romanov <drizt@land.ru> - 0.1.0-1
- Initial version of package
