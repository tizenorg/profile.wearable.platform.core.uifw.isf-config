Name:       isf-config-wearable
Summary:    ISF config files for wearable profile
Version:    0.1.0
Release:    1
Group:      Graphics & UI Framework/Input
License:    Apache-2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
Requires(post): coreutils

%description
ISF configuration files for wearable profile

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_sysconfdir}/scim/conf
%__mkdir_p %{buildroot}%{_prefix}/lib/systemd/user
%__mkdir_p %{buildroot}%{_prefix}/lib/systemd/user/default.target.wants

%__cp etc/scim/conf/* %{buildroot}%{_sysconfdir}/scim/conf
%__cp scim.service %{buildroot}%{_prefix}/lib/systemd/user
%__cp scim.path %{buildroot}%{_prefix}/lib/systemd/user

%post
ln -sf %{_prefix}/lib/systemd/user/scim.path %{_prefix}/lib/systemd/user/default.target.wants/scim.path

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
/etc/scim/conf/*
%{_prefix}/lib/systemd/user/scim.service
%{_prefix}/lib/systemd/user/scim.path
%license LICENSE.APLv2
