%define _libdir /opt/nec/ve/lib
%define _includedir /opt/nec/ve/include
%define _sharedir /opt/nec/ve/share
%define __strip /opt/nec/ve/bin/nstrip
%define optflags -g -O2
%global __debug_install_post /opt/nec/ve/libexec/find-debuginfo.sh %{nil}

Summary: LAPACK C interface
Name: lapacke-ve
Version: 3.8.0
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://www.netlib.org/lapack/
Source0: lapacke-ve-%{version}.tgz
BuildRequires: nec-nc++
Requires: nec-lapack-ve
Requires: nec-blas-ve
 
%description
LAPACKE is a C interface to LAPACK, coded in C. This package contains
the SX-Aurora Vector Engine version of LAPACKE that should work with
the LAPACK library provided by NEC in the NLC / SDK.
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision. LAPACK
is coded in Fortran90.


%prep
%setup -n %{name}-%{version}

sed -i "s|@LONGVER@|%{version}|g" Makefile
 
%build
make clean
make -j 20 lapacke
 
%install
export STRIP=/opt/nec/ve/bin/nstrip
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/debug
mkdir -p ${RPM_BUILD_ROOT}%{_sharedir}/%{name}
chmod 755 ${RPM_BUILD_ROOT}%{_sharedir}/%{name}
 
cp -f liblapacke.a ${RPM_BUILD_ROOT}%{_libdir}/
cp -f liblapacke.a ${RPM_BUILD_ROOT}%{_libdir}/debug
 
# Lapacke headers
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/lapacke/
chmod 755 ${RPM_BUILD_ROOT}%{_includedir}/lapacke/
cp -a include/*.h ${RPM_BUILD_ROOT}%{_includedir}/lapacke/

# some docs
cp -a LICENSE README doc/* ${RPM_BUILD_ROOT}%{_sharedir}/%{name}

%files
%defattr(-,root,root)
%doc %{_sharedir}/%{name}/*
%{_includedir}/lapacke/
%{_libdir}/liblapacke.a
 
%changelog
* Wed Dec 26 2018 Erich Focht <efocht@gmail.com> - 3.8.0-1
- Initial version of lapacke-ve RPM
 
