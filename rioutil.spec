%define svn	54

%define release		
%define distname	%{name}-%{svn}.tar.lzma

%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name: 	 	rioutil
Summary: 	File transfer utility for newer RIO MP3 players
Version: 	1.5.1
Release: 	0.%{svn}.4
Source0:	http://downloads.sourceforge.net/%{name}/%{distname}
URL:		https://rioutil.sourceforge.net/
License:	GPLv2+
Group:		Sound
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
%setup -q -n %{name}-1.x

%build
sed -i -e 's,$(prefix)/lib,%{_libdir},g' Makefile.am librioutil/Makefile.am
./autogen.sh
%configure2_5x
%make
										
%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS TODO README
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.*a
%{_libdir}/*.so
