%define svn	54
%define rel	1
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
./autogen.sh

%build
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

