%global debug_package %{nil}
Name: uke-desktop-metas
Version: 1.0.0
Release: 1%{?dist}
Summary: Explicit desktop package selections for the Uke development platform
License: MIT
URL: https://github.com/MCC45TR/uke-desktop-metas
Source0: %{name}-%{version}.tar.xz
ExclusiveArch: aarch64
BuildRequires: tar xz
Requires: uke-core-meta >= 1.0.0
%description
Desktop selection metadata for Uke. The base installs no graphical session.
Display, touch, GPU and tablet boot remain independently unqualified.
%package -n kde-plasma-uke-meta
Summary: Stock Fedora Plasma Wayland package selection for Uke evaluation
Requires: %{name} = %{version}-%{release}
Requires: plasma-workspace kwin
Requires: plasma-nm plasma-pa bluedevil powerdevil
Requires: dolphin konsole kde-connect kdialog
Requires: xdg-desktop-portal-kde
Requires: mesa-dri-drivers mesa-vulkan-drivers
Requires: pipewire-pulseaudio wireplumber
%description -n kde-plasma-uke-meta
A stock Fedora Plasma Wayland dependency selection. No panel dimensions,
ICC profile, display manager enablement, touch mapping, thermal configuration
or Nabu service is copied. Desktop package solving is not a Uke graphics test.
%prep
%setup -q
%build
%install
install -Dm644 src/profile.json %{buildroot}%{_datadir}/senemos/uke/desktops/profile.json
%files
%license LICENSE
%doc README.md
%{_datadir}/senemos/uke/desktops/profile.json
%files -n kde-plasma-uke-meta
%license LICENSE

%changelog
* Mon Oct 05 2026 Senemos Maintainers <75160848+MCC45TR@users.noreply.github.com> - 1.0.0-1
- Build an independently scoped Uke development package with explicit readiness.
