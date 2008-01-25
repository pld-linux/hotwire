Summary:	Hotwire Shell
Summary(pl.UTF-8):	Powłoka Hotwire
Name:		hotwire
Version:	0.700
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://hotwire-shell.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	51620a43d855934fd3da73cd4a7bafb5
URL:		http://code.google.com/p/hotwire-shell/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	unzip
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	python-dbus
Requires:	python-gnome-desktop
Requires:	python-gnome-vfs
Requires:	python-pygtk-gtk >= 2:2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive hybrid text/graphical shell for developers and system
administrators.

%description -l pl.UTF-8
Interaktywna hybrydowa powłoka tekstowo-graficzna dla programistów i
administratorów systemów.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/hotwire-editor
%attr(755,root,root) %{_bindir}/hotwire-gedit-blocking
%attr(755,root,root) %{_bindir}/hotwire-runtty
%attr(755,root,root) %{_bindir}/hotwire-ssh
%attr(755,root,root) %{_bindir}/hotwire-sudo
%attr(755,root,root) %{_bindir}/hotwire
%{_datadir}/hotwire
%{py_sitescriptdir}/hotwire-*.egg-info
%dir %{py_sitescriptdir}/hotapps
%{py_sitescriptdir}/hotapps/*.py[co]
%dir %{py_sitescriptdir}/hotapps/hotssh
%{py_sitescriptdir}/hotapps/hotssh/*.py[co]
%dir %{py_sitescriptdir}/hotapps/hotsudo
%{py_sitescriptdir}/hotapps/hotsudo/*.py[co]
%dir %{py_sitescriptdir}/hotvte
%{py_sitescriptdir}/hotvte/*.py[co]
%dir %{py_sitescriptdir}/hotwire
%{py_sitescriptdir}/hotwire/*.py[co]
%dir %{py_sitescriptdir}/hotwire/builtins
%{py_sitescriptdir}/hotwire/builtins/*.py[co]
%dir %{py_sitescriptdir}/hotwire/externals
%{py_sitescriptdir}/hotwire/externals/*.py[co]
%dir %{py_sitescriptdir}/hotwire/externals/dispatch
%{py_sitescriptdir}/hotwire/externals/dispatch/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep
%{py_sitescriptdir}/hotwire/sysdep/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/fs_impl
%{py_sitescriptdir}/hotwire/sysdep/fs_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/ipc_impl
%{py_sitescriptdir}/hotwire/sysdep/ipc_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/proc_impl
%{py_sitescriptdir}/hotwire/sysdep/proc_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/term_impl
%{py_sitescriptdir}/hotwire/sysdep/term_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire_ui
%{py_sitescriptdir}/hotwire_ui/*.py[co]
%dir %{py_sitescriptdir}/hotwire_ui/adaptors
%{py_sitescriptdir}/hotwire_ui/adaptors/*.py[co]
%dir %{py_sitescriptdir}/hotwire_ui/renderers
%{py_sitescriptdir}/hotwire_ui/renderers/*.py[co]
%{_desktopdir}/hotwire.desktop
%{_iconsdir}/hicolor/24x24/apps/hotwire-openssh.png
%{_iconsdir}/hicolor/24x24/apps/hotwire-sudo.png
%{_iconsdir}/hicolor/24x24/apps/hotwire.png
