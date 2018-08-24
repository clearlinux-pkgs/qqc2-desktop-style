#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qqc2-desktop-style
Version  : 5.49.0
Release  : 1
URL      : https://download.kde.org/stable/frameworks/5.49/qqc2-desktop-style-5.49.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.49/qqc2-desktop-style-5.49.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: qqc2-desktop-style-lib
Requires: qqc2-desktop-style-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kirigami2-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
# QQC2StyleBridge
QtQuickControls 2 style that uses QWidget's QStyle for painting

%package dev
Summary: dev components for the qqc2-desktop-style package.
Group: Development
Requires: qqc2-desktop-style-lib
Provides: qqc2-desktop-style-devel

%description dev
dev components for the qqc2-desktop-style package.


%package lib
Summary: lib components for the qqc2-desktop-style package.
Group: Libraries
Requires: qqc2-desktop-style-license

%description lib
lib components for the qqc2-desktop-style package.


%package license
Summary: license components for the qqc2-desktop-style package.
Group: Default

%description license
license components for the qqc2-desktop-style package.


%prep
%setup -q -n qqc2-desktop-style-5.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535148206
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535148206
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qqc2-desktop-style
cp LICENSE.GPL-2 %{buildroot}/usr/share/doc/qqc2-desktop-style/LICENSE.GPL-2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5QQC2DeskopStyle/KF5QQC2DeskopStyleConfig.cmake
/usr/lib64/cmake/KF5QQC2DeskopStyle/KF5QQC2DeskopStyleConfigVersion.cmake

%files lib
%defattr(-,root,root,-)
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
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/MenuBarItem.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/MenuItem.qml
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
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/Switch.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/SwitchDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/SwitchIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TabBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TabButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TextArea.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/TextField.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ToolBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ToolButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/ToolTip.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/DefaultListItemBackground.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/org.kde.desktop/private/FocusRect.qml
/usr/lib64/qt5/qml/org/kde/qqc2desktopstyle/private/libqqc2desktopstyleplugin.so
/usr/lib64/qt5/qml/org/kde/qqc2desktopstyle/private/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/qqc2-desktop-style/LICENSE.GPL-2
