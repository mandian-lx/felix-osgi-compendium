%{?_javapackages_macros:%_javapackages_macros}

%global bundle org.osgi.compendium

Name:           felix-osgi-compendium
Version:        1.4.0
Release:        25.1
Summary:        Felix OSGi R4 Compendium Bundle
License:        ASL 2.0
Group:          Development/Java
URL:            http://felix.apache.org
BuildArch:      noarch

Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

Patch0:         0001-Fix-servlet-api-dependency.patch
Patch1:         0002-Fix-compile-target.patch
Patch2:         0003-Add-CM_LOCATION_CHANGED-property-to-ConfigurationEve.patch
Patch3:         0004-Add-TARGET-property-to-ConfigurationPermission.patch
# This is an ugly patch that adds getResourceURL method. This prevents jbosgi-framework
# package from bundling osgi files. Once the jbosgi-framework will be updated
# to a new version without the need for this patch, REMOVE it!
Patch4:         0005-Add-getResourceURL-method-to-make-jbosgi-framework-h.patch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.osgi.core)
BuildRequires:  mvn(org.apache.felix:org.osgi.foundation)

%description
OSGi Service Platform Release 4 Compendium Interfaces and Classes.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

# fix servlet api properly
%patch0 -p1
# fix compile source/target
%patch1 -p1
# add CM_LOCATION_CHANGED property
%patch2 -p1
# add TARGET property
%patch3 -p1
# add getResourceURL method
%patch4 -p1

%mvn_file :%{bundle} "felix/%{bundle}"
%mvn_alias "org.apache.felix:%{bundle}" "org.osgi:%{bundle}"

%build
%mvn_build -- -Drat.numUnapprovedLicenses=100

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-23
- Regenerate build-requires
- Update to current packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 5 2014 Alexander Kurtakov <akurtako@redhat.com> 1.4.0-19
- Switch to mvn style BR for servlet api.

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-18
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-17
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.0-16
- Update for latest guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4.0-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Marek Goldmann <mgoldman@redhat.com> 1.4.0-11
- Add getResourceURL method to XMLParserActivator

* Fri Jun 15 2012 Marek Goldmann <mgoldman@redhat.com> 1.4.0-10
- Add CM_LOCATION_CHANGED property to ConfigurationEvent
- Add TARGET property to ConfigurationPermission

* Wed Mar 21 2012 Alexander Kurtakov <akurtako@redhat.com> 1.4.0-9
- Move to tomcat 7.x servlet api.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-7
- Add org.osgi groupId to depmap
- Packaging fixes

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-5
- Fix servlet api in pom

* Mon Dec 27 2010 Mat Booth <fedora@matbooth.co.uk> 1.4.0-4
- Fix POM names RHBZ #655800.
- Versionless jars/docs, update maven plug-in BRs.
- Other misc guideline compliances.

* Mon Jul 12 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.4.0-3
- Avoid owning the %%{_javadir}/%%{project} directory

* Wed Jul 07 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.4.0-2
- Use maven instead of ant

* Tue Jun 22 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.4.0-1
- Release 1.4.0
