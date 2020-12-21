%global srcname virtkey
%global sum Python extension for emulating keypresses and getting current keyboard layout
%global ver 0.63.0
%global shortver 0.63

Name:           python-%{srcname}
Version:        0.63.0
Release:        13%{?dist}
Summary:        %{sum}

#missing copy of GPL, licensing info in source file
License:        GPLv2+
URL:            https://launchpad.net/virtkey
Source0:        http://launchpad.net/virtkey/trunk/%{shortver}/+download/%{srcname}-%{version}.tar.gz
#Patch0:         virtkey-gdk-pixbuf-headers.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libXtst-devel,
BuildRequires:  gtk2-devel,
BuildRequires:  glib2-devel,
BuildRequires:  libxkbfile-devel

%description
%{sum}

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum}

%prep
%autosetup -n %{srcname}-%{version}
#%patch0 -p1

# move this here for so the doc macro can pick it up in files section
mv docs/api.txt api.txt

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license COPYING
%doc README NEWS AUTHORS api.txt
%{python3_sitearch}/*

%changelog
* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.63.0-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.63.0-10
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.63.0-8
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.63.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.63.0-2
- Rebuild for Python 3.6

* Thu Sep 08 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.63-1
- Update to latest upstream
- Provide python2 and python3 subpackages (BZ#1309264)
- Update to latest python packaging guidelines and rpm macros

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-19
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Adam Jackson <ajax@redhat.com> 0.50-10
- Rebuild to break bogus libpng dep

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.50-8
- Patch to find gdk-pixbuf2 headers

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.50-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.50-4
- Rebuild for Python 2.6

* Thu May 22 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 0.50-3
- Add patch to fix 64bit build issue, thanks Parag and Ivazquez
* Tue May 06 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 0.50-2
- Add missing glib2-devel build dependency
* Tue May 06 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 0.50-1
- Initial build
