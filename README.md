# Uke desktop selections

This source family builds `uke-desktop-metas` and `kde-plasma-uke-meta` as real
AArch64 RPMs plus their SRPM. The base carries an explicit readiness profile and
requires the Uke core selection. The optional Plasma package selects stock Fedora
Wayland, desktop, audio, networking and portal packages. It does not configure
Uke panel geometry, ICC, touch, GPU, thermal policy or a display manager.

`make validate` and `make srpm` support source checks and complete source generation.
COPR's `.copr/Makefile` builds the source RPM from `main`; the GitHub push webhook
requests native Rawhide AArch64 compilation. Actual dependency closure and package
transactions must pass independently; graphics and tablet boot remain untested.
The package itself ships no runtime script or service and does not activate a
session. Fedora owns the dependencies' ordinary installation policies.

The [development COPR](https://copr.fedorainfracloud.org/coprs/mcc45tr/uke-linux-test/)
and [package hub](https://github.com/MCC45TR/uke-linux/blob/main/docs/PACKAGE-HUB.md)
separate packaging readiness from physical platform readiness. Nabu's reference
specification at `98188b595b42ba975f5bc238e596f330d3994ed8` contains panel-specific
profiles, runtime services and session choices; these are not Uke evidence.
