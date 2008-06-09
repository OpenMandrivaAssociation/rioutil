%define name	rioutil
%define version	1.5.0
%define cvs 20051012
%define rel 0.%cvs.1
%define release %mkrel %rel

%define major	1
%define libname %mklibname %name %major

Name: 	 	%{name}
Summary: 	File transfer utility for newer RIO MP3 players
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{cvs}.tar.bz2
URL:		http://rioutil.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libusb-devel

%description
RioUtil is a utility designed for the use of interfacing with Rio's third,
fourth, and fifth generations of portable mp3 players:
Rio 600/800/900/S-Series/Riot/psa[play/Fuse/Chiba/Cali.

It goes beyond the originally packaged software by providing downloading.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
#Provides:	%name
#Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
#Requires: 	%{libname} >= %{version}-%{release}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name
./autogen.sh

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO README
%{_bindir}/%name
%{_mandir}/man1/*

#%files -n %{libname}
#%defattr(-,root,root)
#%{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a

