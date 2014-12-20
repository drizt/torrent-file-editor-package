Name:           torrent-file-editor
Version:        0.1.0
Release:        1%{?dist}
Summary:        Qt based GUI tool designed to create and edit .torrent files

License:        GPLv3+
URL:            http://sourceforge.net/projects/torrent-file-editor/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QJson)
BuildRequires:  desktop-file-utils

%description
%{summary}.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%make_install

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
* Sat Dec 20 2014 Ivan Romanov <drizt@land.ru> - 0.1.0-1
- Initial version of package
