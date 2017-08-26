%define commit 5ba17f90ec173e773470bc80ea26bca9a3f093fd
%define shortcommit %(c=%{commit}; echo ${c:0:7})

%define	minor_version 1054
%define major 0
%define minor 10
%define libname 	%mklibname %{name} %{major}.%{minor}
%define libengine 	%mklibname %{name}-engine %{major}.%{minor}
%define devname 	%mklibname -d %{name} %{major}

Summary:	Simple tabbed text editor
Name:		juffed
Version: 	0.10
Release: 	11
License:	GPLv2
Group:		Editors
#Source0:	https://github.com/Mezomish/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/Mezomish/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:		%{name}-0.10-qtsingleapplication.patch
Patch1:		%{name}-0.10-port-TODOList-to-qt5.patch
Url:		http://juffed.com
BuildRequires:	cmake
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	pkgconfig(enca)
BuildRequires:	qscintilla-qt5-devel
BuildRequires:	qtsingleapplication-devel

Requires:	%{libname} = %{version}-%{release}

%description
Simple tabbed text editor with syntax highlighting for:
	- C++
	- Python
	- HTML
	- PHP
	- XML
	- TeX
	- Makefiles
	- ini-files
	- patch-files

Some features:
	- multi-document interface (tabs)
	- syntax highlighting
	- code blocks folding
	- sessions support
	- find/replace using regular expressions
	- charset selection and auto-detection
	- line markers
	- international languages and Unicode support
	- plugins

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------

%package -n %{libname}
Summary:    %{summary} libraries
Group:      System/Libraries

%description -n %{libname}
%{summary} libraries

%files -n %{libname}
%{_libdir}/libjuff.so.*

#----------------------------------------------------------------------

%package -n	%{libengine}
Summary:	%{summary} libraries
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{libengine}
%{summary} libraries

%files -n %{libengine}
%{_libdir}/libjuffed-engine-qsci.so.%{version}

#----------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development package for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
%{summary}

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libjuffed-engine-qsci.so
%{_libdir}/libjuff.so

#----------------------------------------------------------------------

%package	plugins
Summary:	Plugins for juffed
Group:		Development/Other
Requires:	%{name}-plugin-doclist
Requires:	%{name}-plugin-favorites
Requires:	%{name}-plugin-findinfiles
Requires:	%{name}-plugin-filemanager
Requires:	%{name}-plugin-sort
Requires:	%{name}-plugin-symbolbrowser
Requires:	%{name}-plugin-xmlformat
Requires:	%{name}-plugin-keybindings

%description	plugins
%{summary}
See http://code.google.com/p/juffed-plugins/wiki/JuffEd_Plugins_Tutorial 
for details.

%files plugins

#----------------------------------------------------------------------

%package	plugin-autosave
Summary:	AutoSave plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	plugin-autosave
%{summary}

%files plugin-autosave
%{_libdir}/%{name}/plugins/libautosave.so

#----------------------------------------------------------------------

%package	plugin-colorpicker
Summary:	Color picker plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	plugin-colorpicker
%{summary}

%files plugin-colorpicker
%{_libdir}/%{name}/plugins/libcolorpicker.so

#----------------------------------------------------------------------

%package	plugin-keybindings
Summary:	Keybindings plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	plugin-keybindings
%{summary}

%files plugin-keybindings
%{_libdir}/%{name}/plugins/libkeybindings.so

#----------------------------------------------------------------------

%package	plugin-doclist
Summary:	DocList plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-doclist < %{version}-%{release}

%description	plugin-doclist
%{summary}

%files plugin-doclist
%{_libdir}/%{name}/plugins/libdoclist.so

#----------------------------------------------------------------------

%package	plugin-favorites
Summary:	Favorites plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-favorites < %{version}-%{release}

%description	plugin-favorites
%{summary}

%files plugin-favorites
%{_libdir}/%{name}/plugins/libfavorites.so

#----------------------------------------------------------------------

%package	plugin-findinfiles
Summary:	FindInFiles plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-findinfiles < %{version}-%{release}

%description	plugin-findinfiles
%{summary}

%files plugin-findinfiles
%{_libdir}/%{name}/plugins/libfindinfiles.so

#----------------------------------------------------------------------

%package	plugin-filemanager
Summary:	FileManager plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-filemanager < %{version}-%{release}

%description	plugin-filemanager
%{summary}

%files plugin-filemanager
%{_libdir}/%{name}/plugins/libfm.so

#----------------------------------------------------------------------

%package	plugin-sort
Summary:	SortDocument plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-sort < %{version}-%{release}

%description	plugin-sort
%{summary}

%files plugin-sort
%{_libdir}/%{name}/plugins/libsortdocument.so

#----------------------------------------------------------------------

%package	plugin-symbolbrowser
Summary:	SymbolBrowser plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-symbolbrowser < %{version}-%{release}

%description	plugin-symbolbrowser
%{summary}

%files plugin-symbolbrowser
%{_libdir}/%{name}/plugins/libsymbolbrowser.so

#----------------------------------------------------------------------

%package	plugin-xmlformat
Summary:	XMLFormat plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-xmlformat < %{version}-%{release}

%description	plugin-xmlformat
%{summary}

%files plugin-xmlformat
%{_libdir}/%{name}/plugins/libxmlformat.so

#----------------------------------------------------------------------

%package	plugin-todolist
Summary:	TODO list plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-todolist < %{version}-%{release}

%description	plugin-todolist
%{summary}

%files plugin-todolist
%{_libdir}/%{name}/plugins/libtodolist.so
#----------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{commit}
%apply_patches

# remove bundled libs
rm -rf src/3rd_party

%build
%cmake \
	-DBUILD_TODOLIST:BOOL=ON \
	-DUSE_ENCA:BOOL=ON \
	-DUSE_QT5:BOOL=ON \
	-DUSE_SYSTEM_QTSINGLEAPPLICATION:BOOL=ON \
	-DUSE_SYSTEM_SINGLETON:BOOL=ON \
	%{nil}
%make

%install
%makeinstall_std -C build

