Summary:	Hotwire Shell
Name:		hotwire
Version:	0.567
Release:	1
Source0:	http://hotwire-shell.org/download/%{name}-%{version}.zip
# Source0-md5:	ced9b7a2ab9a0c40ed62c014d953b286
License:	GPL
Group:		X11/Applications
URL:		http://hotwire-shell.org/
BuildRequires:	python-devel
Requires:	python-dbus
Requires:	python-gnome-desktop
Requires:	python-gnome-vfs
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive hybrid text/graphical shell for developers and system
administrators

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/hotwire
%{py_sitescriptdir}/hotwire-0.567-py2.5.egg-info
%dir %{py_sitescriptdir}/hotwire/
%{py_sitescriptdir}/hotwire/*.py[co]
%dir %{py_sitescriptdir}/hotwire/builtins/
%{py_sitescriptdir}/hotwire/builtins/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/
%{py_sitescriptdir}/hotwire/sysdep/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/fs_impl/
%{py_sitescriptdir}/hotwire/sysdep/fs_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/ipc_impl/
%{py_sitescriptdir}/hotwire/sysdep/ipc_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/proc_impl
%{py_sitescriptdir}/hotwire/sysdep/proc_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire/sysdep/term_impl/
%{py_sitescriptdir}/hotwire/sysdep/term_impl/*.py[co]
%dir %{py_sitescriptdir}/hotwire_ui/
%{py_sitescriptdir}/hotwire_ui/*.py[co]
%dir %{py_sitescriptdir}/hotwire_ui/renderers/
%{py_sitescriptdir}/hotwire_ui/renderers/*.py[co]
%{_desktopdir}/hotwire.desktop
