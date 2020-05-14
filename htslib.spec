#%global debug_package %{nil}

Name:    htslib
Version: 1.10.2
Release: 1
Summary: C library for high-throughput sequencing data formats
License: MIT and BSD
URL:	 http://www.htslib.org
Source0: https://github.com/samtools/htslib/archive/%{name}-%{version}.tar.gz

BuildRequires: 	gcc autoconf automake  make curl-devel zlib-devel 

%description
HTSlib is an implementation of a unified C library for accessing common file formats, such as SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by samtools and bcftools. HTSlib only depends on zlib. It is known to be compatible with gcc, g++ and clang.
HTSlib implements a generalized BAM index, with file extension .csi (coordinate-sorted index). The HTSlib file reader first looks for the new index and then for the old if the new index is absent.


%package devel
Summary: libs for htslib package 
Requires: %{name} = %{version}-%{release}
%description devel
HTSlib is an implementation of a unified C library for accessing common file formats, such as SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by samtools and bcftools. HTSlib only depends on zlib. It is known to be compatible with gcc, g++ and clang.
HTSlib implements a generalized BAM index, with file extension .csi (coordinate-sorted index). The HTSlib file reader first looks for the new index and then for the old if the new index is absent.


%prep
%setup -q -n %{name}-%{version}/

%build
autoheader
autoconf
%configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-gcs --enable-libcurl --enable-s3  
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/libhts.a

%pre
%preun
%post
%postun

%check

%files
%license LICENSE 
%doc README NEWS README.large_positions.md
%{_bindir}/*
%{_libdir}/libhts.so.*
%{_mandir}/*


%files devel
%{_libdir}/libhts.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


%changelog
* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

