%define name fsh
%define version 1.2
%define release %mkrel 10

Summary : A tool for ssh remote execution of commands
Name: %name
Version: %version
Release: %release
License: GPL
URL: http://www.lysator.liu.se/fsh/ 
Group: Networking/Other
Source: %{name}-%{version}.tar.bz2
BuildRoot: %_tmppath/%{name}-buildroot
Buildrequires: python-devel

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
%{_infodir}/%{name}.info*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-10mdv2011.0
+ Revision: 610776
- rebuild

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 1.2-9mdv2010.1
+ Revision: 497281
- add python-devel buildrequires

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2-9mdv2010.0
+ Revision: 428923
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2-8mdv2009.0
+ Revision: 245423
- rebuild

* Tue Jan 08 2008 Thierry Vignaud <tv@mandriva.org> 1.2-6mdv2008.1
+ Revision: 146706
- do not harcode extension
- kill re-definition of %%buildroot on Pixel's request
- import fsh

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Aug 09 2006 Lenny Cartier <lenny@mandriva.com> 1.2-6mdv2007.0
- rebuild

* Mon Mar 21 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.2-5mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2-4mdk
- rebuild

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2-3mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2-2mdk
- rebuild

* Thu Aug 29 2002  Lenny Cartier <lenny@mandrakesoft.com> 1.2-1mdk
- 1.2

* Tue Jul 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1-3mdk
- rebuild

* Thu May  3 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1-2mdk
- Make it works, redo the packaging.

* Mon Dec 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1-1mdk
- new in contribs
