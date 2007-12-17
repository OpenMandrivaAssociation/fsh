%define name fsh
%define version 1.2
%define release %mkrel 6

Summary : A tool for ssh remote execution of commands
Name: %name
Version: %version
Release: %release
License: GPL
URL: http://www.lysator.liu.se/fsh/ 
Group: Networking/Other
Source: %{name}-%{version}.tar.bz2

%description
fsh is a tool for establishing an ssh tunnel for remote execution of commands 
without requiring an ssh authentication on every connection. Once the tunnel 
is established, remote commands can be executed almost instantaneously. 
This makes systems such as remote cvs over ssh much faster.

%prep

%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.DEVO 
%doc RELEASING THANKS TODO
%_bindir/*
%_libdir/*
%_datadir/%{name}/
%{_infodir}/%{name}.info.bz2

