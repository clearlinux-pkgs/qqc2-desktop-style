#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : qqc2-desktop-style
Version  : 5.107.0
Release  : 218
URL      : https://download.kde.org/stable/frameworks/5.107/qqc2-desktop-style-5.107.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.107/qqc2-desktop-style-5.107.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.107/qqc2-desktop-style-5.107.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-3.0
Requires: qqc2-desktop-style-lib = %{version}-%{release}
Requires: qqc2-desktop-style-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kiconthemes-dev
BuildRequires : kirigami2-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : qtx11extras-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# QQC2StyleBridge
QtQuickControls 2 style that uses QWidget's QStyle for painting

%package dev
Summary: dev components for the qqc2-desktop-style package.
Group: Development
Requires: qqc2-desktop-style-lib = %{version}-%{release}
Provides: qqc2-desktop-style-devel = %{version}-%{release}
Requires: qqc2-desktop-style = %{version}-%{release}

%description dev
dev components for the qqc2-desktop-style package.


%package lib
Summary: lib components for the qqc2-desktop-style package.
Group: Libraries
Requires: qqc2-desktop-style-license = %{version}-%{release}

%description lib
lib components for the qqc2-desktop-style package.


%package license
Summary: license components for the qqc2-desktop-style package.
Group: Default

%description license
license components for the qqc2-desktop-style package.


%prep
%setup -q -n qqc2-desktop-style-5.107.0
cd %{_builddir}/qqc2-desktop-style-5.107.0

%build
## build_prepend content
# Make sure the package only builds if kiconthemes and kconfigwidgets have been updated first
sed -i -r -e 's,(KF.?IconThemes \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
sed -i -r -e 's,(KF.?ConfigWidgets \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687184028
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if kiconthemes and kconfigwidgets have been updated first
sed -i -r -e 's,(KF.?IconThemes \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
sed -i -r -e 's,(KF.?ConfigWidgets \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1687184028
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qqc2-desktop-style
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/qqc2-desktop-style-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/qqc2-desktop-style/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5QQC2DeskopStyle/KF5QQC2DeskopStyleConfig.cmake
/usr/lib64/cmake/KF5QQC2DeskopStyle/KF5QQC2DeskopStyleConfigVersion.cmake
/usr/lib64/cmake/KF5QQC2DesktopStyle/KF5QQC2DesktopStyleConfig.cmake
/usr/lib64/cmake/KF5QQC2DesktopStyle/KF5QQC2DesktopStyleConfigVersion.cmake

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/kirigami/org.kde.desktop.so
/V3/usr/lib64/qt5/qml/org/kde/qqc2desktopstyle/private/libqqc2desktopstyleplugin.so
/usr/lib64/qt5/plugins/kf5/kirigami/org.kde.desktop.so
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/BusyIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Button.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/CheckBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/CheckDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/CheckIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ComboBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Container.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Control.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/DelayButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Dial.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Dialog.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/DialogButtonBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Drawer.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Frame.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/GroupBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ItemDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Label.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Menu.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/MenuBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/MenuBarItem.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/MenuItem.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/MenuSeparator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Page.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Pane.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Popup.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ProgressBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/RadioButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/RadioDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/RangeSlider.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/RoundButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ScrollBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ScrollView.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Slider.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/SpinBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/StackView.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Switch.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/SwitchDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/SwitchIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TabBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TabButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TextArea.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TextField.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ToolBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ToolButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ToolSeparator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ToolTip.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/DefaultListItemBackground.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/FocusRect.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/MobileCursor.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/MobileTextActionsToolBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/TextFieldContextMenu.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/qmldir
/usr/lib64/qt5/qml/org/kde/qqc2desktopstyle/private/libqqc2desktopstyleplugin.so
/usr/lib64/qt5/qml/org/kde/qqc2desktopstyle/private/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qqc2-desktop-style/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/qqc2-desktop-style/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/qqc2-desktop-style/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/qqc2-desktop-style/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/qqc2-desktop-style/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/qqc2-desktop-style/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/qqc2-desktop-style/e712eadfab0d2357c0f50f599ef35ee0d87534cb
