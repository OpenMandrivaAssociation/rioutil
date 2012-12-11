%define svn	54
%define rel	3
%if %svn
%define release		%mkrel 0.%{svn}.%{rel}
%define distname	%{name}-%{svn}.tar.lzma
%define dirname		%{name}-1.x
%else
%define release		%mkrel %{rel}
%define distname	%{name}-%{version}.tar.gz
%define dirname		%{name}-%{version}
%endif

%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name: 	 	rioutil
Summary: 	File transfer utility for newer RIO MP3 players
Version: 	1.5.1
Release: 	%{release}
Source0:	http://downloads.sourceforge.net/%{name}/%{distname}
URL:		http://rioutil.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libusb-devel

%description
RioUtil is a utility designed for the use of interfacing with Rio's third,
fourth, and fifth generations of portable mp3 players:
Rio 600/800/900/S-Series/Riot/Nike psa[play/Fuse/Chiba/Cali/Nitrus.

It goes beyond the originally packaged software by providing downloading.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{name}-devel
Obsoletes:	%{mklibname rioutil 1 -d}

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q -n %{dirname}

%build
sed -i -e 's,$(prefix)/lib,%{_libdir},g' Makefile.am librioutil/Makefile.am
./autogen.sh
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO README
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.*a
%{_libdir}/*.so



%changelog
* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 1.5.1-0.54.3mdv2010.0
+ Revision: 439803
- rebuild for new libusb

* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5.1-0.54.2mdv2010.0
+ Revision: 433348
- rebuild

* Thu Sep 04 2008 Adam Williamson <awilliamson@mandriva.org> 1.5.1-0.54.1mdv2009.0
+ Revision: 280819
- fix libdir on x86-64
- restore library package, library is being built now
- new devel policy
- new license policy
- clean spec
- bump to current SVN, bump version as 1.5.0 was released

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 1.5.0-0.20051012.1mdv2009.0
+ Revision: 217207
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5.0-0.20051012.1mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import rioutil


* Mon Jul 31 2006 Götz Waschk <waschk@mandriva.org> 1.5.0-0.20051012.1mdv2007.0
- new snapshot

* Mon Nov 29 2004 Austin Acton <austin@mandrake.org> 1.4.7-1mdk
- 1.4.7

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4.6.1-1mdk
- 1.4.6.1

* Sun Aug 15 2004 Austin Acton <austin@mandrake.org> 1.4.4-1mdk
- initial package
