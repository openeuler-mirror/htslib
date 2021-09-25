Name:    htslib
Version: 1.10.2
Release: 3
Summary: C library for high-throughput sequencing data formats
License: MIT and BSD
URL:	 http://www.htslib.org
Source0: https://github.com/samtools/htslib/archive/%{name}-%{version}.tar.gz

BuildRequires: 	gcc autoconf automake make libcurl-devel zlib-devel bzip2-devel xz-devel libxcrypt-devel openssl-devel

%description
HTSlib is an implementation of a unified C library for accessing common file 
formats, such as SAM, CRAM and VCF, used for high-throughput sequencing data, 
and is the core library used by samtools and bcftools. HTSlib only depends on 
zlib. It is known to be compatible with gcc, g++ and clang.
HTSlib implements a generalized BAM index, with file extension .csi (
coordinate-sorted index). The HTSlib file reader first looks for the new index
and then for the old if the new index is absent.

%package devel
Summary: libs for htslib package 
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Additional htslib-based tools
Requires: %{name} = %{version}-%{release}

%description tools
Includes the popular tabix indexer, which indexes both .tbi and .csi formats,
the htsfile identifier tool, and the bgzip compression utility.


%prep
%setup -q -n %{name}-%{version}

%build
autoheader
autoconf
%configure --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-plugins \
    --enable-gcs \
    --enable-libcurl \
    --enable-s3
%make_build
# As we don't install libhts.a, the .private keywords are irrelevant.
sed -i -E '/^(Libs|Requires)\.private:/d' htslib.pc.tmp

%install
%make_install
# The dynamic libraries should have execution permissions, otherwise it cannot be referenced by other packages
find %{buildroot}/%{_libdir} -iname "*.so.*" -exec chmod +x {} \;
rm -rf %{buildroot}/%{_libdir}/libhts.a

%files
%license LICENSE 
%doc README NEWS README.large_positions.md
%{_libdir}/libhts.so.*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/hfile_gcs.so
%{_libexecdir}/%{name}/hfile_libcurl.so
%{_libexecdir}/%{name}/hfile_s3.so
%{_libexecdir}/%{name}/hfile_s3_write.so
%{_mandir}/man5/faidx.5*
%{_mandir}/man5/sam.5*
%{_mandir}/man5/vcf.5*
%{_mandir}/man7/htslib-s3-plugin.7*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libhts.so
%{_libdir}/pkgconfig/htslib.pc

%files tools
%{_bindir}/bgzip
%{_bindir}/htsfile
%{_bindir}/tabix
%{_mandir}/man1/bgzip.1*
%{_mandir}/man1/htsfile.1*
%{_mandir}/man1/tabix.1*

%changelog
* Wed Jun 16 2021 zhao yang <yangzhao1@kylinos.cn> - 1.10.2-3
- Add htslib-tools package

* Fri Mar 26 2021 herengui <herengui@uniontech.com> - 1.10.2-2
- Add compilation parameters, update package lists

* Sun Mar 29 2020 Wei Xiong <myeuler@163.com> - 1.10.2-1
- Package init

