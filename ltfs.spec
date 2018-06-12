Summary: Linear Tape File System (On GitHub)
Name: ltfs
Version: 2.4.0.2
Release: 10071
License: BSD
Group: Util
Packager: User piste2750 on GitHub

URL:     https://github.com/LinearTapeFileSystem/ltfs
Source0: https://github.com/LinearTapeFileSystem/ltfs/archive/v2.4.0.2-10071/ltfs-2.4.0.2.tar.gz

BuildRequires: automake autoconf libtool
BuildRequires: icu libicu-devel libxml2-devel libuuid-devel fuse-devel
BuildRequires: net-snmp-devel

Requires: /sbin/ldconfig, /usr/bin/awk, /usr/bin/systemctl
Requires:  libicu libxml2 libuuid fuse
Requires:  net-snmp

%if %{defined suse_version}
%debug_package
%endif

%description
Reference implementation of the LTFS format Spec.

%prep
%autosetup -n ltfs-%{version}-%{release}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

# Prepare symbolic link (backends)
%if "%{_lib}" == "lib64"
    mkdir -p $RPM_BUILD_ROOT%{_exec_prefix}/lib
    ln -s -f %{_libdir}/ltfs $RPM_BUILD_ROOT%{_exec_prefix}/lib/ltfs
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*
%{_sysconfdir}/*
%if "%{_lib}" == "lib64"
    %{_exec_prefix}/lib/ltfs
%endif
