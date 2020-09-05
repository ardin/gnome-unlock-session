Name:       	{{{ git_dir_name }}}
Version:    	{{{ git_dir_version }}}
Release:    	1%{?dist}
Summary:	Gnome unlock session (super+u)
Group:		ardin

URL:        	https://github.com/ardin/gnome-unlock-session

VCS:        	{{{ git_dir_vcs }}}
Source:     	{{{ git_dir_pack }}}

License:	GPL

Requires:       python3-evdev

%description
Fast gnome unlock session by pressing SUPER+U for quite safe home environments

%global debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0644 gnome-unlock-session ${RPM_BUILD_ROOT}/usr/bin/gnome-unlock-session

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/systemd/system/
install -m 0644 gnome-unlock-session.service ${RPM_BUILD_ROOT}/usr/lib/systemd/system/gnome-unlock-session.service

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
/usr/bin/systemctl daemon-reload
/usr/bin/systemctl enable gnome-unlock-session.service
/usr/bin/systemctl start gnome-unlock-session.service

%files
%dir /usr/bin
/usr/bin/gnome-unlock-session
%dir /usr/lib/systemd/system/
/usr/lib/systemd/system/gnome-unlock-session.service

%changelog
{{{ git_dir_changelog }}}

