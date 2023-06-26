Name:           xeyes
Version:        1.0.0    
Release:        1%{?dist}
Summary:        Xeyes installation with CRON job
BuildArch:      x86_64

License:        BSD
Source0:        %{name}-%{version}.tar.gz
AutoReq:        no

%define _build_id_links none

%description
^{T<xeyes>}, [extract]
Xeyes program and cron job


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/etc/cron.d
cp %{name} ${RPM_BUILD_ROOT}/%{_bindir}
cp xeyes.cron ${RPM_BUILD_ROOT}/etc/cron.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %attr(0755, root, root) "/usr/bin"
%defattr(755,root,root) 
/usr/bin/xeyes

%dir %attr(0755, root, root) "/etc/cron.d"
%defattr(644,root,root) 
/etc/cron.d/xeyes.cron

%changelog
* Fri Jun 23 19:51:01 EDT 2023 Tim Brom <thb@grimm-co.com>
- 

- 
